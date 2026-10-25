from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0202"

    def parser(self):
        schema = StructType(
            [
                StructField("phone", StringType(), nullable=True),
                StructField("product_name", StringType(), nullable=True),
                StructField("price", StringType(), nullable=True),
                StructField("name", StringType(), nullable=True),
                StructField("unknown_column_2", StringType(), nullable=True),
                StructField("url", StringType(), nullable=True),
            ]
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0202/raw/flado.ru_2025_preprocessed.txt",
                sep=":",
                header=False,
                schema=schema,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("product_name"), col("product_name"), lit("price"), col("price")
                ),
            )
            .select("names", "phones", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
