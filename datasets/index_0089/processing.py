from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    flatten,
    struct,
    array_compact,
    array_distinct,
    collect_list,
    size,
    max,
    collect_set,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0089"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0089/raw/Dump_public_autozs.ru_14.08.2022_nopassw/autozs.ru.csv",
            sep="\t",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("firstname")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("telephone")), phone_udf(col("telephone_2"))
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email_2")))
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("shipping_address_1")),
                            address_udf(col("shipping_address_2")),
                            address_udf(col("payment_address_1")),
                            address_udf(col("payment_address_2")),
                        )
                    )
                ),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
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
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("date_modified"), col("date_added"), col("date_calendar")
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("store_name"),
                    df["store_name"],
                    lit("shipping_method"),
                    df["shipping_method"],
                    lit("payment_method"),
                    df["payment_method"],
                ),
            )
        )
        df = df.groupBy(["phones", "names"]).agg(
            array_distinct(flatten(collect_list("emails"))).alias("emails"),
            array_distinct(flatten(collect_list("address"))).alias("address"),
            array_distinct(flatten(collect_list("ips"))).alias("ips"),
            array_distinct(flatten(collect_list("devices"))).alias("devices"),
            collect_set("raw_metadata").alias("raw_metadata"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
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
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "ips",
            "devices",
            "actuality",
            "raw_metadata",
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
