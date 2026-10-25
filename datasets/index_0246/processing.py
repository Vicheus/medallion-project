from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0246"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0246/raw/onlinegibdd.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("user_name"), col("user_lst_name"), col("user_patro")
                ),
            )
            .withColumn("emails", email_udf(col("user_mail")))
            .withColumn("phones", phone_udf(col("user_phone")))
            .withColumn("address", address_udf(col("user_region")))
            .withColumn(
                "socials",
                when(
                    col("facebook_id").isNotNull()
                    | col("vkontakte_id").isNotNull()
                    | col("yandex_id").isNotNull()
                    | col("google_id").isNotNull()
                    | col("twitter_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("facebook_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("vkontakte_id").isNotNull(),
                                social_udf(
                                    lit("Vk"), col("vkontakte_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("yandex_id").isNotNull(),
                                social_udf(
                                    lit("Yandex"),
                                    col("yandex_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("google_id").isNotNull(),
                                social_udf(
                                    lit("Google Plus"),
                                    col("google_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_id").isNotNull(),
                                social_udf(
                                    lit("Twitter"),
                                    col("twitter_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_register"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "phones", "address", "socials", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
