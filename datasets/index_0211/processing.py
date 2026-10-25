from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    greatest,
    max,
    size,
    regexp_extract,
    concat,
    concat_ws,
    flatten,
    collect_set,
)

from parsetron import Parsetron
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
    dataset_code_name: str = "index_0211"
    output_file_count: int = 5

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"

        df_main = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0211/raw/leroymerlin/main.csv",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("TITLE", lit(None))
            .withColumn("BX_USER_ID", lit(None))
            .withColumn("LANGUAGE_ID", lit(None))
            .coalesce(5)
        )

        df_market = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0211/raw/leroymerlin/market.csv",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .coalesce(5)
        )

        df = df_main.unionAll(df_market).drop_duplicates()

        df = (
            df.withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 0))
            .withColumn(
                "facebook_link", regexp_extract("PERSONAL_WWW", facebook_pattern, 0)
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")),
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
                            phone_udf(col("PERSONAL_FAX")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("PERSONAL_PAGER")),
                            phone_udf(col("WORK_PHONE")),
                            phone_udf(col("WORK_FAX")),
                            phone_udf(col("WORK_PAGER")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("EMAIL")),
                            email_udf(col("PERSONAL_MAILBOX")),
                            email_udf(col("LOGIN")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
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
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Леруа Мерлен").alias("title"),
                            lit("https://leroymerlin.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            col("ID").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_POSITION").isNotNull() | col("WORK_COMPANY").isNotNull(),
                    array(
                        work_udf(
                            col("WORK_POSITION"),
                            lit(None),
                            lit(None),
                            col("WORK_COMPANY"),
                            address_udf(
                                when(
                                    col("WORK_CITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("WORK_CITY"),
                                        col("WORK_ZIP"),
                                        when(
                                            col("WORK_STREET").isNotNull(),
                                            concat(lit("ул. "), col("WORK_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_link").isNotNull() | col("facebook_link").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_link").isNotNull(),
                                social_udf(
                                    lit("Vk"), lit(None), col("vk_link"), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_link").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    lit(None),
                                    col("facebook_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
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
        )

        df.show()

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "accounts",
            "works",
            "socials",
            "actuality",
        ).coalesce(1)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            collect_set(col("names")).alias("names"),
            flatten(collect_set(col("works"))).alias("works"),
            flatten(collect_set(col("accounts"))).alias("accounts"),
            flatten(collect_set(col("socials"))).alias("socials"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
