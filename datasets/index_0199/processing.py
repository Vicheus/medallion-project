from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0199"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0199/raw/rabotaitochkahr.csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("mobile_phone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("request_date"), lit("%Y-%m-%d %H:%M")),
            )
            .select("names", "phones", "actuality")
            .drop_duplicates(["names", "phones"])
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
