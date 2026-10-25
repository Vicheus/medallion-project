from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array_distinct,
    array_compact,
    array,
    lit,
    array_size,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0512"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/nbki.ru_2024_500k_sample./nbki.ru_2024_500k_sample.csv",
            sep=";",
        )

        df = (
            (
                df.withColumn("names", name_udf(col("name")))
                .withColumn(
                    "birth_date", birth_date_udf(col("birthdate"), lit("%d.%m.%Y"))
                )
                .withColumn("phones", phone_udf(col("phone")))
                .withColumn("address", address_udf(col("address")))
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array(address_with_type_udf(col("address"), lit(1)))
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    col("passport_date"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .select(
                "names", "phones", "birth_date", "address", "addresses", "documents"
            )
        )

        df = (
            df.groupby("birth_date", "names")
            .agg(
                collect_set("phones").alias("phones"),
                collect_set("address").alias("address"),
                flatten(collect_set("addresses")).alias("addresses"),
                flatten(collect_set("documents")).alias("documents"),
            )
            .select(
                "names", "birth_date", "phones", "address", "addresses", "documents"
            )
        )

        df.cache()

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(array_size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "address",
                when(array_size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(array_size(col("documents")) > 0, col("documents")).otherwise(
                    None
                ),
            )
            .withColumn(
                "addresses",
                when(array_size(col("addresses")) > 0, col("addresses")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
