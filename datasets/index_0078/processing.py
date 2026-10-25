from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    struct,
    collect_set,
    size,
    flatten,
    collect_list,
    coalesce,
    max,
)

from parsetron import Parsetron
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0078"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0078/raw/sushi_pizza.csv",
            sep=",",
            header=True,
        )
        df = (
            df.replace("------", None)
            .replace("-----", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(col("payment_address_1")),
                            address_udf(col("payment_address_2")),
                            address_udf(col("shipping_address_1")),
                            address_udf(col("shipping_address_2")),
                        )
                    )
                ),
            )
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
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("date_modified"), col("date_added")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_id"),
                    col("order_id"),
                    lit("comment"),
                    col("comment"),
                    lit("store_name"),
                    col("store_name"),
                    lit("date_dostavki"),
                    col("date_dostavki"),
                ),
            )
            .select(
                "names",
                "phones",
                "address",
                "ips",
                "devices",
                "actuality",
                "raw_metadata",
            )
        )

        df = df.groupby("phones").agg(
            when(size(collect_set("names")) > 0, collect_set("names"))
            .otherwise(None)
            .alias("names"),
            when(
                size(array_distinct(flatten(collect_list("devices")))) > 0,
                array_distinct(flatten(collect_list("devices"))),
            )
            .otherwise(None)
            .alias("devices"),
            when(
                size(array_distinct(flatten(collect_list("address")))) > 0,
                array_distinct(flatten(collect_list("address"))),
            )
            .otherwise(None)
            .alias("address"),
            when(
                size(array_distinct(flatten(collect_list("ips")))) > 0,
                array_distinct(flatten(collect_list("ips"))),
            )
            .otherwise(None)
            .alias("ips"),
            when(size(collect_set("raw_metadata")) > 0, collect_set("raw_metadata"))
            .otherwise(None)
            .alias("raw_metadata"),
            max("actuality").alias("actuality"),
        )

        df = df.withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
