from pyspark.sql.types import StructType, StructField, StringType, ArrayType
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    concat,
    array_compact,
    size,
    concat_ws,
    flatten,
    collect_set,
    from_json,
    explode,
    first,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_date_udf, ip_address_udf
from parsetron.sections.device.udfs import device_date_udf
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
    dataset_code_name: str = "index_0307"

    def parser(self):
        ip_address_json_schema = ArrayType(
            StructType(
                [
                    StructField("customer_ip_id", StringType(), True),
                    StructField("customer_id", StringType(), True),
                    StructField("ip", StringType(), True),
                    StructField("date_added", StringType(), True),
                ]
            )
        )

        df_address = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0307/raw/raw/customers_address_*.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "address",
                array(
                    address_udf(
                        concat_ws(
                            " ",
                            when(
                                col("Address Postcode") != "", col("Address Postcode")
                            ).otherwise(None),
                            when(
                                col("Address Country") != "", col("Address Country")
                            ).otherwise(None),
                            when(
                                col("Address Zone") != "", col("Address Zone")
                            ).otherwise(None),
                            when(
                                col("Address City") != "", col("Address City")
                            ).otherwise(None),
                            when(col("Address 1") != "", col("Address 1")).otherwise(
                                None
                            ),
                            when(
                                (col("Address 2") != "")
                                & (col("Address 1") != col("Address 2")),
                                col("Address 2"),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .groupBy(["Customer ID"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address")
            )
            .select("Customer ID", "address")
        )

        df_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0307/raw/raw/customers_ecipa*.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("First Name"), col("Last Name"), lit(None))
            )
            .withColumn("emails", email_udf(col("E-Mail")))
            .withColumn("phones", phone_udf(col("Telephone")))
            .withColumn("ip_array", from_json("IP Addresses", ip_address_json_schema))
            .withColumn("ip_array_exploded", explode(col("ip_array")))
            .withColumn("ip", ip_address_udf(col("ip_array_exploded.ip")))
            .withColumn("date_added", col("ip_array_exploded.date_added"))
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
            .groupBy(["Customer ID"])
            .agg(
                first(col("names")).alias("names"),
                first(col("emails")).alias("emails"),
                first(col("phones")).alias("phones"),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
            )
            .select("Customer ID", "names", "emails", "phones", "ips")
        )

        df_customers = (
            df_customers.join(df_address, "Customer ID", "left")
            .withColumn("raw_metadata", lit(None))
            .select(
                "Customer ID",
                "names",
                "emails",
                "phones",
                "address",
                "ips",
                "raw_metadata",
            )
        )

        df_customers_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0307/raw/raw/orders*.csv",
                sep=";",
                header=True,
            )
            .filter(col("Customer ID") == 0)
            .withColumn(
                "names",
                name_parts_udf(
                    col("Customer First Name"), col("Customer Last Name"), lit(None)
                ),
            )
            .withColumn("emails", email_udf(col("Customer E-mail")))
            .withColumn("phones", phone_udf(col("Customer Telephone")))
            .withColumn("ip", ip_address_udf(col("IP")))
            .withColumn("date_added", col("Date Added"))
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
                                    when(
                                        col("Payment Postcode") != "",
                                        col("Payment Postcode"),
                                    ).otherwise(None),
                                    when(
                                        col("Payment Country") != "",
                                        col("Payment Country"),
                                    ).otherwise(None),
                                    when(
                                        col("Payment Zone") != "", col("Payment Zone")
                                    ).otherwise(None),
                                    when(
                                        col("Payment City") != "", col("Payment City")
                                    ).otherwise(None),
                                    when(
                                        col("Payment Address 1") != "",
                                        col("Payment Address 1"),
                                    ).otherwise(None),
                                    when(
                                        (col("Payment Address 1") != "")
                                        & (
                                            col("Payment Address 1")
                                            != col("Payment Address 2")
                                        ),
                                        col("Payment Address 2"),
                                    ).otherwise(None),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    when(
                                        col("Shipping Postcode") != "",
                                        col("Shipping Postcode"),
                                    ).otherwise(None),
                                    when(
                                        col("Shipping Country") != "",
                                        col("Shipping Country"),
                                    ).otherwise(None),
                                    when(
                                        col("Shipping Zone") != "", col("Shipping Zone")
                                    ).otherwise(None),
                                    when(
                                        col("Shipping City") != "", col("Shipping City")
                                    ).otherwise(None),
                                    when(
                                        col("Shipping Address 1") != "",
                                        col("Shipping Address 1"),
                                    ).otherwise(None),
                                    when(
                                        (col("Shipping Address 1") != "")
                                        & (
                                            col("Shipping Address 1")
                                            != col("Shipping Address 2")
                                        ),
                                        col("Shipping Address 2"),
                                    ).otherwise(None),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("User Agent").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(
                                    lit("ecipa.ru").alias("title"),
                                    col("User Agent").alias("user_agent"),
                                    device_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Date Added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Payment Company"),
                    col("Payment Company"),
                    lit("Payment Tax ID"),
                    col("Payment Tax ID"),
                    lit("Shipping Method"),
                    col("Shipping Method"),
                    lit("Comment"),
                    col("Comment"),
                    lit("Total"),
                    col("Total"),
                    lit("Custom Field"),
                    col("Custom Field"),
                    lit("Payment Custom Field"),
                    col("Payment Custom Field"),
                    lit("Shipping Custom Field"),
                    col("Shipping Custom Field"),
                ),
            )
            .select(
                "Customer ID",
                "names",
                "emails",
                "phones",
                "address",
                "devices",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df_customers_from_orders_not_registered = (
            df_customers_from_orders.filter(col("Customer ID") == 0)
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "devices",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df_customers_from_orders_registered = df_customers_from_orders.filter(
            col("Customer ID") != 0
        )

        df_customers = (
            df_customers.join(
                df_customers_from_orders_registered, "Customer ID", "left"
            )
            .select(
                array_compact(
                    array_distinct(
                        concat(
                            df_customers["address"],
                            df_customers_from_orders_registered["address"],
                        )
                    )
                ).alias("address"),
                array_compact(
                    array_distinct(
                        concat(
                            df_customers["ips"],
                            df_customers_from_orders_registered["ips"],
                        )
                    )
                ).alias("ips"),
                array_compact(
                    array_distinct(
                        array(
                            df_customers["emails"],
                            df_customers_from_orders_registered["emails"],
                        )
                    )
                ).alias("emails"),
                array_compact(
                    array_distinct(
                        array(
                            df_customers["phones"],
                            df_customers_from_orders_registered["phones"],
                        )
                    )
                ).alias("phones"),
                df_customers["names"].alias("names"),
                df_customers_from_orders_registered["actuality"].alias("actuality"),
                df_customers_from_orders_registered["devices"].alias("devices"),
                df_customers_from_orders_registered["raw_metadata"].alias(
                    "raw_metadata"
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "devices",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_customers_from_orders_not_registered.unionAll(df_customers)

        df = df.drop_duplicates(["names", "emails", "phones"])

        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
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
