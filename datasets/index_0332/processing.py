from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0332"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0332/raw/philharmonia.spb.ru_2023.txt",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names", name_parts_udf(col("Фамилия"), col("Имя"), lit(None))
            )
            .withColumn("emails", email_udf(col("Почта")))
            .select("names", "emails")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
