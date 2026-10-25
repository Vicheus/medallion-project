from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0291"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0291/raw/tenders_parsed_bicotender_ru/parsed_tenders.csv",
            sep=",",
            header=True,
        ).filter(
            (col("E-mail").contains("ru"))
            | (col("Адрес").contains("Российская Федерация"))
            | (col("Адрес").contains("Россия"))
        )

        df_companies = (
            df.withColumn("names", name_udf(col("заказчик")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
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
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("КПП").isNotNull(),
                                document_udf(
                                    lit("кпп"),
                                    col("КПП"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("ОГРН").isNotNull(),
                                document_udf(
                                    lit("огрн"),
                                    col("ОГРН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn("works", array())
            .select("names", "phones", "emails", "address", "documents", "works")
        )

        df_users = (
            df.withColumn("names", name_udf(col("Контактное лицо")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("documents", array())
            .withColumn(
                "works",
                when(
                    col("заказчик").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("заказчик"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "address", "documents", "works")
        )

        df = df_companies.unionAll(df_users)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
