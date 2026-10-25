from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, size, from_json, expr
from pyspark.sql.types import (
    ArrayType,
    StructType,
    StructField,
    StringType,
    BooleanType,
    IntegerType,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import names_udf, phone_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0539"

    def parser(self):
        schema = ArrayType(
            StructType(
                [
                    StructField("name", StringType(), True),
                    StructField("isSpam", BooleanType(), True),
                    StructField("occurrences", IntegerType(), True),
                ]
            )
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0539/raw/VіеwСаІІеr.csv",
                sep=",",
                header=True,
            )
            .withColumn("parsed_names", from_json(col("names"), schema))
            .withColumn("names", expr("transform(parsed_names, x -> x.name)"))
            .withColumn("names", names_udf(col("names")))
            .withColumn(
                "phones", phone_udf(col("phone"), lit(self.dataset_country_code))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .select("names", "phones", "actuality")
        )

        df = df.dropDuplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(size(col("names")) > 0, col("names")).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
