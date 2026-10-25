from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    concat,
    struct,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.financials.udfs import (
    financial_card_number_udf,
    yandex_money_number_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 50
    dataset_code_name: str = "index_0109"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0109/raw/vodila-428658.json",
            sep="\n",
            header=False,
        )

        df = (
            df.withColumn("bank", col("_source.bank"))
            .withColumn("bankcard", col("_source.bankcard"))
            .withColumn("bankip", col("_source.bankip"))
            .withColumn("city", col("_source.city"))
            .withColumn("email", col("_source.email"))
            .withColumn("fam", col("_source.fam"))
            .withColumn("inn", col("_source.inn").cast("string"))
            .withColumn("kpp", col("_source.kpp").cast("string"))
            .withColumn("ogrn", col("_source.ogrn").cast("string"))
            .withColumn("name", col("_source.name"))
            .withColumn("nomer", col("_source.nomer").cast("string"))
            .withColumn("nomerp", col("_source.nomerp").cast("string"))
            .withColumn("numqiwi", col("_source.numqiwi"))
            .withColumn("numyandexk", col("_source.numyandexk"))
            .withColumn("phone", col("_source.phone"))
            .withColumn("datevidachi", col("_source.datevidachi"))
            .withColumn("kemvidan", col("_source.kemvidan"))
            .withColumn("seria", col("_source.seria").cast("string"))
            .withColumn("seriap", col("_source.seriap").cast("string"))
            .withColumn("dateb", col("_source.dateb"))
            .withColumn("otch", col("_source.otch"))
            .withColumn("datereg", col("_source.datereg"))
            .withColumn("lasltimeinn", col("_source.lasltimeinn"))
            .withColumn("last_transaction_date", col("_source.last_transaction_date"))
            .withColumn("imei", col("_source.imei"))
            .withColumn("yandex", col("_source.yandex"))
            .withColumn("uber", col("_source.uber"))
            .withColumn("pozivnoi", col("_source.pozivnoi"))
            .drop("_id", "_index", "_score", "_source", "_type", "sort")
        )

        df = (
            df.withColumn("names", name_parts_udf(col("name"), col("fam"), col("otch")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("birth_date", birth_date_udf(col("dateb"), lit("yyyy-MM-dd")))
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "yandex_money_number", yandex_money_number_udf(col("numyandexk"))
            )
            .withColumn("card_number", financial_card_number_udf(col("bankcard")))
            .withColumn(
                "documents",
                when(
                    (col("seria").isNotNull() | col("nomer").isNotNull())
                    | (col("seriap").isNotNull() | col("nomerp").isNotNull())
                    | (col("inn").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("seriap").isNotNull() | col("nomerp").isNotNull()),
                                document_udf(
                                    lit(None),
                                    concat(col("seriap"), col("nomerp")),
                                    col("datevidachi"),
                                    lit(None),
                                    col("kemvidan"),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("seria").isNotNull() | col("nomer").isNotNull()),
                                document_udf(
                                    lit(None),
                                    concat(col("seria"), col("nomer")),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("kpp").isNotNull()),
                                document_udf(
                                    lit("кпп"),
                                    col("kpp"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("ogrn").isNotNull()),
                                document_udf(
                                    lit("огрн"),
                                    col("ogrn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("inn").isNotNull()),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull()
                    | col("yandex_money_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("card_number").isNotNull(),
                                struct(
                                    coalesce(
                                        col("bank"),
                                        col("bankip"),
                                        lit("Неопределенный банк"),
                                    ).alias("title"),
                                    col("card_number").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("yandex_money_number").isNotNull(),
                                struct(
                                    lit("Яндекс деньги").alias("title"),
                                    col("yandex_money_number").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("numqiwi").isNotNull() & (col("numqiwi") != ""),
                                struct(
                                    lit("QIWI").alias("title"),
                                    col("numqiwi").alias("card_number"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(
                        col("datereg"), col("lasltimeinn"), col("last_transaction_date")
                    ),
                    lit("%Y-%m-%dT%H:%M:%S.%fZ"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("imei"),
                    col("imei"),
                    lit("yandex"),
                    col("yandex"),
                    lit("uber"),
                    col("uber"),
                    lit("pozivnoi"),
                    col("pozivnoi"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "financials",
                "birth_date",
                "actuality",
                "raw_metadata",
            )
        )

        df = (
            df.withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )
        df = df.select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "address",
            "documents",
            "financials",
            "actuality",
            "raw_metadata",
        )

        df.show(n=100, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
