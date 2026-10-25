from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    collect_set,
    max,
    flatten,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    actuality_date_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0523"
    output_file_count: int = 50
    validate_invalid_groupping: bool = True
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/home/user/Documents/shared/fssp_2025qqq.csv", sep="|", header=True
        ).replace("NULL", None)

        # print(f"""Count without birth_date: {df.filter(col("dr").isNull()).count()}""")
        #
        # print(f"""Count: {df.count()}""")
        # print(
        #    f"""Count without docs: {df.filter(col("pass").isNull() & col("INN").isNull() & col("SNILS").isNull()).count()}"""
        # )
        # print(f"""Count with pass: {df.filter(col("pass").isNotNull()).count()}""")
        # print(
        #    f"""Count without pass with inn: {df.filter(col("pass").isNull() & col("INN").isNotNull()).count()}"""
        # )
        # print(
        #    f"""Count without pass and inn with snils: {df.filter(col("pass").isNull() & col("INN").isNull() & col("SNILS").isNotNull()).count()}"""
        # )

        df = (
            df.withColumn("address", address_udf(col("adres")))
            # .withColumn(
            #    "addresses_with_type",
            #    array_compact(
            #        array_distinct(array(address_with_type_udf(col("address"), lit(1))))
            #    ),
            # )
            # .withColumn(
            #    "addresses",
            #    array_compact(
            #        array_distinct(
            #            normalize_address_batch_udf(col("addresses_with_type"))
            #        )
            #    ),
            # )
        )
        df.cache()

        df = (
            df.withColumn("names", name_udf(col("matched_fio")))
            .withColumn("birth_date", birth_date_udf(col("dr"), lit("%d.%m.%Y")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("SNILS").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("SNILS"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("pass").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("pass"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("INN"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("dataisp"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("dataisp"),
                    col("dataisp"),
                    lit("isp"),
                    col("isp"),
                    lit("nomerisp"),
                    col("nomerisp"),
                    lit("vidisp"),
                    col("vidisp"),
                    lit("dolg"),
                    col("dolg"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "address",
                # "addresses",
                "raw_metadata",
                "documents",
                "actuality",
            )
        )

        df = (
            df.groupby([col("names"), col("birth_date")])
            .agg(
                array_compact(collect_set("address")).alias("address"),
                # array_compact(array_distinct(flatten(collect_set("addresses")))).alias(
                #    "addresses"
                # ),
                array_compact(collect_set("raw_metadata")).alias("raw_metadata"),
                array_compact(array_distinct(flatten(collect_set("documents")))).alias(
                    "documents"
                ),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array_distinct(array_compact(array(col("names")))))
            .select(
                "names",
                "birth_date",
                "address",
                # "addresses",
                "raw_metadata",
                "documents",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df.cache()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            # .withColumn(
            #    "addresses",
            #    when(size(col("addresses")) > 0, col("addresses")).otherwise(None),
            # )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 20)"))
            .withColumn("documents", expr("slice(documents, 1, 20)"))
            .withColumn("address", expr("slice(address, 1, 20)"))
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
