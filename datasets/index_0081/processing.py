from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    when,
    size,
    collect_set,
    flatten,
    coalesce,
    max,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0081"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0081/raw/YOTA 2013 - @bereza_bd/YOTA.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_udf(
                    regexp_replace(regexp_replace(col("Клиент"), "Xxxx", ""), "Xxx", "")
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            regexp_replace(
                                regexp_replace(address_udf("Адрес юр"), "Xxxx", ""),
                                "Xxx",
                                "",
                            ),
                            regexp_replace(
                                regexp_replace(address_udf("Адрес факт"), "Xxxx", ""),
                                "Xxx",
                                "",
                            ),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("e-mail")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(array(phone_udf("Телефоны"), phone_udf("Телефон")))
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull() | col("Паспорт").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Паспорт").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Паспорт"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
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
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("Дата контракта"), col("Дата начала")), lit("%d.%m.%Y")
                ),
            )
        )

        df_without_doc = df.filter(col("documents")[0]["serial"].isNull())
        df_without_doc = (
            df_without_doc.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .select("names", "address", "emails", "phones", "documents", "actuality")
        )

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
                flatten(collect_set("phones")).alias("phones"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("address")).alias("address"),
                max("actuality").alias("actuality"),
            )
            .select("names", "address", "emails", "phones", "documents", "actuality")
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = df.drop_duplicates(["names", "address", "emails", "phones", "documents"])

        df = df.select("names", "address", "emails", "phones", "documents", "actuality")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(
                    size(col("names")) > 0, array_compact(array_distinct(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(col("emails")) > 0,
                    array_compact(array_distinct(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(col("address")) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(col("documents")) > 0,
                    array_compact(array_distinct(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(col("phones")) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
