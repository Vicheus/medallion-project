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
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0604"

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0604/raw/20260326-122219-933-file-МОС ОСАГО июль 2022(1).csv",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("address", address_udf(col("город")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Телефон"))))),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("Госномер").isNotNull() & (col("Госномер") != ""))
                    | (col("VIN").isNotNull() & (col("VIN") != ""))
                    | col("Модель").isNotNull() & (col("Модель") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("Модель"),
                            lit(None),
                            lit(None),
                            col("Госномер"),
                            col("VIN"),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "birth_date", "address", "phones", "vehicles")
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
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
