from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    lit,
    regexp_extract,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0384"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"
        twitter_pattern = r"https://twitter.com/([a-zA-Z0-9_]+)"
        ok_pattern = r"http://odnoklassniki.ru/profile/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0384/raw/sport-marafon.ru/sport-marafon.ru (04.2023).txt",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%m.%d"))
            )
            .withColumn("vk_link", regexp_extract("Социальная сеть", vk_pattern, 0))
            .withColumn(
                "facebook_link", regexp_extract("Социальная сеть", facebook_pattern, 0)
            )
            .withColumn("ok_link", regexp_extract("Социальная сеть", ok_pattern, 0))
            .withColumn(
                "twitter_link", regexp_extract("Социальная сеть", twitter_pattern, 0)
            )
            .withColumn(
                "instagram_link",
                regexp_extract("Социальная сеть", instagram_pattern, 0),
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
            .select("names", "birth_date", "phones", "emails", "address", "socials")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
