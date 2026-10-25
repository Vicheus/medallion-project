from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    when,
    struct,
    size,
    regexp_extract,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0085"

    def parser(self):
        df_users_registered = self.read(
            path="AtlasBus/AtlasBus.ru_пользователи.csv", sep=",", header=True
        )
        df_emails = self.read(
            path="AtlasBus/AtlasBus.ru_обратная_связь_emails.csv", sep=",", header=True
        )
        df_users_not_registered = self.read(
            path="AtlasBus/AtlasBus.ru_not_register_пользователи.csv",
            sep=",",
            header=True,
        )

        df_users_registered = (
            df_users_registered.withColumn("user_id", col("ID"))
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("email_1", email_udf(col("EMAIL")))
            .withColumn("email_2", email_udf(col("PERSONAL_MAILBOX")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("LOGIN")),
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("WORK_PHONE")),
                        )
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDATE"), lit("%Y-%m-%d"))
            )
            .withColumn("login", col("LOGIN"))
            .withColumn("password", col("PASSWORD"))
            .withColumn(
                "vk", regexp_extract(col("PERSONAL_NOTES"), r"(?<=VK_ID=)\d+", 0)
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("LAST_LOGIN"), col("DATE_REGISTER")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "user_id",
                "names",
                "email_1",
                "email_2",
                "phones",
                "sex",
                "birth_date",
                "login",
                "password",
                "vk",
                "actuality",
            )
        )

        df_emails = (
            df_emails.filter(col("UF_EMAIL") != "landyrev@atlasbus.ru")
            .withColumn("user_id", col("UF_USER_ID"))
            .withColumn("email_3", email_udf(col("UF_EMAIL")))
            .select("user_id", "email_3")
        )

        df_users_not_registered = (
            df_users_not_registered.withColumn(
                "names",
                name_parts_udf(col("UF_UNR_NAME"), col("UF_UNR_LAST_NAME"), lit(None)),
            )
            .withColumn("phones", array_compact(array(phone_udf(col("UF_LOGIN_UNR")))))
            .withColumn("emails", array())
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("login", lit(None))
            .withColumn("password", lit(None))
            .withColumn("vk", lit(None))
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "login",
                "password",
                "vk",
                "actuality",
            )
        )

        df_users_registered = (
            df_users_registered.join(df_emails, "user_id", "inner")
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(col("email_1"), col("email_2"), col("email_3"))
                    )
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "login",
                "password",
                "vk",
                "actuality",
            )
        )

        df = (
            df_users_registered.unionAll(df_users_not_registered)
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Атлас").alias("title"),
                            lit("https://atlasbus.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk").isNotNull(),
                                struct(
                                    lit("ВКонтакте").alias("title"),
                                    col("vk").alias("id"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "accounts",
                "socials",
                "actuality",
            )
        )

        df = df.dropDuplicates(["names", "phones", "emails"])

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("socials").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
