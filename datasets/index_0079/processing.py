from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    coalesce,
    struct,
    split,
    lower,
    array_compact,
    transform,
    regexp_replace,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf, work_date_udf
from parsetron.sections.financials.udfs import (
    extract_invoice_number_for_physical_person_udf,
)
from parsetron.sections.main.udfs import (
    names_udf,
    phones_udf,
    addresses_udf,
    address_udf,
    extract_address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0079"
    output_file_count: int = 10

    def parser(self):
        interpreneur_key_words = ["ип", "индивидуальный предприниматель"]
        interpreneur_pattern = "|".join(interpreneur_key_words)
        inn_pattern = r"(?i)инн[:\s]*\n?\s*(\d+)"
        bank_pattern = r'[«"](.*?)[»"]'

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0079/raw/rossko_preprocessed.csv",
            sep=",",
            header=True,
        ).coalesce(10)

        df = (
            df.withColumn("names", names_udf(array_compact(split("name", "~~"))))
            .withColumn(
                "address",
                addresses_udf(
                    transform(
                        array_compact(split("address", "~~")),
                        lambda x: regexp_replace(x, ";", " "),
                    )
                ),
            )
            .withColumn("phones", phones_udf(array_compact(split("phone", "~~"))))
            .withColumn("work_address", extract_address_udf(array(col("work_info"))))
            .withColumn("work_info", lower(regexp_replace(col("work_info"), "\n", " ")))
            .withColumn(
                "is_interpreneur",
                when(lower(col("work")).rlike(interpreneur_pattern), True).otherwise(
                    False
                ),
            )
            .withColumn(
                "inn",
                when(
                    col("is_interpreneur"),
                    regexp_extract(col("work_info"), inn_pattern, 1),
                ).otherwise(None),
            )
            .withColumn(
                "invoice_number",
                when(
                    col("is_interpreneur"),
                    extract_invoice_number_for_physical_person_udf(col("work_info")),
                ).otherwise(None),
            )
            .withColumn(
                "bank",
                when(
                    col("is_interpreneur"),
                    regexp_extract(col("work_info"), bank_pattern, 1),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("work").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                work_date_udf(col("order_date"), lit("%Y-%m-%d")),
                                lit(None),
                                col("work"),
                                address_udf(
                                    when(
                                        col("work_address").isNotNull(),
                                        col("work_address"),
                                    ).otherwise(None)
                                ),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("inn").isNotNull(),
                    array_compact(
                        array(
                            document_udf(
                                lit("инн"),
                                col("inn"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "financials",
                when(
                    (col("is_interpreneur"))
                    & (col("bank").isNotNull() & col("invoice_number").isNotNull()),
                    array_compact(
                        array(
                            struct(
                                coalesce(col("bank"), lit("Неопределенный банк")).alias(
                                    "title"
                                ),
                                col("invoice_number").alias("invoice_number"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date")),
                lit("%Y-%m-%d %H:%M:%S"),
            )
        )
        df = df.select(
            "names", "phones", "address", "documents", "financials", "actuality"
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("phones").isNotNull())
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY)

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
