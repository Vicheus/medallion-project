from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    concat,
    concat_ws,
    collect_set,
    flatten,
    trim,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0256"

    def parser(self):
        df_user_agents = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0256/raw/users_agents_preprocessed.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(
                                    lit("buhfest24.ru").alias("title"),
                                    col("user_agent").alias("user_agent"),
                                    device_date_udf(
                                        col("DATE_INSERT"), lit("yyyy-MM-dd HH:mm:ss")
                                    ).alias("date"),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .groupBy(["USER_ID"])
            .agg(flatten(collect_set(col("devices"))).alias("devices"))
            .select("USER_ID", "devices")
        )

        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0256/raw/users_preprocessed.csv",
            sep=",",
            header=True,
        ).replace("NULL", None)

        df = (
            df_users.join(
                df_user_agents, df_user_agents["USER_ID"] == df_users["ID"], "left"
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("WORK_PHONE")),
                            phone_udf(col("LOGIN")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("EMAIL")), email_udf(col("LOGIN")))
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("buhfest24").alias("title"),
                            lit("https://buhfest24.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_DEPARTMENT").isNotNull()
                    | col("WORK_POSITION").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    trim(
                                        concat_ws(
                                            " ",
                                            col("WORK_DEPARTMENT"),
                                            col("WORK_POSITION"),
                                        )
                                    ),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("PERSONAL_CITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_ZIP"),
                                        when(
                                            col("PERSONAL_STREET").isNotNull(),
                                            concat(lit("ул. "), col("PERSONAL_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("PERSONAL_WWW").isNotNull()
                    & (col("PERSONAL_WWW").contains("t.me")),
                    array_compact(
                        array(
                            when(
                                col("PERSONAL_WWW").isNotNull()
                                & (col("PERSONAL_WWW").contains("t.me")),
                                social_udf(
                                    lit("Telegram"),
                                    lit(None),
                                    col("PERSONAL_WWW"),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("LAST_LOGIN"),
                        col("DATE_REGISTER"),
                        col("LAST_ACTIVITY_DATE"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "accounts",
                "devices",
                "works",
                "socials",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
