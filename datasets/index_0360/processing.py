from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0360"

    def parser(self):
        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0360/raw/blackstarwear.ru -/Клиенты (очищенная).txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip").isNotNull(),
                                struct(
                                    col("ip").alias("ip"),
                                    ip_date_udf(
                                        col("created_at"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn("devices", array())
            .select("names", "emails", "phones", "ips", "devices", "actuality")
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0360/raw/blackstarwear.ru -/Заказы (очищенная).txt",
                sep=",",
                header=False,
            )
            .withColumn("names", name_parts_udf(col("_c3"), col("_c4"), lit(None)))
            .withColumn("emails", email_udf(col("_c1")))
            .withColumn("phones", phone_udf(col("_c6")))
            .withColumn(
                "actuality", actuality_date_udf(col("_c7"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("ip", ip_address_udf(col("_c0")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip").isNotNull(),
                                struct(
                                    col("ip").alias("ip"),
                                    ip_date_udf(
                                        col("_c7"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("_c10").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("_c10").alias("user_agent"),
                            device_date_udf(col("_c7"), lit("%Y-%m-%d %H:%M:%S")).alias(
                                "date"
                            ),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "ips", "devices", "actuality")
        )

        df = df_clients.unionAll(df_orders)
        df = df.drop_duplicates(["names", "phones", "emails"])

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
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
