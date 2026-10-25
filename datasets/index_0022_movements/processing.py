from pyspark import StorageLevel

from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_datetime_udf,
    ticket_order_datetime_udf,
)
from parsetron.sections.main.udfs import birth_date_udf, phone_udf, name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 250
    dataset_code_name: str = "index_0022_movements"
    calc_completeness: bool = False

    def parser(self):
        citizenship_blacklist = [
            "UA",
            "UKR",
            "AZ",
            "AZE",
            "TR",
            "TUR",
            "IL",
            "ISR",
            "IN",
            "IND",
            "DE",
            "DEU",
            "US",
            "USA",
            "TD",
            "EG",
            "EGY",
            "RS",
            "SRB",
            "VN",
            "VNM",
            "FR",
            "FRA",
            "LV",
            "LVA",
            "IT",
            "ITA",
            "LT",
            "LTU",
            "MN",
            "MNG",
            "KR",
            "IQ",
            "NL",
            "NLD",
            "PK",
            "GB",
            "GBR",
            "SA",
            "SAU",
            "PS",
            "PSE",
            "AF",
            "EE",
            "EST",
            "AR",
            "AT",
            "AUT",
            "PL",
            "POL",
            "BR",
            "CA",
            "CAN",
            "GR",
            "GRC",
            "CH",
            "CHE",
            "ES",
            "ESP",
            "NG",
            "NGA",
            "MA",
            "MAR" "CZ",
            "CZE",
            "BG",
            "BGR",
            "TH",
            "THA",
            "JP",
            "JPN",
            "YE",
            "YEM",
            "BE",
            "BEL",
        ]
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0022/raw/sirena-pboarded_raw.json"
        )
        df = df.filter(~col("_source.citizenship").isin(citizenship_blacklist))

        df = (
            df.withColumn("names", array(name_udf(col("_source.full_name"))))
            .withColumn(
                "birth_date",
                birth_date_udf(col("_source.birth_date"), lit("%Y-%m-%dT%H:%M:%S.%fZ")),
            )
            .withColumn("phones", array(phone_udf(col("_source.phone_number"))))
            .withColumn("emails", array(email_udf(col("_source.email"))))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("_source.passport").isNotNull()
                            & (
                                (col("_source.citizenship") == "RU")
                                | (col("_source.citizenship") == "RUS")
                            ),
                            document_udf(
                                lit(None),
                                col("_source.passport"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "movements",
                array_compact(
                    array(
                        movement_udf(
                            movement_datetime_udf(
                                col("_source.departure_date"),
                                lit("%Y-%m-%dT%H:%M:%S.%fZ"),
                            ),
                            lit(None),
                            lit(None),
                            col("_source.departure_point"),
                            lit(None),
                            lit(None),
                            lit(None),
                            col("_source.arrival_point"),
                            lit("IATA"),
                            ticket_order_datetime_udf(
                                col("_source.booking_date"),
                                lit("%Y-%m-%dT%H:%M:%S.%fZ"),
                            ),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(2),
                            lit(None),
                        )
                    )
                ),
            )
        )

        df.cache()

        print(f"DF size: {df.count()}")
        print(
            f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}"
        )
        print(
            f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}"
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
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
                "movements",
                when(
                    size(array_compact(col("movements"))) > 0,
                    array_compact(col("movements")),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("movements").isNotNull()
            )
        )
        df = df.select(
            "names", "birth_date", "emails", "phones", "documents", "movements"
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
