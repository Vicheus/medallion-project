from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_date_udf,
    get_movement_airport_code_by_name_udf,
)
from parsetron.sections.main.udfs import name_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 100
    dataset_code_name: str = "index_0025_movements"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0025/raw/Sirena 2019.txt",
            sep="\t",
            header=True,
        )
        df = df.filter(
            (col("FullName").isNotNull() & col("BDay").isNotNull())
            | (col("FullName").isNotNull() & col("Passport").isNotNull())
        )
        AIRPORT_NAME_STOPWORDS = [
            "Кыргызстан",
            "Россия",
            "Беларусь",
            "Казахстан",
            "Армения",
        ]
        ALLOWED_AIRPORT_COUNTRY_CODES = ["KG", "RU", "BY", "KZ", "AM", "TJ"]

        df = (
            df.withColumn(
                "names", array(name_udf(regexp_replace(col("FullName"), "\\d", "")))
            )
            .withColumn("birth_date", birth_date_udf(col("BDay"), lit("%d.%m.%Y")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("Passport").isNotNull(),
                        document_udf(
                            lit("паспорт гражданина рф"),
                            col("Passport"),
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
                        movement_date_udf(col("FlightDate"), lit("%d.%m.%Y")),
                        lit(None),
                        col("PlaceDeparture"),
                        get_movement_airport_code_by_name_udf(
                            col("PlaceDeparture"),
                            lit(AIRPORT_NAME_STOPWORDS),
                            lit(ALLOWED_AIRPORT_COUNTRY_CODES),
                        ),
                        lit(None),
                        lit(None),
                        col("Destination"),
                        get_movement_airport_code_by_name_udf(
                            col("Destination"),
                            lit(AIRPORT_NAME_STOPWORDS),
                            lit(ALLOWED_AIRPORT_COUNTRY_CODES),
                        ),
                        lit("IATA"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        col("FlightNumber"),
                        lit(None),
                        lit(2),
                        lit(None),
                        lit(None),
                        col("Airline"),
                        lit(None),
                    )
                ),
            )
            .select("names", "birth_date", "documents", "movements")
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
        df = df.select("names", "birth_date", "documents", "movements")

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
