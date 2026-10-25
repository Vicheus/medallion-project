from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    concat_ws,
    array_compact,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0261"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0261/raw/utair_ru.csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон (норм)")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "address",
                when(
                    col("Адрес (город)").isNotNull(),
                    address_udf(
                        concat_ws(
                            " ",
                            col("Адрес (страна)"),
                            col("Адрес (регион)"),
                            col("Адрес (город)"),
                            col("Адрес (улица, дом)"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Паспорт / ID").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Паспорт / ID"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("documents1").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("documents1"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("documents0").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("documents0"),
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
            .select("names", "phones", "emails", "birth_date", "address", "documents")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
