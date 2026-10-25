from pyspark.sql.functions import (
    when,
    col,
    first,
    lit,
    array,
    trim,
    max,
    array_distinct,
    array_compact,
    concat,
    concat_ws,
    regexp_extract,
    struct,
    size,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0150"

    def parser(self):
        df_payments = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0150/raw/cross_t/cross-t.ru/cross-t-txt-docs/ftp/payment/*.txt",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("ID", col("ABONENT_ID"))
            .withColumn("phone_payment", phone_udf(col("PHONE_NUMBER")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("PAYMENT_DATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("ID", "phone_payment", "actuality")
        )
        df_payments.cache()

        df_abonent = self.read(
            path="/media/user/SAMSUNG/Databases/index_0150/raw/cross_t/cross-t.ru/cross-t-txt-docs/ftp/abonents/*.txt",
            sep=";",
            header=True,
        ).replace("NULL", None)
        df_abonent.cache()

        df_abonent = (
            df_abonent.join(df_payments, "ID", "left")
            .withColumn("abonent_id", col("ID"))
            .withColumn(
                "names",
                name_parts_udf(
                    col("GIVEN_NAME"), col("FAMILY_NAME"), col("INITIAL_NAME")
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("BIRTH_DATE"), lit("%Y-%M-%d"))
            )
            .withColumn("phones", col("phone_payment"))
            .withColumn(
                "doc_type",
                when(col("IDENT_CARD_TYPE_ID") == 1, "паспорт гражданина рф")
                .when(
                    col("IDENT_CARD_TYPE_ID") == 6, "заграничный паспорт гражданина рф"
                )
                .when(
                    col("IDENT_CARD_TYPE_ID") == 8,
                    "Временное удостоверение личн. гражд. РФ",
                )
                .when(
                    col("IDENT_CARD_TYPE_ID") == 4,
                    "удостоверение личности военнослужащего",
                )
                .otherwise(None),
            )
            .withColumn(
                "doc_date",
                regexp_extract(
                    col("IDENT_CARD_DESCRIPTION"), r"(\d{4}-\d{2}-\d{2})", 1
                ),
            )
            .withColumn(
                "doc_issued_by",
                regexp_extract(
                    col("IDENT_CARD_DESCRIPTION"), r"(\d{4}-\d{2}-\d{2})(.*)", 2
                ),
            )
            .withColumn(
                "documents",
                when(
                    (
                        col("IDENT_CARD_SERIAL").isNotNull()
                        & col("IDENT_CARD_NUMBER").isNotNull()
                    )
                    | col("INN").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("IDENT_CARD_SERIAL").isNotNull()
                                    & col("IDENT_CARD_NUMBER").isNotNull(),
                                    document_udf(
                                        col("doc_type"),
                                        concat(
                                            col("IDENT_CARD_SERIAL"),
                                            col("IDENT_CARD_NUMBER"),
                                        ),
                                        col("doc_date"),
                                        lit(None),
                                        trim(col("doc_issued_by")),
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
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    col("BANK_ACCOUNT").isNotNull() & col("BANK").isNotNull(),
                    array(
                        struct(
                            col("BANK_ACCOUNT").alias("title"),
                            col("BANK_ACCOUNT").alias("invoice_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "abonent_id",
                "names",
                "phones",
                "birth_date",
                "documents",
                "financials",
                "actuality",
            )
        )

        df_abonent_addr = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0150/raw/cross_t/cross-t.ru/cross-t-txt-docs/ftp/abonent_address/*.txt",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("abonent_id", col("ABONENT_ID"))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    ", ",
                                    when(col("ZIP") != "", col("ZIP")).otherwise(None),
                                    when(
                                        col("COUNTRY") != "", col("COUNTRY")
                                    ).otherwise(None),
                                    when(col("REGION") != "", col("REGION")).otherwise(
                                        None
                                    ),
                                    when(col("ZONE") != "", col("ZONE")).otherwise(
                                        None
                                    ),
                                    when(col("CITY") != "", col("CITY")).otherwise(
                                        None
                                    ),
                                    when(
                                        col("STREET") != "",
                                        concat(lit("ул. "), col("STREET")),
                                    ).otherwise(None),
                                    when(
                                        col("BUILDING") != "",
                                        concat(lit("д. "), col("BUILDING")),
                                    ).otherwise(None),
                                    when(
                                        col("BUILD_SECT") != "", col("BUILD_SECT")
                                    ).otherwise(None),
                                    when(
                                        col("APARTMENT") != "",
                                        concat(lit("кв. "), col("APARTMENT")),
                                    ).otherwise(None),
                                )
                            )
                        )
                    )
                ),
            )
            .select("abonent_id", "address")
        )
        df_abonent_addr.cache()

        df = df_abonent.join(df_abonent_addr, "abonent_id", "left").drop_duplicates()

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .groupby(["names", "birth_date"])
            .agg(
                collect_set("phones").alias("phones"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("address"))).alias("address"),
                array_compact(flatten(collect_set("financials"))).alias("financials"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array(col("names")))
            .select(
                "names",
                "phones",
                "birth_date",
                "documents",
                "financials",
                "address",
                "actuality",
            )
        )

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"], col("documents")[0]["type"])
            .agg(
                collect_set("names").alias("names"),
                first("birth_date").alias("birth_date"),
                collect_set("phones").alias("phones"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("address"))).alias("address"),
                array_compact(flatten(collect_set("financials"))).alias("financials"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "phones",
                "birth_date",
                "documents",
                "financials",
                "address",
                "actuality",
            )
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = df.select(
            "names",
            "phones",
            "birth_date",
            "documents",
            "financials",
            "address",
            "actuality",
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
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
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
