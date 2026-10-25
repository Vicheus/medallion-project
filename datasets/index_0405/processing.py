from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
)
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0405"
    output_file_count: int = 20
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0405/raw/combined_results_pages.csv"
        )

        df = (
            df.withColumn("names", name_udf(col("Company Name")))
            .withColumn("address", address_udf(col("Company Address")))
            .withColumn(
                "documents",
                when(
                    col("INN").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("INN"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Company Full Name"),
                    col("Company Full Name"),
                    lit("Company Activity"),
                    col("Company Activity"),
                    lit("Management and Registration Info (Raw)"),
                    col("Management and Registration Info (Raw)"),
                    lit("Financial Info (Raw)"),
                    col("Financial Info (Raw)"),
                    lit("Director Name"),
                    col("Director Name"),
                    lit("Registration Date"),
                    col("Registration Date"),
                    lit("Net Profit"),
                    col("Net Profit"),
                    lit("Capital"),
                    col("Capital"),
                ),
            )
            .select("names", "address", "documents", "raw_metadata")
        )

        df = df.repartition(self.output_file_count)

        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("address").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
