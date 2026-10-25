from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_distinct, array_compact, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0381"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0381/raw/vird.ru/vird_ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("Номер телефона1")),
                            phone_udf(col("Номер телефона2")),
                        )
                    )
                ),
            )
            .select("names", "phones")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
