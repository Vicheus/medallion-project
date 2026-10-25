from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat_ws,
    size,
    array_compact,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    get_movement_airport_iata_code_by_slavic_code_udf,
    movement_datetime_udf,
    get_movement_airport_city_by_slavic_code_udf,
    ticket_order_datetime_udf,
)
from parsetron.sections.main.udfs import name_udf, birth_date_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 100
    dataset_code_name: str = "index_0024_movements"

    def parser(self):
        schema = StructType(
            [
                StructField("full_name", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("document_type", StringType(), True),
                StructField("document_number", StringType(), True),
                StructField("flight_company", StringType(), True),
                StructField("flight_number", StringType(), True),
                StructField("flight_date", StringType(), True),
                StructField("flight_time", StringType(), True),
                StructField("airport_from", StringType(), True),
                StructField("airport_to", StringType(), True),
                StructField("operation_date", StringType(), True),
                StructField("operation", StringType(), True),
                StructField("all_boarded", StringType(), True),
                StructField("passenger_with", StringType(), True),
                StructField("flight_signature", StringType(), True),
                StructField("operator_code", StringType(), True),
            ]
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0024/raw/Sirena-travel_2014-2016_60M.txt",
            sep="|",
            header=False,
            schema=schema,
            encoding="windows-1251",
        )
        df = df.filter(
            (col("full_name").isNotNull() & col("birth_date").isNotNull())
            | (
                col("full_name").isNotNull()
                & (
                    col("document_type").isNotNull()
                    & col("document_number").isNotNull()
                )
            )
        )

        df = (
            df.withColumn("names", array(name_udf(col("full_name"))))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "documents",
                array(
                    when(
                        col("document_type").isNotNull()
                        & col("document_number").isNotNull(),
                        document_udf(
                            lit(None),
                            concat_ws("", col("document_type"), col("document_number")),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "movements",
                array(
                    movement_udf(
                        movement_datetime_udf(
                            concat_ws(" ", col("flight_date"), col("flight_time")),
                            lit("%d.%m.%Y %H:%M"),
                        ),
                        lit("RUS"),
                        get_movement_airport_city_by_slavic_code_udf(
                            col("airport_from")
                        ),
                        get_movement_airport_iata_code_by_slavic_code_udf(
                            col("airport_from")
                        ),
                        lit(None),
                        lit("RUS"),
                        get_movement_airport_city_by_slavic_code_udf(col("airport_to")),
                        get_movement_airport_iata_code_by_slavic_code_udf(
                            col("airport_to")
                        ),
                        lit("IATA"),
                        ticket_order_datetime_udf(
                            col("operation_date"), lit("%d.%m.%Y")
                        ),
                        lit(None),
                        lit(None),
                        lit(None),
                        col("flight_number"),
                        lit(None),
                        lit(2),
                        lit(None),
                        lit(None),
                        col("flight_company"),
                        lit(None),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("flight_signature"),
                    df["flight_signature"],
                    lit("operator_code"),
                    df["operator_code"],
                ),
            )
            .select("names", "birth_date", "documents", "movements", "raw_metadata")
        )

        print(f"DF size: {df.count()}")
        print(
            f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}"
        )
        print(
            f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}"
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
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
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("movements").isNotNull())
        )
        df = df.select("names", "birth_date", "documents", "movements", "raw_metadata")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
