from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array
from parsetron import Parsetron

from parsetron.sections.main.udfs import name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0458"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0458/raw/Магазин_техники_Pro-Katalog_02_2023.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("Почта")))
            .select("names", "emails")
        )

        df = df.drop_duplicates(["names", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
