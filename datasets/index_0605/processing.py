from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, actuality_date_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0605"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0605/raw/20260327-112406-234-file-Январь_2021_4935_с_тел.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Телефон1")), phone_udf(col("Телефон2")))
                    )
                ),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("Г_Н").isNotNull() & (col("Г_Н") != ""))
                    | (col("VIN").isNotNull() & (col("VIN") != ""))
                    | col("Марка_Модель").isNotNull() & (col("Марка_Модель") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("Марка_Модель"),
                            col("гв").cast("int"),
                            lit(None),
                            col("Г_Н"),
                            col("VIN"),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("actuality", actuality_date_udf(col("Дата"), lit("%m/%d/%Y")))
            .select("names", "phones", "vehicles", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("vehicles").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
