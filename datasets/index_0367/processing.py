from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0367"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0367/raw/автоцентр_Lada_2022.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%M.%Y"))
            )
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn(
                "vehicles",
                when(
                    (col("Машина").isNotNull() & (col("Машина") != "")),
                    vehicle_udf(
                        lit(1),
                        col("Машина"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .select("names", "birth_date", "phones", "vehicles")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(col("vehicles").isNotNull(), array(col("vehicles"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
