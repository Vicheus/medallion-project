from pyspark import StorageLevel

from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0399"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0399/raw/bdPropalaRu.txt",
                sep=",",
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("phones", phone_udf(col("Number")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("WhoMiss"), col("WhoMiss"))
            )
            .select("names", "phones", "raw_metadata")
        )

        df = df.drop_duplicates(["phones"])

        df.cache()

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
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
