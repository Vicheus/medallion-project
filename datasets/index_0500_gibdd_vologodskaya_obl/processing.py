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
from pyspark.sql.types import StructType, StructField, StringType


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_gibdd_vologodskaya_obl"
    calc_completeness: bool = False
    output_file_count: int = 10

    def parser(self):
        schema = StructType(
            [
                StructField("ФИО", StringType(), True),
                StructField("Дата рождения", StringType(), True),
                StructField("vehicle_model_1", StringType(), True),
                StructField("vehicle_number_1", StringType(), True),
                StructField("vehicle_model_2", StringType(), True),
                StructField("vehicle_number_2", StringType(), True),
                StructField("vehicle_model_3", StringType(), True),
                StructField("vehicle_number_3", StringType(), True),
                StructField("vehicle_model_4", StringType(), True),
                StructField("vehicle_number_4", StringType(), True),
                StructField("vehicle_model_5", StringType(), True),
                StructField("vehicle_number_5", StringType(), True),
                StructField("vehicle_model_6", StringType(), True),
                StructField("vehicle_number_6", StringType(), True),
                StructField("vehicle_model_7", StringType(), True),
                StructField("vehicle_number_7", StringType(), True),
                StructField("vehicle_model_8", StringType(), True),
                StructField("vehicle_number_8", StringType(), True),
                StructField("vehicle_model_9", StringType(), True),
                StructField("vehicle_number_9", StringType(), True),
                StructField("vehicle_model_10", StringType(), True),
                StructField("vehicle_number_10", StringType(), True),
            ]
        )

        df = (
            self.read(
                path="/home/user/Documents/shared/Водители_ГИБДД_Вологодской_Области_2008_output.csv",
                sep=",",
                schema=schema,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "vehicles",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("vehicle_model_1").isNotNull()
                                & col("vehicle_number_1").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_1"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_1"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_2").isNotNull()
                                & col("vehicle_number_2").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_2"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_2"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_3").isNotNull()
                                & col("vehicle_number_3").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_3"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_3"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_4").isNotNull()
                                & col("vehicle_number_4").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_4"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_4"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_5").isNotNull()
                                & col("vehicle_number_5").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_5"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_5"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_6").isNotNull()
                                & col("vehicle_number_6").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_6"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_6"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_7").isNotNull()
                                & col("vehicle_number_7").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_7"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_7"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_8").isNotNull()
                                & col("vehicle_number_8").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_8"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_8"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_9").isNotNull()
                                & col("vehicle_number_9").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_9"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_9"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
                            when(
                                col("vehicle_model_10").isNotNull()
                                & col("vehicle_number_10").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_10"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_number_10"),
                                    lit(None),
                                    lit(None),
                                ),
                            ),
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
