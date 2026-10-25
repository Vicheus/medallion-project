from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    struct,
    lit,
    size,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0389"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0389/raw/perekrestok_ru.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("Имя"), lit(None), col("Отчество"))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("E-mail")))))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Телефон"))))),
            )
            .withColumn(
                "accounts",
                array(
                    when(
                        col("Номер карты").isNotNull(),
                        struct(
                            lit("Перекрёсток").alias("title"),
                            lit("https://www.perekrestok.ru").alias("link"),
                            col("Номер карты").alias("client_card_number"),
                        ),
                    )
                ),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("Баланс"), col("Баланс")))
            .select("names", "emails", "phones", "accounts", "raw_metadata")
        )

        df = (
            df.groupBy(["names", "emails", "phones"])
            .agg(
                collect_set(col("accounts")).alias("accounts"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
            )
            .select("names", "emails", "phones", "accounts", "raw_metadata")
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
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
