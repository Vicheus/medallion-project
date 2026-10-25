from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    collect_set,
    flatten,
    array_compact,
    regexp_replace,
    concat_ws,
    udf,
    array_distinct,
)
from pyspark.sql.types import StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_date_udf,
    get_movement_airport_code_by_name_udf,
    movement_time_udf,
    movement_datetime_udf,
)
from parsetron.sections.main.udfs import name_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 100
    dataset_code_name: str = "index_0026"

    def parser(self):
        # UDF to convert hhmm to HH:MM:SS
        def format_hhmm_to_hhmmss(time_str):
            if not time_str or len(time_str) != 4 or not time_str.isdigit():
                return None
            try:
                hh = int(time_str[:2])
                mm = int(time_str[2:])
                if not (0 <= hh < 24 and 0 <= mm < 60):
                    return None
                return f"{hh:02d}:{mm:02d}:00"
            except Exception:
                return None

        format_time_udf = udf(format_hhmm_to_hhmmss, StringType())

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0026/raw/сирена-2006.txt",
            sep="|",
            header=True,
            encoding="windows-1251",
        )
        ALLOWED_AIRPORT_COUNTRY_CODES = ["KG", "RU", "BY", "KZ", "AM", "TJ"]
        NAME_PARTS_TO_REPLACE_PATTERN = r" Г-Н| Г-А| Г-ЖА|Г-Н М|/^\s+[0-9]{2}\s+[а-яА-Яa-zA-Z]{3}\s+[0-9]{2}\s+$|\\d+ЛЕТ|\\d+ГОД"

        df = (
            df.withColumn(
                "ФИО Группа, ДР",
                regexp_replace(
                    col("ФИО Группа, ДР"), NAME_PARTS_TO_REPLACE_PATTERN, ""
                ),
            )
            .withColumn("names", name_udf(col("ФИО Группа, ДР")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("Документ").isNotNull()
                        & col("Номер документа").isNotNull(),
                        document_udf(
                            lit(None),
                            concat_ws("", col("Документ"), col("Номер документа")),
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
                "movement_from_date",
                concat_ws(
                    " ",
                    movement_date_udf(col("Дата вылета"), lit("%d.%m.%Y")),
                    movement_time_udf(format_time_udf(col("время вылета"))),
                ),
            )
            .withColumn(
                "movements",
                array(
                    movement_udf(
                        movement_datetime_udf(
                            col("movement_from_date"), lit("%d.%m.%Y %H:%M:%S")
                        ),
                        lit(None),
                        col("аэропорт вылета"),
                        get_movement_airport_code_by_name_udf(
                            col("аэропорт вылета"),
                            lit(None),
                            lit(ALLOWED_AIRPORT_COUNTRY_CODES),
                        ),
                        lit(None),
                        lit(None),
                        col("аэропорт прибытия"),
                        get_movement_airport_code_by_name_udf(
                            col("аэропорт прибытия"),
                            lit(None),
                            lit(ALLOWED_AIRPORT_COUNTRY_CODES),
                        ),
                        lit("IATA"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        col("номер борта"),
                        lit(None),
                        lit(2),
                        lit(None),
                        lit(None),
                        col("авиакомпания"),
                        lit(None),
                    )
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("номер борта"), df["номер борта"])
            )
        )

        df = df.filter(col("names").isNotNull() & (col("names") != ""))
        df = df.cache()

        print(f"DF size: {df.count()}")
        print(
            f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}"
        )
        print(
            f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}"
        )

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
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
            .withColumn("names", array(col("names")))
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .select("names", "documents", "movements", "raw_metadata")
        )

        df_without_doc.show(n=1000, truncate=False)

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("names", "documents", "movements", "raw_metadata")
        )

        df = df_with_doc.unionAll(df_without_doc)

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
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("movements").isNotNull())
        )
        df = df.select("names", "documents", "movements", "raw_metadata")
        df.show(n=10, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
