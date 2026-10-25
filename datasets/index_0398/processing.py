from pyspark import StorageLevel

from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, address_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0398"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0398/raw/agroserver - @bereza_bd.csv",
                sep="|",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("tel")))
            .select("names", "phones", "address")
        )

        df = df.drop_duplicates(["phones"])

        df.cache()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
