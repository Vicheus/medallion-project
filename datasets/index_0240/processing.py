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
    concat,
    regexp_replace,
    collect_set,
    flatten,
    max,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0240"

    def parser(self):
        df_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0240/raw/customers_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("\t", "")
            .withColumn(
                "names",
                regexp_replace(
                    regexp_replace(
                        name_parts_udf(col("firstname"), col("lastname"), lit(None)),
                        "quot",
                        "",
                    ),
                    "Quot",
                    "",
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("customer_id", "names", "emails", "phones", "ips", "actuality")
        )

        df_address = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0240/raw/address_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("\t", "")
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address_1")), address_udf(col("address"))
                        )
                    )
                ),
            )
            .select("customer_id", "address")
        )

        df_registered_customers_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0240/raw/registered_customers_from_orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("\t", "")
            .withColumn(
                "names",
                regexp_replace(
                    regexp_replace(
                        name_parts_udf(col("firstname"), col("lastname"), lit(None)),
                        "quot",
                        "",
                    ),
                    "Quot",
                    "",
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn("address", array(address_udf(col("address"))))
            .select("customer_id", "names", "emails", "phones", "ips", "address")
        )

        df_address = df_address.alias("df_address")
        df_customers = df_customers.alias("df_customers")
        df_registered_customers_from_orders = df_registered_customers_from_orders.alias(
            "df_registered_customers_from_orders"
        )

        df_registered_customers = (
            df_customers.join(df_address, "customer_id", "left")
            .join(df_registered_customers_from_orders, "customer_id", "left")
            .withColumn("names_merged", col("df_customers.names"))
            .withColumn(
                "address_merged",
                array_distinct(
                    array_compact(
                        concat(
                            col("df_address.address"),
                            col("df_registered_customers_from_orders.address"),
                        )
                    )
                ),
            )
            .withColumn(
                "phones_merged",
                array_distinct(
                    array_compact(
                        array(
                            col("df_customers.phones"),
                            col("df_registered_customers_from_orders.phones"),
                        )
                    )
                ),
            )
            .withColumn(
                "emails_merged",
                array_distinct(
                    array_compact(
                        array(
                            col("df_customers.emails"),
                            col("df_registered_customers_from_orders.emails"),
                        )
                    )
                ),
            )
            .withColumn(
                "ips_merged",
                array_distinct(
                    array_compact(
                        concat(
                            col("df_customers.ips"),
                            col("df_registered_customers_from_orders.ips"),
                        )
                    )
                ),
            )
            .select(
                col("names_merged").alias("names"),
                col("emails_merged").alias("emails"),
                col("phones_merged").alias("phones"),
                col("ips_merged").alias("ips"),
                col("address_merged").alias("address"),
                col("actuality").alias("actuality"),
            )
        )
        df_customers_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0240/raw/customers_from_orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("\t", "")
            .withColumn(
                "names",
                regexp_replace(
                    regexp_replace(
                        name_parts_udf(col("firstname"), col("lastname"), lit(None)),
                        "quot",
                        "",
                    ),
                    "Quot",
                    "",
                ),
            )
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("telephone")))))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn("address", array_compact(array(address_udf(col("address")))))
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "phones", "ips", "address", "actuality")
        )

        df = df_registered_customers.unionAll(df_customers_from_orders)

        df = df.groupBy(["phones", "names"]).agg(
            flatten(array_distinct(array_compact(collect_set("emails")))).alias(
                "emails"
            ),
            flatten(array_distinct(array_compact(collect_set("ips")))).alias("ips"),
            flatten(array_distinct(array_compact(collect_set("address")))).alias(
                "address"
            ),
            max("actuality").alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
