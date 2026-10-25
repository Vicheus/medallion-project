from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_set,
    flatten,
    regexp_replace,
)

from parsetron import Parsetron

from parsetron.sections.document.udfs import document_udf

from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
    relations_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0439"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/new/fira.ru/preprocessed/fira.ru.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                regexp_replace(
                    name_udf(col("Название")),
                    "Общество С Ограниченной Ответственностью",
                    "ООО",
                ),
            )
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Телефон")), phone_udf(col("Факс")))
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("E-mail")))))
            )
            .withColumn(
                "documents",
                when(
                    (col("ИНН").isNotNull() | (col("ОГРН").isNotNull())),
                    array_compact(
                        array(
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
            .withColumn("Руководитель", name_udf(col("Руководитель")))
            .withColumn(
                "relations",
                when(
                    col("Руководитель").isNotNull(),
                    array(
                        when(
                            col("Руководитель").isNotNull(),
                            relations_udf(
                                concat_ws(" ", col("Руководитель"), col("Должность"))
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Статус"),
                    col("Статус"),
                    lit("Код ОКАТО"),
                    col("Код ОКАТО"),
                    lit("Код ОКВЭД"),
                    col("Код ОКВЭД"),
                    lit("Название ОКВЭД"),
                    col("Название"),
                    lit("Группа"),
                    col("Группа"),
                    lit("ОКПО"),
                    col("ОКПО"),
                    lit("Дата регистрации"),
                    col("Дата регистрации"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "relations",
                "raw_metadata",
                "ИНН",
            )
        )

        df_with_inn = df.filter(col("ИНН").isNotNull())
        df_with_inn = (
            df_with_inn.groupBy(["ИНН", "names"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(
                    array_distinct(flatten(collect_set(col("relations"))))
                ).alias("relations"),
                collect_set(col("address")).alias("address"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
            )
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "relations",
                "raw_metadata",
            )
        )

        df_without_inn = df.filter(col("ИНН").isNull())
        df_without_inn = (
            df_without_inn.withColumn("address", array(col("address")))
            .withColumn("names", array(col("names")))
            .withColumn("raw_metadata", array(col("raw_metadata")))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "relations",
                "raw_metadata",
            )
        )

        df = df_with_inn.unionAll(df_without_inn)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
