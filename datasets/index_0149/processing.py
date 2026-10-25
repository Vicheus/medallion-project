from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0149"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0149/raw/annex/dump_accounts_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("fullname")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone_m")),
                            phone_udf(col("phone_h")),
                            phone_udf(col("phone_w")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email1")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    col("passport_date"),
                                    lit(None),
                                    col("passport_given"),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("company"),
                            address_udf(
                                when(
                                    col("company_address").isNotNull(),
                                    col("company_address"),
                                ).otherwise(None)
                            ),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "works", "documents")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=10, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
