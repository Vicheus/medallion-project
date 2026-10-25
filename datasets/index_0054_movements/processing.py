import re

from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    udf,
    array_compact,
    size,
    coalesce,
)
from pyspark.sql.functions import StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    ticket_order_datetime_udf,
    get_movement_airport_iata_code_by_slavic_code_udf,
    get_movement_airport_city_by_slavic_code_udf,
)
from parsetron.sections.main.udfs import birth_date_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0054_movements"
    output_file_count: int = 50
    calc_completeness: bool = False

    def parser(self):

        def extract_birth_date(name):
            MONTH_2_NUM = {
                "JAN": "01",
                "FEB": "02",
                "MAR": "03",
                "APR": "04",
                "MAY": "05",
                "JUN": "06",
                "JUL": "07",
                "AUG": "08",
                "SEP": "09",
                "OCT": "10",
                "NOV": "11",
                "DEC": "12",
                "ЯНВ": "01",
                "ФЕВ": "02",
                "МАР": "03",
                "АПР": "04",
                "МАЙ": "05",
                "ИЮН": "06",
                "ИЮЛ": "07",
                "АВГ": "08",
                "СЕН": "09",
                "ОКТ": "10",
                "НОЯ": "11",
                "ДЕК": "12",
            }
            try:
                if not name:
                    return None
                regexp = r"([0-9]{2})([A-ZА-Я]{3})([0-9]{2})"
                match = re.search(regexp, name)
                if not match:
                    return None
                (d, m, y) = match.groups()
                y = int(y)
                if y <= 24:
                    y = 2000 + y
                else:
                    y = 1900 + y
                birth_date = f"{d}.{MONTH_2_NUM.get(m, m)}.{y}"
                return birth_date
            except Exception:
                return None

        extract_birth_date_udf = udf(extract_birth_date, StringType())

        def extract_full_name(name):
            try:
                if not name:
                    return name
                full_name = (
                    name.replace("MS", "")
                    .replace("MRS", "")
                    .replace("MR", "")
                    .replace("Г-ЖА", "")
                    .replace("Г-Н", "")
                )
                regexp = (
                    r"^[\d\s]{0,5}([\-A-ZА-Я]+)\/([A-ZА-Я]+)(\s[A-ZА-Я]{2,50}(\s|$))?"
                )
                match = re.search(regexp, full_name)
                if not match:
                    return full_name
                (ln, fn, sn, *rest) = match.groups()
                return f"{ln.strip().capitalize()} {fn.strip().capitalize()}{' ' + sn.strip().capitalize() if sn else ''}"
            except Exception:
                return name

        extract_full_name_udf = udf(extract_full_name, StringType())

        df_serials_to_ignore = self.read(
            path="/media/user/SAMSUNG/Databases/index_0054/doc_serial_to_ignore.csv",
            sep="\n",
            header=True,
        )
        serials_to_ignore = [
            row["serial"] for row in df_serials_to_ignore.select("serial").collect()
        ]

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0054/raw/*.json",
                sep="\n",
                header=True,
            )
            .withColumn("airline_code", col("_source.airline_code"))
            .withColumn("airline_name", col("_source.airline_name"))
            .withColumn("arrival_point", col("_source.arrival_point"))
            .withColumn("booking_date", col("_source.booking_date"))
            .withColumn("departure_point", col("_source.departure_point"))
            .withColumn("full_name", col("_source.full_name"))
            .withColumn("passport", col("_source.passport"))
            .withColumn("ticket_issuer", col("_source.ticket_issuer"))
            .withColumn(
                "departure_city",
                get_movement_airport_city_by_slavic_code_udf(col("departure_point")),
            )
            .withColumn(
                "departure_code",
                get_movement_airport_iata_code_by_slavic_code_udf(
                    col("departure_point")
                ),
            )
            .withColumn(
                "arrival_city",
                get_movement_airport_city_by_slavic_code_udf(col("arrival_point")),
            )
            .withColumn(
                "arrival_code",
                get_movement_airport_iata_code_by_slavic_code_udf(col("arrival_point")),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(
                    extract_birth_date_udf(col("full_name")), lit("%d.%M.%Y")
                ),
            )
            .withColumn(
                "names", array(name_udf(extract_full_name_udf(col("full_name"))))
            )
        )

        df = (
            df.withColumn(
                "documents",
                array(
                    when(
                        col("passport").isNotNull(),
                        document_udf(
                            lit(None),
                            col("passport"),
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
                    when(
                        (
                            col("departure_city").isNotNull()
                            | col("departure_point").isNotNull()
                        )
                        & (
                            col("arrival_city").isNotNull()
                            | col("arrival_point").isNotNull()
                        ),
                        movement_udf(
                            lit(None),
                            lit(None),
                            col("departure_city"),
                            coalesce(col("departure_code"), col("departure_point")),
                            lit(None),
                            lit(None),
                            col("arrival_city"),
                            coalesce(col("arrival_code"), col("arrival_point")),
                            when(
                                col("arrival_code").isNull()
                                | col("departure_code").isNull(),
                                lit("CODE"),
                            ).otherwise(lit("IATA")),
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
                            col("ticket_issuer"),
                            col("airline_name"),
                            col("airline_code"),
                        ),
                    ).otherwise(None)
                ),
            )
            .select("names", "birth_date", "documents", "movements")
        )

        df = df.withColumn(
            "documents",
            when(
                (
                    col("documents")[0]["serial"].isin(
                        [
                            "123123123",
                            "234234234",
                            "345345345",
                            "456456456",
                            "567567567",
                            "678678678",
                            "789789789",
                            "321321321",
                            "432432432",
                            "543543543",
                            "654654654",
                            "765765765",
                            "876876876",
                            "987987987",
                            "123654789",
                            "012345678",
                            "123456789",
                        ]
                    )
                )
                | (col("documents")[0]["serial"].isin(serials_to_ignore)),
                None,
            ).otherwise(col("documents")),
        )

        df = df.filter(col("names").isNotNull())
        df.cache()

        # print(f"DF size: {df.count()}")
        # print(f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}")
        # print(f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}")

        df = df.repartition(50)

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
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
            & (col("documents").isNotNull() | col("movements").isNotNull())
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
