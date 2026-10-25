from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
    flatten,
    collect_set,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import phone_udf, actuality_date_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_parking_mos_groupped"
    calc_completeness: bool = False
    output_file_count: int = 10

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/shared/parking*.csv", sep="|", header=False
            )
            .withColumn("phones", phone_udf(col("_c0")))
            .withColumn(
                "vehicles",
                when(
                    col("_c1").isNotNull() & (col("_c1") != ""),
                    array_compact(
                        array_distinct(
                            array(
                                vehicle_udf(
                                    lit(1),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("_c1"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("_c6"), lit("%d.%m.%Y %H:%M:%S"))
            )
            .select("phones", "vehicles", "actuality")
        )

        df = df.groupBy(["phones"]).agg(
            array_compact(array_distinct(flatten(collect_set(col("vehicles"))))).alias(
                "vehicles"
            ),
            max(col("actuality")).alias("actuality"),
        )

        df = df.withColumn(
            "phones",
            when(
                col("phones").isNotNull(), array_compact(array(col("phones")))
            ).otherwise(None),
        ).withColumn(
            "vehicles", when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None)
        )

        df = df.filter(col("vehicles").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
