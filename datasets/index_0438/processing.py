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
    regexp_extract,
    concat_ws,
)

from parsetron import Parsetron

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
    dataset_code_name: str = "index_0438"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0438/raw/eksmo.csv",
            sep="\t",
            header=True,
        )

        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"
        twitter_pattern = r"https://twitter.com/([a-zA-Z0-9_]+)"
        ok_pattern = r"http://odnoklassniki.ru/profile/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"
        google_plus_pattern = r"https://plus.google.com/([a-zA-Z0-9_]+)"

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("LOGIN")), email_udf(col("EMAIL")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("PERSONAL_PHONE"))))),
            )
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
                "google_plus_id", regexp_extract("PERSONAL_WWW", google_plus_pattern, 1)
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(" ", col("PERSONAL_CITY"), col("PERSONAL_STREET"))
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Книжный интернет-магазин Эксмо").alias("title"),
                            lit("https://eksmo.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
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
                                col("vk_id").isNotNull() & (col("vk_id") != ""),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull()
                                & (col("facebook_id") != ""),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("ok_id").isNotNull() & (col("ok_id") != ""),
                                social_udf(
                                    lit("Ok"),
                                    col("ok_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_id").isNotNull()
                                & (col("twitter_id") != ""),
                                social_udf(
                                    lit("Twitter"),
                                    col("twitter_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_id").isNotNull()
                                & (col("instagram_id") != ""),
                                social_udf(
                                    lit("Instagram"),
                                    col("instagram_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("google_plus_id").isNotNull()
                                & (col("google_plus_id") != ""),
                                social_udf(
                                    lit("GooglePlus"),
                                    col("google_plus_id"),
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
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "actuality",
                "socials",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
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
            .withColumn(
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
