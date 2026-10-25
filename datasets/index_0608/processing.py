from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    collect_set,
    regexp_extract,
    trim,
    split,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, raw_metadata_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_datetime_udf,
    get_movement_airport_code_by_name_udf,
)
from parsetron.sections.device.udfs import device_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0608"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    AIRPORT_NAME_STOPWORDS = []
    ALLOWED_AIRPORT_COUNTRY_CODES = ["KG", "RU", "BY", "KZ", "AM", "TJ", "UA"]

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0608/raw/clickavia_tickets.csv",
                sep="|",
                header=True,
            )
            .withColumn(
                "name",
                trim(regexp_extract(col("Ticket_data"), r"^(.*?)\s*Документ:", 1)),
            )
            .withColumn(
                "doc_num_masked",
                regexp_extract(
                    col("Ticket_data"), r"Документ:\s*([\d]{4}\s*\d\*+\d)", 1
                ),
            )
            .withColumn("age_num", regexp_extract(col("age"), r"(\d+)", 1))
            .withColumn("route_parts", split(col("Flight_details"), " — "))
            .withColumn("from_part", trim(col("route_parts")[0]))
            .withColumn("to_part", trim(col("route_parts")[1]))
            .withColumn("from_tokens", split(col("from_part"), " "))
            .withColumn("to_tokens", split(col("to_part"), " "))
            .withColumn(
                "airport_from",
                when(size(col("from_tokens")) == 3, col("from_tokens")[0]),
            )
            .withColumn(
                "airport_from_code",
                get_movement_airport_code_by_name_udf(
                    col("airport_from"),
                    lit(self.AIRPORT_NAME_STOPWORDS),
                    lit(self.ALLOWED_AIRPORT_COUNTRY_CODES),
                ),
            )
            .withColumn(
                "city_from",
                when(size(col("from_tokens")) == 3, col("from_tokens")[1]).when(
                    size(col("from_tokens")) == 2, col("from_tokens")[0]
                ),
            )
            .withColumn(
                "country_from",
                when(size(col("from_tokens")) == 3, col("from_tokens")[2]).when(
                    size(col("from_tokens")) == 2, col("from_tokens")[1]
                ),
            )
            .withColumn(
                "airport_to", when(size(col("to_tokens")) == 3, col("to_tokens")[0])
            )
            .withColumn(
                "airport_to_code",
                get_movement_airport_code_by_name_udf(
                    col("airport_to"),
                    lit(self.AIRPORT_NAME_STOPWORDS),
                    lit(self.ALLOWED_AIRPORT_COUNTRY_CODES),
                ),
            )
            .withColumn(
                "city_to",
                when(size(col("to_tokens")) == 3, col("to_tokens")[1]).when(
                    size(col("to_tokens")) == 2, col("to_tokens")[0]
                ),
            )
            .withColumn(
                "country_to",
                when(size(col("to_tokens")) == 3, col("to_tokens")[2]).when(
                    size(col("to_tokens")) == 2, col("to_tokens")[1]
                ),
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "movements",
                movement_udf(
                    movement_datetime_udf(
                        col("Flight_date"),
                        lit("%d.%m.%Y"),
                    ),
                    col("country_from"),
                    col("city_from"),
                    when(
                        col("airport_from_code").isNotNull(), col("airport_from_code")
                    ).otherwise(col("airport_from")),
                    lit(None),
                    col("country_to"),
                    col("city_to"),
                    when(
                        col("airport_to_code").isNotNull(), col("airport_to_code")
                    ).otherwise(col("airport_to")),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    col("Flight_number"),
                    col("Booking_class"),
                    lit(2),
                    lit(None),
                    lit(None),
                    col("Selected_airline"),
                    lit(None),
                ),
            )
            .withColumn(
                "devices",
                when(
                    ~col("User_agent").rlike(r"^\d+(\.\d+){0,3}$"),
                    device_udf(
                        lit(None),
                        col("User_agent"),
                        lit(None),
                        lit("Покупка авиабилета"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("age_num").isNotNull() | col("doc_num_masked").isNotNull(),
                    raw_metadata_udf(
                        lit("age"),
                        col("age_num"),
                        lit("document_masked"),
                        col("doc_num_masked"),
                    ),
                ),
            )
            .select(
                "names",
                "emails",
                "movements",
                "devices",
                "raw_metadata",
                "doc_num_masked",
            )
        )

        df = (
            df.groupBy(["names", "doc_num_masked"])
            .agg(
                array_compact(array_distinct(collect_set(col("movements")))).alias(
                    "movements"
                ),
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("devices")))).alias(
                    "devices"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("names", "emails", "movements", "devices", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "movements",
                when(size(col("movements")) > 0, col("movements")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("movements").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
