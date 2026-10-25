from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    regexp_extract,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0117"

    def parser(self):
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0117/raw/preprocessed/webleo_preprocessed_stage_2.csv",
            sep=",",
            header=True,
        )

        vk_pattern = r"https://vk\.com/([^/]+)"
        instagram_pattern = r"https://instagram\.com/([^/]+)"

        df = (
            df.replace("NULL", None)
            .replace("-", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("name1")), name_udf(col("name2")))
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("vk_id", regexp_extract(col("link"), vk_pattern, 1))
            .withColumn(
                "instagram_id", regexp_extract(col("link"), instagram_pattern, 1)
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("passport").isNotNull(),
                        document_udf(
                            lit("паспорт гражданина рф"),
                            col("passport"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None),
                    when(
                        col("inn").isNotNull(),
                        document_udf(
                            lit("инн"),
                            col("inn"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None),
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("vk_id").isNotNull() & (col("vk_id") != ""),
                            struct(
                                lit("Vk").alias("title"),
                                col("vk_id").alias("id"),
                                col("link").alias("link"),
                            ),
                        ).otherwise(None),
                        when(
                            col("instagram_id").isNotNull()
                            & (col("instagram_id") != ""),
                            struct(
                                lit("Instagram").alias("title"),
                                col("instagram_id").alias("id"),
                                col("link").alias("link"),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .select("names", "emails", "socials", "phones", "documents", "address")
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
                | col("socials").isNotNull()
            )
        )

        df = df.select("names", "emails", "socials", "phones", "documents", "address")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
