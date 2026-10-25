from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0498"
    output_file_count: int = 50
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0498/raw/1cont.txt",
                sep="|",
                header=True,
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array(address_with_type_udf(col("address"), lit(3)))
                ),
            )
        )
        df_persons = (
            df.withColumn("names", name_udf(col("ceo")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "works",
                when(
                    col("org_name").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                lit(None),
                                lit(None),
                                col("org_name"),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn("documents", array())
            .select(
                "names",
                "address",
                "addresses",
                "phones",
                "emails",
                "works",
                "documents",
            )
        )

        df_companies = (
            df.withColumn("names", name_udf(col("org_name")))
            .withColumn(
                "documents",
                array_compact(
                    array(
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
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn("emails", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("works", array())
            .select(
                "names",
                "address",
                "addresses",
                "phones",
                "emails",
                "works",
                "documents",
            )
        )

        df = df_persons.unionAll(df_companies)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(col("addresses").isNotNull(), array(col("addresses"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
