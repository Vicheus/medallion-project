from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, concat_ws, coalesce

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0290"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0290/raw/sushigo.online/*.csv",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "address",
                when(
                    col("Улица").isNotNull(),
                    address_udf(
                        concat_ws(" ", col("Улица"), col("Дом"), col("Квартира"))
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("Последний заказ"), col("Создан")), lit("%d.%m.%Y")
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Комментарий"),
                    col("Комментарий"),
                    lit("Канал продаж"),
                    col("Канал продаж"),
                    lit("Филиал"),
                    col("Филиал"),
                    lit("Заказы"),
                    col("Заказы"),
                    lit("Сумма"),
                    col("Сумма"),
                ),
            )
            .select("names", "phones", "address", "actuality", "raw_metadata")
        )

        df = df.drop_duplicates()
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
