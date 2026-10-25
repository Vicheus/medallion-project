from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
    size,
    split,
    lower,
    lit,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phones_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0435"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0435/raw/preprocessed/csv/users.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(array_distinct(phones_udf(split(col("newphone"), ",")))),
            )
            .withColumn(
                "address",
                when(lower(col("address")).contains("http"), lit(None)).otherwise(
                    address_udf(col("address"))
                ),
            )
            .select("names", "phones", "address")
        )

        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
