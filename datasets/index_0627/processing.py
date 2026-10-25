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
    raw_metadata_udf,
    address_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0627"

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0627/raw/Такси_Москва_2019.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("address", address_udf(col("ГОРОД")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("ТЕЛЕФОН"))))),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("НОМЕР АВТО").isNotNull() & (col("НОМЕР АВТО") != ""))
                    | col("МОДЕЛЬ").isNotNull() & (col("МОДЕЛЬ") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("МОДЕЛЬ"),
                            lit(None),
                            col("ЦВЕТ"),
                            col("НОМЕР АВТО"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("КЛАСС"), col("КЛАСС"), lit("СЛУЖБА ТАКСИ"), col("СЛУЖБА ТАКСИ")
                ),
            )
            .select("names", "raw_metadata", "address", "phones", "vehicles")
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
