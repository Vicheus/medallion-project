from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
    first,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0113"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "documents,emails,phones,address"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0113/raw/covid19_move.csv",
            sep="|",
            encoding="windows-1251",
            header=True,
        )

        passport_number_pattern = r"(\d{4}\s?\d{6})"
        passport_issuer_pattern = r"\d{4}\s?\d{6} (.+?) \d{2}-\d{2}-\d{4}"
        passport_issue_date_pattern = r"(\d{2}-\d{2}-\d{4})"

        df = (
            df.withColumn("names", name_udf(col("fio")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("out/in")))
            .withColumn(
                "passport_number",
                regexp_extract(col("passport"), passport_number_pattern, 1),
            )
            .withColumn(
                "passport_issuer",
                regexp_extract(col("passport"), passport_issuer_pattern, 1),
            )
            .withColumn(
                "passport_issue_date",
                regexp_extract(col("passport"), passport_issue_date_pattern, 1),
            )
            .withColumn(
                "documents",
                when(
                    col("passport_number").isNotNull(),
                    array(
                        document_udf(
                            lit(None),
                            col("passport_number"),
                            col("passport_issue_date"),
                            lit(None),
                            col("passport_issuer"),
                            lit(None),
                            lit("%Y-%m-%d"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("job").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("job"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "address", "documents", "works")
        )

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .groupby(["names", "phones"])
            .agg(
                collect_set("emails").alias("emails"),
                collect_set("address").alias("address"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("works"))).alias("works"),
            )
            .withColumn("phones", array(col("phones")))
            .select("names", "phones", "emails", "address", "documents", "works")
        )

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"], col("documents")[0]["type"])
            .agg(
                first("names").alias("names"),
                collect_set("emails").alias("emails"),
                collect_set("phones").alias("phones"),
                collect_set("address").alias("address"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("works"))).alias("works"),
            )
            .select("names", "phones", "emails", "address", "documents", "works")
        )

        df = df_without_doc.unionAll(df_with_doc)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.select("names", "phones", "emails", "address", "documents", "works")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
