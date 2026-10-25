from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    concat,
    concat_ws,
    array_distinct,
    struct,
    greatest,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    sex_udf,
    address_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    output_file_count: int = 10
    test_mode: bool = False
    dataset_code_name: str = "index_0329"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"
        twitter_pattern = r"https://twitter.com/([a-zA-Z0-9_]+)"
        ok_pattern = r"http://odnoklassniki.ru/profile/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0329/raw/stolplit_ru/b_user.csv",
            sep=";",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .withColumn("social_link", col("PERSONAL_WWW"))
            .withColumn("vk_id", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "facebook_id", regexp_extract("PERSONAL_WWW", facebook_pattern, 1)
            )
            .withColumn("ok_id", regexp_extract("PERSONAL_WWW", ok_pattern, 1))
            .withColumn(
                "twitter_id", regexp_extract("PERSONAL_WWW", twitter_pattern, 1)
            )
            .withColumn(
                "instagram_id", regexp_extract("PERSONAL_WWW", instagram_pattern, 1)
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
            .withColumn("emails", email_udf(col("EMAIL")))
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
                            lit("СТОЛПЛИТ").alias("title"),
                            lit("https://www.stolplit.ru").alias("link"),
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
                    array_compact(
                        array_distinct(
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
                                                    concat(
                                                        lit("ул. "), col("WORK_STREET")
                                                    ),
                                                ).otherwise(None),
                                            ),
                                        )
                                    ),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull()
                    | col("facebook_id").isNotNull()
                    | col("ok_id").isNotNull()
                    | col("twitter_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("ok_id").isNotNull(),
                                social_udf(
                                    lit("Ok"),
                                    col("ok_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_id").isNotNull(),
                                social_udf(
                                    lit("Twitter"),
                                    col("twitter_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_id").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    col("instagram_id"),
                                    col("social_link"),
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = df.drop_duplicates()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
