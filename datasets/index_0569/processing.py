from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    lit,
    size,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0569"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0569/raw/statprivat.csv",
            sep=";",
            header=True,
        )

        df_ip = (
            df.filter(col("Наименование").startswith("Индивидуальный предприниматель"))
            .withColumn(
                "names",
                name_udf(
                    regexp_replace(
                        col("Наименование"), "Индивидуальный предприниматель ", ""
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Регион")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("ИНН").isNotNull(),
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
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("ОКВЭД"), col("ОКВЭД")),
            )
            .withColumn("works", array())
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
            )
        )

        df_companies = (
            df.filter(~col("Наименование").startswith("Индивидуальный предприниматель"))
            .withColumn("names", name_udf(col("Руководитель")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Регион")))
            .withColumn("documents", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("ОКВЭД"), col("ОКВЭД"), lit("ИНН предприятия"), col("ИНН")
                ),
            )
            .withColumn(
                "works",
                array(
                    when(
                        col("Наименование").isNotNull(),
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("Наименование"),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
            )
        )

        df = df_ip.unionAll(df_companies)

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
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
