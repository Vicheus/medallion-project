from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    size,
    array_distinct,
    array_compact,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import name_udf, phone_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0461"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0461/raw/clients.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("fullname")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("brand"), col("brand")))
            .select("names", "phones", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "phones"])

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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
