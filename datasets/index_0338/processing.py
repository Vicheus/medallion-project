from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0338"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0338/raw/5120_ru_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("Email заказа")),
                            email_udf(col("Email аккаунта")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("Адрес доставки")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    regexp_extract(
                        col("Статус заказа"), r"\(от (\d{2}\.\d{2}\.\d{4})\)", 1
                    ),
                    lit("%d.%m.%Y"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Статус заказа"),
                    col("Статус заказа"),
                    lit("Сумма"),
                    col("Сумма"),
                    lit("Платежная система"),
                    col("Платежная система"),
                    lit("Оплата завершена"),
                    col("Оплата завершена"),
                ),
            )
            .select("names", "phones", "emails", "address", "actuality", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
