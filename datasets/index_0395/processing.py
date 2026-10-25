from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0395"

    def parser(self):
        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0395/raw/avrora24.ru - @StormBaseAdapter/Сделки.csv",
                sep=";",
                header=True,
            )
            .withColumn("user_id", col("Контакт: ID"))
            .withColumn("address", address_udf(col("Адрес доставки")))
            .select("user_id", "address")
        )

        df_orders = df_orders.groupBy("user_id").agg(
            array_compact(collect_set(col("address"))).alias("address")
        )

        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0395/raw/avrora24.ru - @StormBaseAdapter/Клиенты.csv",
                sep=";",
                header=True,
            )
            .withColumn("user_id", col("ID"))
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Мобильный телефон")),
                            phone_udf(col("Рабочий телефон")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Рабочий e-mail")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Последняя активность"), lit("%d.%m.%Y %H:%M:%S")
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Комментарий"),
                    col("Комментарий"),
                    lit("Источник"),
                    col("Источник"),
                    lit("Дополнительно об источнике"),
                    col("Дополнительно об источнике"),
                ),
            )
            .select("user_id", "names", "phones", "emails", "actuality", "raw_metadata")
        )

        df = df_clients.join(df_orders, "user_id", "left").select(
            "names", "phones", "emails", "address", "actuality", "raw_metadata"
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
