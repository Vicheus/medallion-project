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
    flatten,
    collect_set,
    first,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0269"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0269/raw/vezetvsem/vezetvsem-user_profile.txt",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("first_name", regexp_replace(col("first_name"), "\.", ""))
            .withColumn("last_name", regexp_replace(col("last_name"), "\.", ""))
            .withColumn("middle_name", regexp_replace(col("middle_name"), "\.", ""))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone_home")),
                            phone_udf(col("phone_office")),
                            phone_udf(col("phone_mobile")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("actuality", lit(None))
            .withColumn(
                "socials",
                when(
                    col("skype").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("skype").isNotNull(),
                                social_udf(
                                    lit("Skype"), col("skype"), lit(None), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select("user_id", "names", "emails", "phones", "birth_date", "socials")
        )

        df_1.show(n=10)

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0269/raw/vezetvsem/vezetvsem-users.txt",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("emails2", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("last_ip")))
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("username").isNotNull(),
                    array(
                        struct(
                            lit("Везёт Всем").alias("title"),
                            lit("https://vezetvsem.ru/").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("last_login"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_login"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )
        df = (
            df_1.join(df_2, df_1["user_id"] == df_2["id"], "left")
            .withColumn(
                "emails",
                array_compact(array_distinct(array(col("emails"), col("emails2")))),
            )
            .select(
                "names", "emails", "phones", "birth_date", "socials", "ips", "accounts"
            )
        )

        df = (
            df.groupBy(["names", "phones", "emails"])
            .agg(
                first(col("birth_date")).alias("birth_date"),
                array_compact(
                    array_distinct(flatten(collect_set(col("socials"))))
                ).alias("socials"),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("accounts"))))
                ).alias("accounts"),
            )
            .select(
                "names", "emails", "phones", "birth_date", "socials", "ips", "accounts"
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
