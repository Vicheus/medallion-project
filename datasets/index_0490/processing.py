from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    split,
    concat_ws,
    max,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phones_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0490"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0490/raw/osago_23/*.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phones_udf(split(col("phones"), ",")))
            .withColumn(
                "address",
                address_udf(
                    when(
                        col("address1") != col("address2"),
                        concat_ws(" ", col("address1"), col("address2")),
                    ).otherwise(col("address1"))
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("insurance_policy").isNotNull(),
                                document_udf(
                                    lit("номер страхового полиса"),
                                    col("insurance_policy"),
                                    col("date_from"),
                                    col("date_to"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "vehicles",
                when(
                    (
                        col("plate_num").isNotNull()
                        | col("vin").isNotNull()
                        | col("vehicle_mark").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        concat_ws(" ", col("vehicle_mark"), col("vehicle_model")),
                        col("year").cast("int"),
                        lit(None),
                        col("plate_num"),
                        col("vin"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date_from"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("insurance_company"),
                    col("insurance_company"),
                    lit("vehicle_horse_power"),
                    col("col0"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "documents",
                "vehicles",
                "raw_metadata",
                "actuality",
            )
        )

        df_with_b_date = df.filter(
            (col("names").isNotNull()) & (col("birth_date").isNotNull())
        )
        df_without_b_date = (
            df.filter((col("birth_date").isNull()))
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("vehicles", array_compact(array(col("vehicles"))))
            .withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_with_b_date = (
            df_with_b_date.filter(
                (col("names").isNotNull()) & (col("birth_date").isNotNull())
            )
            .groupBy(["names", "birth_date"])
            .agg(
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("vehicles")))).alias(
                    "vehicles"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_with_b_date.unionAll(df_without_b_date)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("vehicles").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
