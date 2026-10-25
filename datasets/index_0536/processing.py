from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    size,
    length,
    flatten,
    max,
)

from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, actuality_date_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0536"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0536/raw/*.csv",
                sep=",",
                header=False,
            )
            .filter(col("_c5") != "блок")
            .withColumn("names", name_udf(col("_c5")))
            .withColumn("phones", phone_udf(col("_c6"), lit(self.dataset_country_code)))
            .withColumn(
                "vehicle_number",
                when(
                    col("_c8").isNull(),
                    when(length(col("_c9")) > 4, col("_c9")).otherwise(None),
                ).otherwise(col("_c8")),
            )
            .withColumn(
                "vehicles",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("_c8").isNotNull(),
                                vehicle_udf(
                                    lit(1),
                                    col("_c7"),
                                    when(
                                        col("_c9").rlike("^-?\\d+$"),
                                        col("_c9").cast("int"),
                                    ),
                                    lit(None),
                                    col("vehicle_number"),
                                    lit(None),
                                    lit(None),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn("actuality", actuality_date_udf(col("_c1"), lit("%d.%m.%Y")))
            .select("names", "phones", "vehicles", "actuality")
        )

        df = df.filter(col("phones").isNotNull())

        df = df.groupBy(["phones"]).agg(
            array_distinct(array_compact(collect_set(col("names")))).alias("names"),
            array_distinct(array_compact(flatten(collect_set(col("vehicles"))))).alias(
                "vehicles"
            ),
            max("actuality").alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
