from parsetron.settings import DATASET_COUNTRY_CODE
from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    flatten,
    first,
    max,
    size,
    to_timestamp,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    raw_metadata_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import movement_udf, movement_datetime_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0493"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 50
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0483/raw/kordon2024.parquet"
            )
            .replace("NULL", None)
            .withColumn(
                "parsed_date", to_timestamp(col("date_fixed"), "yyyy-MM-dd HH:mm:ss")
            )
            .filter(col("parsed_date") < "2023-01-01")
        )

        df = df.filter(
            (col("document_issue_country") != "УКРАИНА")
            & (col("document_issue_country") == "БЕЛАРУСЬ")
        )

        df.show(n=200)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date_fixed"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    col("document_data").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                when(
                                    col("document_data").isNotNull(),
                                    document_udf(
                                        lit(None),
                                        col("document_data"),
                                        col("document_issue_date_fixed"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("%Y-%m-%d"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    (
                        col("license_number").isNotNull()
                        & (col("transport_type") == "АВТОМОБИЛЬНЫЙ ТРАНСПОРТ")
                        & col("carrier").isNull()
                    ),
                    array_compact(
                        array_distinct(
                            array(
                                vehicle_udf(
                                    lit(1),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("license_number"),
                                    lit(None),
                                    lit(None),
                                ),
                            )
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "movements",
                array_compact(
                    array_distinct(
                        array(
                            movement_udf(
                                movement_datetime_udf(
                                    col("date_fixed"),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                                col("departure_country"),
                                when(
                                    col("departure_city").isNotNull(),
                                    col("departure_city"),
                                ).otherwise(col("checkpoint")),
                                lit(None),
                                lit(None),
                                col("arrival_country"),
                                when(
                                    col("arrival_city").isNotNull(),
                                    col("arrival_city"),
                                ).otherwise(col("checkpoint")),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("transport_type") == "АВИАЦИОННЫЙ ТРАНСПОРТ",
                                    when(
                                        col("flight_number").isNotNull(),
                                        col("flight_number"),
                                    ).otherwise(col("license_number")),
                                ),
                                lit(None),
                                when(
                                    col("transport_type") == "АВИАЦИОННЫЙ ТРАНСПОРТ",
                                    2,
                                )
                                .when(
                                    (col("transport_type") == "АВТОМОБИЛЬНЫЙ ТРАНСПОРТ")
                                    & (col("carrier").isNull()),
                                    1,
                                )
                                .when(
                                    (col("transport_type") == "АВТОМОБИЛЬНЫЙ ТРАНСПОРТ")
                                    & (col("carrier").isNotNull()),
                                    3,
                                )
                                .when(
                                    (col("transport_type") == "ПЕРЕДВИЖЕНИЕ ПЕШКОМ")
                                    & (col("carrier").isNull()),
                                    0,
                                )
                                .otherwise(None),
                                lit(None),
                                lit(None),
                                col("carrier"),
                                lit(None),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("license_number"), col("license_number")),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_fixed"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "vehicles",
                "movements",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        result_df = df.filter(
            col("names").isNotNull()
            & (col("birth_date").isNotNull() | (size(col("documents")) > 0))
        )

        result_df_with_document = result_df.filter(size(col("documents")) > 0)
        result_df_without_document = result_df.filter(size(col("documents")) == 0)

        result_df_with_document = (
            result_df_with_document.groupBy(
                [col("names"), col("documents")[0]["serial"]]
            )
            .agg(
                array_distinct(
                    array_compact(flatten(collect_set(col("vehicles"))))
                ).alias("vehicles"),
                array_distinct(
                    array_compact(flatten(collect_set(col("movements"))))
                ).alias("movements"),
                array_distinct(
                    array_compact(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "vehicles",
                "movements",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        result_df_without_document = (
            result_df_without_document.groupBy([col("names"), col("birth_date")])
            .agg(
                array_distinct(
                    array_compact(flatten(collect_set(col("vehicles"))))
                ).alias("vehicles"),
                array_distinct(
                    array_compact(flatten(collect_set(col("movements"))))
                ).alias("movements"),
                array_distinct(
                    array_compact(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "vehicles",
                "movements",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        result_df = result_df_with_document.unionAll(result_df_without_document)

        result_df = (
            result_df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    size(array_compact(col("vehicles"))) > 0,
                    array_compact(col("vehicles")),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                when(
                    size(array_compact(col("movements"))) > 0,
                    array_compact(col("movements")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )

        result_df = result_df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("movements").isNotNull())
        )

        result_df.persist(StorageLevel.DISK_ONLY).count()

        return result_df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
