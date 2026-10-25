from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0495"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0495/raw/2gis.ru - @StormBaseAdapter.txt",
                sep=";",
                header=False,
            )
            .filter(col("_c1") != "Городской житель")
            .withColumn("names", name_udf(col("_c1")))
            .withColumn("phones", phone_udf(col("_c0")))
            .select("names", "phones")
        )

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
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
