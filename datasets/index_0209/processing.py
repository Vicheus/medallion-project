from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    size,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0209"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0209/raw/pryanikov38.ru.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("client_name_c")))
            .withColumn("emails", email_udf(col("client_email_c")))
            .withColumn("phones", phone_udf(col("phone_c")))
            .withColumn("address", address_udf(col("address_c")))
            .withColumn("ip_address", ip_address_udf(col("ip_c")))
            .withColumn(
                "devices",
                when(
                    col("user_agent_c").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("user_agent_c").alias("user_agent"),
                            device_date_udf(
                                col("datetime_delivered_c"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "coordinates",
                when(
                    (
                        col("longitude_c").isNotNull()
                        & (col("longitude_c") != "")
                        & col("latitude_c").isNotNull()
                        & (col("latitude_c") != "")
                    ),
                    array(
                        array(
                            col("longitude_c").cast("float"),
                            col("latitude_c").cast("float"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("datetime_delivered_c"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment_c"),
                    col("comment_c"),
                    lit("comment_client_c"),
                    col("comment_client_c"),
                    lit("delivery_price_c"),
                    col("delivery_price_c"),
                    lit("purchase_price_c"),
                    col("purchase_price_c"),
                    lit("sberbank_acquiring_id_c"),
                    col("sberbank_acquiring_id_c"),
                    lit("telecom_operator_c"),
                    col("telecom_operator_c"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "ips",
                "devices",
                "coordinates",
                "raw_metadata",
            )
        )

        df = df.groupBy(["phones", "names"]).agg(
            array_distinct(flatten(collect_set("ips"))).alias("ips"),
            array_distinct(flatten(collect_set("devices"))).alias("devices"),
            array_distinct(flatten(collect_set("coordinates"))).alias("coordinates"),
            collect_set("emails").alias("emails"),
            collect_set("address").alias("address"),
            collect_set("raw_metadata").alias("raw_metadata"),
        )

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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "coordinates",
                when(size(col("coordinates")) > 0, col("coordinates")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
