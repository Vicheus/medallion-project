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
    trim,
    concat_ws,
    collect_set,
    flatten,
    max,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
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
    dataset_code_name: str = "index_0187"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0187/raw/raw/oc_customer_@DBC_links.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email")), email_udf(col("email_newsletter"))
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                phone_udf(col("telephone"), lit(self.dataset_country_code.value)),
            )
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
                ),
            )
            .withColumn("devices", array())
            .withColumn("address", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "customer_id",
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_1 = (
            df_1.groupby("customer_id")
            .agg(
                array_compact(collect_set("names")).alias("names"),
                array_compact(collect_set("phones")).alias("phones"),
                flatten(collect_set("emails")).alias("emails"),
                flatten(collect_set("ips")).alias("ips"),
                flatten(collect_set("devices")).alias("devices"),
                flatten(collect_set("address")).alias("address"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_1.show(n=20)

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0187/raw/raw/oc_order_@DBC_links.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn(
                "phones",
                phone_udf(col("telephone"), lit(self.dataset_country_code.value)),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("user_agent").alias("user_agent"),
                            device_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
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
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("payment_country").isNotNull()
                                    | col("payment_address_1").isNotNull(),
                                    trim(
                                        concat_ws(
                                            " ",
                                            when(
                                                col("payment_country").isNotNull(),
                                                col("payment_country"),
                                            ).otherwise(None),
                                            when(
                                                col("payment_address_1").isNotNull(),
                                                col("payment_address_1"),
                                            ).otherwise(None),
                                            when(
                                                col("payment_address_2").isNotNull(),
                                                col("payment_address_2"),
                                            ).otherwise(None),
                                        )
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("shipping_country").isNotNull()
                                    | col("shipping_city").isNotNull(),
                                    trim(
                                        concat_ws(
                                            " ",
                                            when(
                                                col("shipping_country").isNotNull(),
                                                col("shipping_country"),
                                            ).otherwise(None),
                                            when(
                                                col("shipping_city").isNotNull(),
                                                col("shipping_city"),
                                            ).otherwise(None),
                                            when(
                                                col("shipping_address_1").isNotNull(),
                                                col("shipping_address_1"),
                                            ).otherwise(None),
                                            when(
                                                col("shipping_address_2").isNotNull(),
                                                col("shipping_address_2"),
                                            ).otherwise(None),
                                        )
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_id"),
                    col("order_id"),
                    lit("store_name"),
                    col("store_name"),
                    lit("total"),
                    col("total"),
                    lit("comment"),
                    col("comment"),
                    lit("shipping_method"),
                    col("shipping_method"),
                    lit("shipping_company"),
                    col("shipping_company"),
                ),
            )
            .select(
                "customer_id",
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_2_with_id = (
            df_2.filter(col("customer_id") != 0)
            .groupby("customer_id")
            .agg(
                array_compact(collect_set("names")).alias("names"),
                array_compact(collect_set("phones")).alias("phones"),
                flatten(collect_set("emails")).alias("emails"),
                flatten(collect_set("ips")).alias("ips"),
                flatten(collect_set("devices")).alias("devices"),
                flatten(collect_set("address")).alias("address"),
                collect_set("raw_metadata").alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_2_without_id = (
            df_2.filter(col("customer_id") == 0)
            .groupby(["names", "emails"])
            .agg(
                flatten(collect_set(col("ips"))).alias("ips"),
                flatten(collect_set(col("devices"))).alias("devices"),
                flatten(collect_set(col("address"))).alias("address"),
                array_compact(collect_set(col("phones"))).alias("phones"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array_compact(array(col("names"))))
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_2 = df_2_with_id.unionAll(df_2_without_id)

        df = df_1.unionAll(df_2)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
            .withColumn(
                "devices",
                when(
                    size(array_compact(col("devices"))) > 0,
                    array_compact(col("devices")),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
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
