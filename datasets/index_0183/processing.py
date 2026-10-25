from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    concat,
    size,
    regexp_extract,
    concat_ws,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0183"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"
        twitter_pattern = r"https://twitter.com/([a-zA-Z0-9_]+)"
        ok_pattern = r"http://odnoklassniki.ru/profile/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0183/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 0))
            .withColumn(
                "facebook_link", regexp_extract("PERSONAL_WWW", facebook_pattern, 0)
            )
            .withColumn("ok_link", regexp_extract("PERSONAL_WWW", ok_pattern, 0))
            .withColumn(
                "twitter_link", regexp_extract("PERSONAL_WWW", twitter_pattern, 0)
            )
            .withColumn(
                "instagram_link", regexp_extract("PERSONAL_WWW", instagram_pattern, 0)
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
                            phone_udf(
                                col("PERSONAL_PHONE"),
                                lit(self.dataset_country_code.value),
                            ),
                            phone_udf(
                                col("PERSONAL_MOBILE"),
                                lit(self.dataset_country_code.value),
                            ),
                            phone_udf(
                                col("LOGIN"), lit(self.dataset_country_code.value)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(concat(array(email_udf(col("EMAIL")))))),
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
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Amihome.by").alias("title"),
                            lit("https://amihome.by").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_link").isNotNull()
                    | col("facebook_link").isNotNull()
                    | col("ok_link").isNotNull()
                    | col("twitter_link").isNotNull(),
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
                            when(
                                col("ok_link").isNotNull(),
                                social_udf(
                                    lit("Ok"), lit(None), col("ok_link"), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_link").isNotNull(),
                                social_udf(
                                    lit("Twitter"),
                                    lit(None),
                                    col("twitter_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_link").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    lit(None),
                                    col("instagram_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "socials",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            flatten(collect_set(col("names"))).alias("names"),
            flatten(collect_set(col("address"))).alias("address"),
            flatten(collect_set(col("accounts"))).alias("accounts"),
            flatten(collect_set(col("socials"))).alias("socials"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
