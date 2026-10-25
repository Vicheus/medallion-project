from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0233"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0233/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("_billing_first_name"), col("_billing_last_name"), lit(None)
                ),
            )
            .withColumn("emails", email_udf(col("_billing_email")))
            .withColumn("phones", phone_udf(col("_billing_phone")))
            .withColumn("address", address_udf(col("_billing_address_1")))
            .withColumn("ip_address", ip_address_udf(col("_customer_ip_address")))
            .withColumn(
                "devices",
                when(
                    col("_customer_user_agent").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("_customer_user_agent").alias("user_agent"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array_compact(array(struct(col("ip_address").alias("ip")))),
                ),
            )
            .select("names", "emails", "phones", "address", "ips", "devices")
        )

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
