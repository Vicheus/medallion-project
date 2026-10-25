from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    first,
    flatten,
    collect_set,
    concat_ws,
    array_compact,
    array_distinct,
    udf,
    max,
)
from pyspark.sql.types import StringType
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_date_udf,
    movement_time_udf,
    ticket_order_datetime_udf,
    movement_datetime_udf,
    get_movement_airport_city_by_IATA_code_udf,
)
from parsetron.sections.main.udfs import (
    birth_date_udf,
    name_parts_udf,
    sex_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 200
    dataset_code_name: str = "index_0021"
    calc_completeness: bool = False

    def parser(self):

        # UDF to convert yymmdd to proper date
        def parse_yymmdd(date_str):
            if not date_str or len(date_str) != 6:
                return None
            try:
                yy = int(date_str[:2])
                mm = int(date_str[2:4])
                dd = int(date_str[4:6])

                year = 1900 + yy if yy > 25 else 2000 + yy
                date = f"{year}-{mm:02d}-{dd:02d}"  # Zero-padding for mm and dd
                print(date)

                return date
            except Exception:
                return None

        parse_yymmdd_udf = udf(parse_yymmdd, StringType())

        # UDF to convert hhmm to HH:MM:SS
        def format_hhmm_to_hhmmss(time_str):
            if not time_str or len(time_str) != 4 or not time_str.isdigit():
                return None
            try:
                hh = int(time_str[:2])
                mm = int(time_str[2:])
                if not (0 <= hh < 24 and 0 <= mm < 60):
                    return None
                print(f"{hh:02d}:{mm:02d}:00")
                return f"{hh:02d}:{mm:02d}:00"
            except Exception:
                return None

        format_time_udf = udf(format_hhmm_to_hhmmss, StringType())

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0021/raw/sirena_insurance_raw/INSURANCE_INFO_202309121924.csv",
            sep=",",
            header=True,
        )
        df = df.filter(
            (col("PASS_NAME").isNotNull() & col("DOB").isNotNull())
            | (
                col("PASS_NAME").isNotNull()
                & (col("DOCTYPE").isNotNull() & col("DOCNUMBER").isNotNull())
            )
        )

        df = (
            df.withColumn(
                "names", name_parts_udf(col("PASS_NAME"), col("PASS_SURNAME"), lit(""))
            )
            .withColumn("sex", sex_udf(col("GENDER")))
            .withColumn(
                "birth_date",
                birth_date_udf(parse_yymmdd_udf(col("DOB")), lit("%Y-%m-%d")),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("DOCNUMBER").isNotNull() & col("DOCTYPE").isNotNull(),
                        document_udf(
                            lit(None),
                            concat_ws("", col("DOCTYPE"), col("DOCNUMBER")),
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
                "movement_time",
                concat_ws(
                    " ",
                    movement_date_udf(
                        parse_yymmdd_udf(col("DEP_DATE")), lit("%Y-%m-%d")
                    ),
                    movement_time_udf(format_time_udf(col("DEP_TIME"))),
                ),
            )
            .withColumn(
                "movements",
                array(
                    movement_udf(
                        movement_datetime_udf(col("movement_time")),
                        lit(None),
                        get_movement_airport_city_by_IATA_code_udf(col("CITY_FROM")),
                        col("PORT_FROM"),
                        lit(None),
                        lit(None),
                        get_movement_airport_city_by_IATA_code_udf(col("CITY_TO")),
                        col("PORT_TO"),
                        lit("IATA"),
                        ticket_order_datetime_udf(col("TKT_DATE")),
                        lit(None),
                        lit(None),
                        col("TICKET_NUM"),
                        col("FLIGHT"),
                        lit(None),
                        lit(2),
                        lit(None),
                        col("AGENCY"),
                        col("TICKET_AIRLINE"),
                        lit(None),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("TKT_DATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("PPR"),
                    df["PPR"],
                    lit("PUL"),
                    df["PUL"],
                    lit("REGNUM"),
                    df["REGNUM"],
                    lit("SCODE"),
                    df["SCODE"],
                    lit("SER"),
                    df["SER"],
                    lit("STATE_FROM"),
                    df["STATE_FROM"],
                    lit("STATE_TO"),
                    df["STATE_TO"],
                    lit("STYPE"),
                    df["STYPE"],
                    lit("TICKET_SER"),
                    df["TICKET_SER"],
                    lit("TLINE"),
                    df["TLINE"],
                ),
            )
        )
        df.cache()
        df.show()

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .groupby(["names", "birth_date"])
            .agg(
                first("sex").alias("sex"),
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
                max("actuality").alias("actuality"),
                array_compact(array_distinct((collect_set(col("raw_metadata"))))).alias(
                    "raw_metadata"
                ),
            )
            .withColumn("names", array(col("names")))
            .select(
                "names",
                "documents",
                "emails",
                "movements",
                "birth_date",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                first("sex").alias("sex"),
                first("birth_date").alias("birth_date"),
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
                max("actuality").alias("actuality"),
                array_compact(array_distinct((collect_set(col("raw_metadata"))))).alias(
                    "raw_metadata"
                ),
            )
            .select(
                "names",
                "documents",
                "emails",
                "movements",
                "birth_date",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_distinct(array_compact(col("names")))) > 0,
                    array_distinct(array_compact(col("names"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_distinct(array_compact(col("emails")))) > 0,
                    array_distinct(array_compact(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_distinct(array_compact(col("documents")))) > 0,
                    array_distinct(array_compact(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                when(
                    size(array_distinct(array_compact(col("movements")))) > 0,
                    array_distinct(array_compact(col("movements"))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_distinct(array_compact(col("raw_metadata")))) > 0,
                    array_distinct(array_compact(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("movements").isNotNull()
            )
        )
        df = df.select(
            "names",
            "sex",
            "birth_date",
            "emails",
            "documents",
            "movements",
            "actuality",
            "raw_metadata",
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
