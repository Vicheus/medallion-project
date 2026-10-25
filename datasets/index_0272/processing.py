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
    collect_set,
    concat,
    flatten,
    max,
    greatest,
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
    dataset_code_name: str = "index_0272"

    def parser(self):
        df_registered_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0272/raw/hsnonline.ru/preprocessed/customers_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    col("ip_address").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("ХСН онлайн").alias("title"),
                            lit("https://hsnonline.ru").alias("link"),
                            col("email").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select(
                "customer_id",
                "names",
                "emails",
                "phones",
                "ips",
                "actuality",
                "accounts",
            )
        )

        df_registered_customers.show(n=20)

        df_customer_address = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0272/raw/hsnonline.ru/preprocessed/customers_address_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        when(col("postcode").isNotNull(), col("postcode")).otherwise(
                            None
                        ),
                        when(col("city").isNotNull(), col("city")).otherwise(None),
                        when(col("address_1").isNotNull(), col("address_1")).otherwise(
                            None
                        ),
                    )
                ),
            )
            .groupBy(["customer_id"])
            .agg(
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                )
            )
            .select("customer_id", "address")
        )

        df_registered_customers_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0272/raw/hsnonline.ru/preprocessed/registered_customers_from_orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names2", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("emails2", email_udf(col("email")))
            .withColumn("phones2", phone_udf(col("telephone")))
            .withColumn(
                "actuality2",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips2",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    col("ip_address").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn("address2", array(address_udf(col("address"))))
            .select(
                "customer_id",
                "names2",
                "emails2",
                "phones2",
                "ips2",
                "actuality2",
                "address2",
            )
        )

        df_registered_customers = (
            df_registered_customers.join(
                df_registered_customers_from_orders, "customer_id", "left"
            )
            .join(df_customer_address, "customer_id", "left")
            .withColumn(
                "names",
                array_compact(array_distinct(array(col("names"), col("names2")))),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(array(col("emails"), col("emails2")))),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(col("phones"), col("phones2")))),
            )
            .withColumn(
                "address",
                array_compact(array_distinct(concat(col("address"), col("address2")))),
            )
            .withColumn(
                "ips", array_compact(array_distinct(concat(col("ips"), col("ips2"))))
            )
            .withColumn("actuality", greatest(col("actuality"), col("actuality2")))
            .select(
                "names", "emails", "phones", "ips", "actuality", "address", "accounts"
            )
        )

        df_not_registered_customers_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0272/raw/hsnonline.ru/preprocessed/not_registered_customers_from_orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    col("ip_address").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("accounts", array())
            .select(
                "names", "emails", "phones", "ips", "actuality", "address", "accounts"
            )
        )

        df_not_registered_customers_from_orders = (
            df_not_registered_customers_from_orders.groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("accounts"))))
                ).alias("accounts"),
                max(col("actuality")).alias("actuality"),
            )
            .withColumn("names", array_compact(array(col("names"))))
            .withColumn("phones", array_compact(array(col("phones"))))
            .select(
                "names", "emails", "phones", "ips", "actuality", "address", "accounts"
            )
        )

        df = df_registered_customers.unionAll(df_not_registered_customers_from_orders)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
