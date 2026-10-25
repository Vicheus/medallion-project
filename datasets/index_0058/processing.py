from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    flatten,
    size,
    collect_set,
    concat_ws,
    regexp_extract,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0058"
    output_file_count: int = 10
    calc_completeness: bool = False
    important_columns_for_filtering: str = "phones,documents,emails,address"
    write_filtered_rows: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0058/raw/gemotest.ru_Лаборатория Гемотест(1).csv",
                sep="\t",
                header=True,
            )
            .replace("- - ", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(
                                regexp_replace(
                                    col("last_name first_name middle_name"), " -", ""
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("mobile_phone")), phone_udf(col("home_phone"))
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    " ", col("address_city"), col("address_street")
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ", col("actual_region"), col("actual_address")
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "passport_authority_code",
                regexp_replace(
                    regexp_extract("passport_issued_by", r"(\d{3}-\d{3})", 0), "-", ""
                ),
            )
            .withColumn(
                "passport",
                regexp_extract(
                    "passport_number",
                    r"ПС(\d{10})|PS(\d{10})|ПН(\d{10})|((?:\b)?\d{10}(?:\b)?)",
                    0,
                ),
            )
            .withColumn(
                "birth_certificate",
                regexp_extract(
                    "passport_number",
                    r"СР(\d[А-ЯЁ]{2}\d{6})|СР([IVXLCDM]+[А-ЯЁ]{2}\d{6})|(\d[А-ЯЁ]{2}\d{6})|([IVXLCDM]+[А-ЯЁ]{2}\d{6})",
                    0,
                ),
            )
            .withColumn(
                "ru_foreign_passport",
                regexp_replace(
                    regexp_extract("passport_issued_by", r"(\d{3}-\d{3})", 0), "-", ""
                ),
            )
            .withColumn(
                "passport_authority_code",
                regexp_replace(
                    regexp_extract("passport_issued_by", r"(\d{3}-\d{3})", 0), "-", ""
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (col("passport").isNotNull() & (col("passport") != "")),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("passport_issued_by").alias("authority"),
                                    when(
                                        col("passport_authority_code").isNotNull()
                                        & (col("passport_authority_code") != ""),
                                        col("passport_authority_code"),
                                    )
                                    .otherwise(None)
                                    .alias("authority_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                            when(
                                (
                                    col("birth_certificate").isNotNull()
                                    & (col("birth_certificate") != "")
                                ),
                                document_udf(
                                    lit("свидетельство о рождении"),
                                    col("birth_certificate").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("passport_issued_by").alias("authority"),
                                    when(
                                        col("passport_authority_code").isNotNull()
                                        & (col("passport_authority_code") != ""),
                                        col("passport_authority_code"),
                                    )
                                    .otherwise(None)
                                    .alias("authority_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .select("names", "birth_date", "phones", "emails", "address", "documents")
        )

        df = df.groupBy("names", "birth_date").agg(
            flatten(collect_set("phones")).alias("phones"),
            flatten(collect_set("address")).alias("address"),
            flatten(collect_set("documents")).alias("documents"),
            collect_set("emails").alias("emails"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY)

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
