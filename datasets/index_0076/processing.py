from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    concat_ws,
    array_distinct,
    regexp_replace,
    flatten,
    collect_set,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0076"
    output_file_count: int = 200
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "address,emails,documents,phones"

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("unknown_1", StringType(), True),
                StructField("unknown_2", StringType(), True),
                StructField("unknown_3", StringType(), True),
                StructField("unknown_4", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("doc_type", StringType(), True),
                StructField("doc_series", StringType(), True),
                StructField("doc_number", StringType(), True),
                StructField("doc_date_issue", StringType(), True),
                StructField("doc_issued_by_code", StringType(), True),
                StructField("doc_issued_by", StringType(), True),
                StructField("unknown_6", StringType(), True),
                StructField("unknown_7", StringType(), True),
                StructField("unknown_8", StringType(), True),
                StructField("unknown_9", StringType(), True),
                StructField("snils", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("address", StringType(), True),
                StructField("unknown_10", StringType(), True),
                StructField("unknown_11", StringType(), True),
                StructField("unknown_12", StringType(), True),
                StructField("unknown_13", StringType(), True),
                StructField("unknown_14", StringType(), True),
                StructField("unknown_15", StringType(), True),
                StructField("unknown_16", StringType(), True),
                StructField("unknown_17", StringType(), True),
                StructField("unknown_18", StringType(), True),
                StructField("unknown_19", StringType(), True),
                StructField("unknown_20", StringType(), True),
                StructField("unknown_21", StringType(), True),
                StructField("unknown_22", StringType(), True),
                StructField("unknown_23", StringType(), True),
                StructField("unknown_24", StringType(), True),
                StructField("email", StringType(), True),
                StructField("phone_number", StringType(), True),
                StructField("unknown_25", StringType(), True),
                StructField("address_2", StringType(), True),
                StructField("address_3", StringType(), True),
                StructField("unknown_26", StringType(), True),
                StructField("unknown_27", StringType(), True),
                StructField("unknown_28", StringType(), True),
                StructField("unknown_29", StringType(), True),
                StructField("unknown_30", StringType(), True),
                StructField("unknown_31", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0076/raw/preprocessed/rosreestr_preprocessed.csv",
            sep="\t",
            header=False,
            schema=schema,
        ).replace("\\N", None)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address")),
                            address_udf(col("address_2")),
                            address_udf(col("address_3")),
                        )
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    (col("doc_series").isNotNull() & col("doc_number").isNotNull())
                    | col("snils").isNotNull(),
                    array_compact(
                        array(
                            when(
                                (
                                    col("doc_series").isNotNull()
                                    & col("doc_number").isNotNull()
                                ),
                                document_udf(
                                    lit(None),
                                    regexp_replace(
                                        concat_ws(
                                            "", col("doc_series"), col("doc_number")
                                        ),
                                        " ",
                                        "",
                                    ),
                                    col("doc_date_issue"),
                                    lit(None),
                                    col("doc_issued_by"),
                                    regexp_replace(
                                        col("doc_issued_by_code"), r"[^0-9]", ""
                                    ),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
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
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "emails", "address", "birth_date", "documents")
        )

        df.cache()

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .groupby(["names", "birth_date"])
            .agg(
                array_compact(collect_set("emails")).alias("emails"),
                array_compact((collect_set("phones"))).alias("phones"),
                array_compact(flatten(collect_set("address"))).alias("address"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
            )
            .withColumn("names", array(col("names")))
            .select("names", "phones", "emails", "address", "birth_date", "documents")
        )

        df_without_doc.cache()
        df_without_doc.show(n=10, truncate=False)

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(
                col("documents")[0]["serial"],
                col("documents")[0]["type"],
                "names",
                "birth_date",
            )
            .agg(
                array_compact(collect_set("emails")).alias("emails"),
                array_compact((collect_set("phones"))).alias("phones"),
                array_compact(flatten(collect_set("address"))).alias("address"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
            )
            .withColumn("names", array(col("names")))
            .select("names", "phones", "emails", "address", "birth_date", "documents")
        )

        df_with_doc.cache()
        df_with_doc.show(n=10, truncate=False)

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
                "phones",
                when(
                    size(array_distinct(array_compact(col("phones")))) > 0,
                    array_distinct(array_compact(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_distinct(array_compact(col("address")))) > 0,
                    array_distinct(array_compact(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_distinct(array_compact(col("documents")))) > 0,
                    array_distinct(array_compact(col("documents"))),
                ).otherwise(None),
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.drop_duplicates()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
