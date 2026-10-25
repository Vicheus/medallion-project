from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    size,
    array,
    lit,
    regexp_extract,
    array_compact,
    length,
)
from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import name_udf, email_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0415"

    def parser(self):
        vk_pattern = r"^https?://(www\.)?vk\.com/([a-zA-Z0-9_.-]+)$"
        facebook_pattern = r"^https?://(www\.)?facebook\.com/([a-zA-Z0-9_.-]+)$"
        ok_pattern = r"^https?://(www\.)?odnoklassniki\.ru/profile/([a-zA-Z0-9_.-]+)$"
        instagram_pattern = r"^https?://(www\.)?instagram\.com/([a-zA-Z0-9_.-]+)$"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0415/raw/VMasshtabe.ru_2023_1,3kk.json",
                sep="\n",
            )
            .withColumn("names", name_udf(col("_source.display_name")))
            .withColumn("emails", email_udf(col("_source.user_email")))
            .withColumn("vk_id", regexp_extract("_source.user_url", vk_pattern, 2))
            .withColumn(
                "facebook_id", regexp_extract("_source.user_url", facebook_pattern, 2)
            )
            .withColumn("ok_id", regexp_extract("_source.user_url", ok_pattern, 2))
            .withColumn(
                "instagram_id", regexp_extract("_source.user_url", instagram_pattern, 2)
            )
            .withColumn("social_link", col("_source.user_url"))
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull()
                    | col("facebook_id").isNotNull()
                    | col("ok_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull() & (length(col("vk_id")) > 0),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull()
                                & (length(col("facebook_id")) > 0),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("ok_id").isNotNull() & (length(col("ok_id")) > 0),
                                social_udf(
                                    lit("Ok"),
                                    col("ok_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_id").isNotNull()
                                & (length(col("instagram_id")) > 0),
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
                    col("_source.user_registered"), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("names", "emails", "socials", "actuality")
        )

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
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
        )
        df = df.select("names", "emails", "socials", "actuality")

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
