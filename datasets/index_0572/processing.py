from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
    trim,
    concat,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0572"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0572/raw/universantal.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "doc_type", trim(regexp_extract(col("document"), r"^([^,]+)", 1))
            )
            .withColumn(
                "series", regexp_extract(col("document"), r"серия:\s*([^,]+)", 1)
            )
            .withColumn("number", regexp_extract(col("document"), r"№\s*(\d+)", 1))
            .withColumn(
                "date_issue",
                regexp_extract(col("document"), r"выдан:\s*([0-9\.]+\s*г\.)", 1),
            )
            .withColumn(
                "dept_code",
                regexp_extract(col("document"), r"№\s*подр\.:\s*([\d-]+)", 1),
            )
            .withColumn(
                "issued_by",
                regexp_extract(
                    col("document"), r"выдан:.*?г\.,\s*(.*?)(?:,\s*№\s*подр\.|$)", 1
                ),
            )
            .withColumn(
                "doc_code",
                when(col("doc_type") == "Водительское удостоверение", 3)
                .when(
                    col("doc_type") == "Удостоверение беженца в Российской Федерации", 7
                )
                .when(col("doc_type") == "Военный билет", 6)
                .when(col("doc_type") == "Паспорт гражданина РФ", 0)
                .when(col("doc_type") == "Загранпаспорт гражданина РФ", 4)
                .when(col("doc_type") == "Свидетельство о рождении", 5)
                .when(
                    col("doc_type")
                    == "Временное удостоверение личности гражданина Российской Федерации",
                    9,
                )
                .otherwise(None),
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("snils").isNotNull(),
                            document_udf(
                                lit("снилс"),
                                col("snils"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("%Y-%m-%d"),
                            ),
                        ).otherwise(None),
                        when(
                            col("document").isNotNull(),
                            document_udf(
                                col("doc_type"),
                                concat(col("series"), col("number")),
                                col("date_issue"),
                                col("issued_by"),
                                col("dept_code"),
                                lit(None),
                                lit("%d.%m.%Y"),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .select("names", "birth_date", "sex", "documents", "phones")
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.show(truncate=False, n=20)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
