from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0132"

    def parser(self):
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0132/raw/infourok.ru (2024).txt",
            sep=",",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .replace("None", None)
            .filter(col("Страна") == "Россия")
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%M.%Y"))
            )
            .withColumn(
                "works",
                when(
                    col("Должность").isNotNull() | col("Место работы").isNotNull(),
                    array(
                        work_udf(
                            col("Должность"),
                            lit(None),
                            lit(None),
                            col("Место работы"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "birth_date", "works")
        )

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "works",
            when(
                size(array_compact(col("works"))) > 0, array_compact(col("works"))
            ).otherwise(None),
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & col("works").isNotNull())

        df = df.select("names", "birth_date", "works")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
