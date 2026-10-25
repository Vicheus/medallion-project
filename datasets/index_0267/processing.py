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
    max,
    collect_set,
)

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
    dataset_code_name: str = "index_0267"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0267/raw/leomax.ru/leomax_ru.csv",
                sep=";",
                header=True,
            )
            .replace("\t", "")
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("МобТелефон")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("Индекс").cast("int"),
                        col("Адрес доставки 1"),
                        col("Адрес доставки 2"),
                        col("Адрес доставки 3"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата заказа"), lit("%m/%d/%Y %H:%M")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Бренд"),
                    col("Бренд"),
                    lit("Название"),
                    col("Название"),
                    lit("Цена со скидкой"),
                    col("Цена со скидкой"),
                    lit("Цена без скидки"),
                    col("Цена без скидки"),
                ),
            )
            .select("names", "phones", "address", "actuality", "raw_metadata")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                max(col("actuality")).alias("actuality"),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
            )
            .select("names", "phones", "address", "actuality", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
