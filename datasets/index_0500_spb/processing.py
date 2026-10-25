from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, birth_date_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_spb"
    calc_completeness: bool = False
    output_file_count: int = 10

    def parser(self):
        df = (
            self.read(path="/home/user/Documents/shared/ГИБДД_СПБ_2005.csv", sep=",")
            .withColumn("names", name_udf(col("ФИО владельца")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("Дата рождения владельца"), lit("%Y-%m-%d")),
            )
            .withColumn(
                "vehicles",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Государственный номер").isNotNull()
                                & col("Модель").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("Модель"),
                                    when(
                                        col("Год выпуска").rlike("^[0-9]+$"),
                                        col("Год выпуска").cast("int"),
                                    ).otherwise(None),
                                    lit(None),
                                    col("Государственный номер"),
                                    col("VIN"),
                                    lit(None),
                                ),
                            )
                        )
                    )
                ),
            )
            .select("names", "birth_date", "vehicles")
        )

        df = df.withColumn(
            "names",
            when(
                col("names").isNotNull(), array_compact(array(col("names")))
            ).otherwise(None),
        ).withColumn(
            "vehicles", when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None)
        )

        df = df.filter(col("vehicles").isNotNull() & col("names").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
