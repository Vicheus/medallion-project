from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    struct,
    array_compact,
    size,
)
from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.financials.udfs import financial_invoice_number_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    raw_metadata_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0412"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0412/raw/full_data_deltasert_ru_2025_9k+.csv",
            sep=",",
        )
        df1 = (
            df.withColumn("names", name_udf(col("ФИО руководителя")))
            .withColumn("phones", phone_udf(col("Телефон руководителя")))
            .withColumn("emails", email_udf(col("E-mail руководителя")))
            .withColumn("financials", array())
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn(
                "works",
                when(
                    col("Краткое наименование").isNotNull()
                    & (col("Краткое наименование") != ""),
                    array(
                        work_udf(
                            col("Должность"),
                            lit(None),
                            lit(None),
                            col("Краткое наименование").alias("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df2 = (
            df.withColumn("names", name_udf(col("Лицо 1 ФИО")))
            .withColumn("phones", phone_udf(col("Лицо 1 Телефон")))
            .withColumn("emails", email_udf(col("Лицо 1 Email")))
            .withColumn("documents", array())
            .withColumn("financials", array())
            .withColumn("works", array())
            .withColumn("address", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("Лицо 1 Комментарий"), col("Лицо 1 Комментарий")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df3 = (
            df.withColumn("names", name_udf(col("Лицо 2 ФИО")))
            .withColumn("phones", phone_udf(col("Лицо 2 Телефон")))
            .withColumn("emails", email_udf(col("Лицо 2 Email")))
            .withColumn("address", array())
            .withColumn("documents", array())
            .withColumn("financials", array())
            .withColumn("works", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("Лицо 2 Комментарий"), col("Лицо 2 Комментарий")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df4 = (
            df.withColumn("names", name_udf(col("Лицо 3 ФИО")))
            .withColumn("phones", phone_udf(col("Лицо 3 Телефон")))
            .withColumn("emails", email_udf(col("Лицо 3 Email")))
            .withColumn("documents", array())
            .withColumn("financials", array())
            .withColumn("works", array())
            .withColumn("address", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("Лицо 3 Комментарий"), col("Лицо 3 Комментарий")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df5 = (
            df.withColumn("names", name_udf(col("Полное наименование")))
            .withColumn("phones", lit(None))
            .withColumn("emails", email_udf(col("Email_CSV")))
            .withColumn(
                "address",
                array(address_udf(col("Юр адрес")), address_udf(col("Факт адрес"))),
            )
            .withColumn(
                "invoice_number", financial_invoice_number_udf(col("Расчётный счёт"))
            )
            .withColumn(
                "documents",
                when(
                    (col("ИНН").isNotNull() | col("КПП").isNotNull())
                    | (col("ОГРН").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("КПП").isNotNull()),
                                document_udf(
                                    lit("кпп"),
                                    col("КПП"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("ОГРН").isNotNull()),
                                document_udf(
                                    lit("огрн"),
                                    col("ОГРН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("ИНН").isNotNull()),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
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
                    col("invoice_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("invoice_number").isNotNull(),
                                struct(
                                    col("Банк").alias("title"),
                                    col("invoice_number").alias("card_number"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("works", array())
            .withColumn("raw_metadata", raw_metadata_udf(lit("БИК"), col("БИК")))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df = df1.unionAll(df2).unionAll(df3).unionAll(df4).unionAll(df5)

        df = df.drop_duplicates(["names", "emails", "phones"])

        df = df.repartition(self.output_file_count)

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
