from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    regexp_replace,
    array,
    split,
    array_distinct,
    array_compact,
    concat,
    size,
    explode,
    min,
    monotonically_increasing_id,
    first,
    collect_list,
    collect_set,
    flatten,
)
from pyspark.sql.window import Window

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import name_udf, phone_udf, phones_udf, address_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0603"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    validate_invalid_groupping: bool = True

    def parser(self):
        mapping = [
            ("Ә", "А"),
            ("ә", "а"),
            ("Ғ", "Г"),
            ("ғ", "г"),
            ("Қ", "К"),
            ("қ", "к"),
            ("Ң", "Н"),
            ("ң", "н"),
            ("Ө", "О"),
            ("ө", "о"),
            ("Ұ", "У"),
            ("ұ", "у"),
            ("Ү", "У"),
            ("ү", "у"),
            ("І", "И"),
            ("і", "и"),
            ("Һ", "Х"),
            ("һ", "х"),
        ]

        df = self.read(
            path="/home/user/Documents/data/index_0603/raw/combined.csv",
            sep=",",
            header=True,
        )

        for kz, ru in mapping:
            df = df.withColumn("fio", regexp_replace(col("fio"), kz, ru))

        df = (
            df.withColumn("names", name_udf(col("fio")))
            .withColumn(
                "phones1",
                phones_udf(
                    split(col("phone1"), ","),
                    lit(self.dataset_country_code),
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        concat(
                            when(col("phones1").isNotNull(), col("phones1")).otherwise(
                                array()
                            ),
                            array(
                                phone_udf(
                                    col("phone2"), lit(self.dataset_country_code)
                                ),
                            ),
                            array(
                                phone_udf(
                                    col("phone3"), lit(self.dataset_country_code)
                                ),
                            ),
                            array(
                                phone_udf(col("phone4"), lit(self.dataset_country_code))
                            ),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("adress")))
            .withColumn(
                "documents",
                when(
                    col("iin").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                document_udf(
                                    lit("инн"),
                                    col("iin"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                    lit(self.dataset_country_code),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "address", "documents")
        )

        df.show(n=20, truncate=False)

        df_with_iin = df.filter(size(col("documents")) > 0)
        df_without_iin = df.filter(
            col("documents").isNull() | (size(col("documents")) == 0)
        )

        df_with_iin_grouped = (
            df_with_iin.groupBy("documents")
            .agg(
                array_compact(collect_set(col("names"))).alias("names"),
                array_compact(flatten(collect_set(col("phones")))).alias("phones"),
                array_compact(collect_set(col("address"))).alias("address"),
            )
            .select("names", "phones", "address", "documents")
        )

        df_no_iin_exploded = df_without_iin.withColumn("phone", explode("phones"))

        w = Window.partitionBy("phone")
        df_no_iin_grouped = (
            (
                df_no_iin_exploded.withColumn(
                    "group_id", min(monotonically_increasing_id()).over(w)
                )
                .groupBy("group_id")
                .agg(
                    array_compact(array(first("names"))).alias("names"),
                    array_compact(
                        array_distinct(flatten(collect_list(col("phones"))))
                    ).alias("phones"),
                    array_compact(array_distinct(collect_list(col("address")))).alias(
                        "address"
                    ),
                )
            )
            .withColumn("documents", array())
            .select("names", "phones", "address", "documents")
        )

        df = df_with_iin_grouped.unionByName(
            df_no_iin_grouped, allowMissingColumns=True
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
