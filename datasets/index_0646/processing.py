from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    concat_ws,
    collect_set,
    array_compact,
    max,
    first,
    size,
    array_distinct,
)
from pyspark.sql.types import StructType, StructField, StringType


from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0646"
    validate_invalid_groupping: bool = True
    output_file_count: int = 50

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("transfer_date", StringType(), True),
                StructField("transfer_sum", StringType(), True),
                StructField("unknown_col_1", StringType(), True),
                StructField("sender_first_name", StringType(), True),
                StructField("sender_middle_name", StringType(), True),
                StructField("sender_last_name", StringType(), True),
                StructField("sender_document_series", StringType(), True),
                StructField("sender_document_number", StringType(), True),
                StructField("sender_document_issued_by", StringType(), True),
                StructField("sender_document_issued_at", StringType(), True),
                StructField("sender_birth_date", StringType(), True),
                StructField("sender_address", StringType(), True),
                StructField("sender_phone", StringType(), True),
                StructField("receiver_first_name", StringType(), True),
                StructField("receiver_middle_name", StringType(), True),
                StructField("receiver_last_name", StringType(), True),
                StructField("receiver_document_series", StringType(), True),
                StructField("receiver_document_number", StringType(), True),
                StructField("receiver_document_issued_by", StringType(), True),
                StructField("receiver_document_issued_at", StringType(), True),
                StructField("receiver_birth_date", StringType(), True),
                StructField("receiver_address", StringType(), True),
                StructField("receiver_phone", StringType(), True),
            ]
        )

        df = self.read(
            path="/media/user/T7/unistream/u_*.txt",
            sep="\t",
            header=False,
            schema=schema,
        )

        df_senders_with_ru_phones = df.withColumn(
            "phones", phone_udf(col("sender_phone"))
        ).filter(col("phones").isNotNull())

        df_receivers_with_ru_phones = df.withColumn(
            "phones", phone_udf(col("receiver_phone"))
        ).filter(col("phones").isNotNull())

        df_senders = (
            df_senders_with_ru_phones.withColumn(
                "names",
                name_parts_udf(
                    col("sender_first_name"),
                    col("sender_last_name"),
                    col("sender_middle_name"),
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("sender_birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("sender_phone")))
            .withColumn("address", address_udf(col("sender_address")))
            .withColumn(
                "receiver_fullname",
                name_parts_udf(
                    col("receiver_first_name"),
                    col("receiver_last_name"),
                    col("receiver_middle_name"),
                ),
            )
            .withColumn(
                "receiver_birth_date",
                birth_date_udf(col("receiver_birth_date"), lit("%Y-%m-%d")),
            )
            .withColumn("receiver_phone", phone_udf(col("receiver_phone")))
            .withColumn(
                "documents",
                when(
                    (
                        col("sender_document_series").isNotNull()
                        & col("sender_document_number").isNotNull()
                    ),
                    document_udf(
                        lit(None),
                        concat_ws(
                            "",
                            col("sender_document_series"),
                            col("sender_document_number"),
                        ),
                        col("sender_document_issued_at"),
                        lit(None),
                        col("sender_document_issued_by"),
                        lit(None),
                        lit("%Y-%m-%d"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    (
                        col("receiver_fullname").isNotNull()
                        & col("receiver_birth_date").isNotNull()
                    ),
                    concat_ws(
                        " ",
                        col("receiver_fullname"),
                        col("receiver_birth_date"),
                        col("receiver_phone"),
                        lit("Получатель денежного перевода Unistream"),
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("transfer_date"), lit("%Y-%m-%d"))
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "address",
                "documents",
                "relations",
                "actuality",
            )
        )

        df_receivers = (
            df_receivers_with_ru_phones.withColumn(
                "names",
                name_parts_udf(
                    col("receiver_first_name"),
                    col("receiver_last_name"),
                    col("receiver_middle_name"),
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("receiver_birth_date"), lit("%Y-%m-%d")),
            )
            .withColumn("phones", phone_udf(col("receiver_phone")))
            .withColumn("address", address_udf(col("receiver_address")))
            .withColumn(
                "sender_fullname",
                name_parts_udf(
                    col("sender_first_name"),
                    col("sender_last_name"),
                    col("sender_middle_name"),
                ),
            )
            .withColumn(
                "sender_birth_date",
                birth_date_udf(col("sender_birth_date"), lit("%Y-%m-%d")),
            )
            .withColumn("sender_phone", phone_udf(col("sender_phone")))
            .withColumn(
                "documents",
                when(
                    (
                        col("receiver_document_series").isNotNull()
                        & col("receiver_document_number").isNotNull()
                    ),
                    document_udf(
                        lit(None),
                        concat_ws(
                            "",
                            col("receiver_document_series"),
                            col("receiver_document_number"),
                        ),
                        col("receiver_document_issued_at"),
                        lit(None),
                        col("receiver_document_issued_by"),
                        lit(None),
                        lit("%Y-%m-%d"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    (
                        col("sender_fullname").isNotNull()
                        & col("sender_birth_date").isNotNull()
                    ),
                    concat_ws(
                        " ",
                        col("sender_fullname"),
                        col("sender_birth_date"),
                        col("sender_phone"),
                        lit("Отправитель денежного перевода Unistream"),
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("transfer_date"), lit("%Y-%m-%d"))
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "address",
                "documents",
                "relations",
                "actuality",
            )
        )

        df = df_senders.unionAll(df_receivers)

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(collect_set(col("documents"))).alias("documents"),
                array_compact(collect_set(col("relations"))).alias("relations"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "address",
                "documents",
                "relations",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
            .withColumn(
                "relations",
                when(
                    size(array_distinct(array_compact(col("relations")))) > 0,
                    array_distinct(array_compact(col("relations"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
