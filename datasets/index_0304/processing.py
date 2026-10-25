from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, from_json, concat_ws
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0304"

    def parser(self):
        address_json_schema = StructType(
            [
                StructField("city", StringType(), True),
                StructField("street", StringType(), True),
                StructField("house", StringType(), True),
                StructField("kv", StringType(), True),
            ]
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0304/raw/royalserv_db/modx_a_order.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("user_fullname")))
            .withColumn("emails", email_udf(col("user_email")))
            .withColumn("phones", phone_udf(col("user_phone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_created"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "order_delivery", from_json(col("order_delivery"), address_json_schema)
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("order_delivery.city"),
                        col("order_delivery.street"),
                        col("order_delivery.house"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_id"),
                    col("order_id"),
                    lit("order_manager"),
                    col("order_manager"),
                    lit("order_cost"),
                    col("order_cost"),
                    lit("order_comment"),
                    col("order_comment"),
                    lit("order_code"),
                    col("order_code"),
                    lit("order_pay"),
                    col("order_pay"),
                ),
            )
            .select("names", "emails", "phones", "address", "actuality", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "emails", "phones"])
        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
