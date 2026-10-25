from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    expr,
    collect_set,
    flatten,
    max,
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
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0448"
    validate_invalid_groupping: bool = True

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0448/raw/atletic-food.ru/Пользователи.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("telephone")))
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "raw_metadata",
                array_compact(
                    array_distinct(
                        array(
                            raw_metadata_udf(
                                lit("order_total"),
                                col("order_total"),
                                lit("company_type"),
                                col("company_type"),
                                lit("customer_comment"),
                                col("customer_comment"),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn("address", array())
            .withColumn("devices", array())
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "devices",
                "raw_metadata",
                "actuality",
            )
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0448/raw/atletic-food.ru/Заказы.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("telephone"))))),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("shipping_company"),
                    col("shipping_company"),
                    lit("shipping_method"),
                    col("shipping_method"),
                    lit("total_payment"),
                    col("total_payment"),
                    lit("total"),
                    col("total"),
                    lit("comment"),
                    col("comment"),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("payment_city"),
                                    col("payment_address_1"),
                                    col("payment_address_2"),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("shipping_city"),
                                    col("shipping_address_1"),
                                    col("shipping_address_2"),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "devices",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("user_agent").isNotNull(),
                                struct(
                                    lit("Оформление заказа").alias("action"),
                                    col("user_agent").alias("user_agent"),
                                    device_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "devices",
                "raw_metadata",
                "actuality",
            )
        )

        df_orders = (
            df_orders.groupBy(["names", "phones"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("devices"))))
                ).alias("devices"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "devices",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_orders.unionAll(df_users)

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("raw_metadata"))))
                ).alias("raw_metadata"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("devices"))))
                ).alias("devices"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "devices",
                "raw_metadata",
                "actuality",
            )
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
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = (
            df.withColumn("emails", expr("slice(emails, 1, 10)"))
            .withColumn("address", expr("slice(address, 1, 10)"))
            .withColumn("ips", expr("slice(ips, 1, 10)"))
            .withColumn("devices", expr("slice(devices, 1, 10)"))
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 10)"))
            .withColumn("phones", expr("slice(phones, 1, 10)"))
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
