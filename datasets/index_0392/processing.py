from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
    struct,
    concat,
    regexp_extract,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0392"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0392/raw/aurora.gun.ru.txt",
            sep=",",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("Почта")))))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Номер телефона"))))),
            )
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (
                                    col("Паспорт серия").isNotNull()
                                    & (col("Паспорт серия") != "")
                                )
                                & (
                                    col("Паспорт номер").isNotNull()
                                    & (col("Паспорт номер") != "")
                                ),
                                document_udf(
                                    lit(None),
                                    concat(col("Паспорт серия"), col("Паспорт номер")),
                                    regexp_extract(
                                        col("Паспорт дата выдачи"),
                                        r"(\d{2}\.\d{2}\.\d{4})",
                                        1,
                                    ),
                                    lit(None),
                                    col("Паспорт кем выдан"),
                                    lit(None),
                                    lit("%d.%M.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("ИНН"),
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
            )
            .withColumn(
                "accounts",
                when(
                    col("Логин").isNotNull() & col("Пароль").isNotNull(),
                    array(
                        struct(
                            lit("Аврора").alias("title"),
                            lit("https://aurora.gun.ru").alias("link"),
                            col("Логин").alias("login"),
                            col("Пароль").alias("password"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "address", "documents", "accounts")
        )

        df = df.groupBy(["names", "emails"]).agg(
            array_compact(array_distinct(flatten(collect_set(col("phones"))))).alias(
                "phones"
            ),
            array_compact(array_distinct(collect_set(col("address")))).alias("address"),
            array_compact(array_distinct(flatten(collect_set(col("documents"))))).alias(
                "documents"
            ),
            array_compact(array_distinct(flatten(collect_set(col("accounts"))))).alias(
                "accounts"
            ),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
