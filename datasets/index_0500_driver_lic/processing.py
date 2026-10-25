from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    birth_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_driver_lic"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0500/raw/Водительское_удостоверение_2024_@StormBaseAdapter.csv",
            sep=",",
        )

        df = (
            df.withColumn(
                "birth_date", birth_date_udf(col("data_birth"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    col("nomber").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("nomber").isNotNull(),
                                document_udf(
                                    lit("водительское удостоверение"),
                                    col("nomber"),
                                    col("date_action"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select("birth_date", "documents")
        )

        df = df.withColumn(
            "documents",
            when(size(col("documents")) > 0, col("documents")).otherwise(None),
        )

        df = df.filter(col("documents").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
