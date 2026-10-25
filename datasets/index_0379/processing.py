from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0379"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0379/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address1")),
                            address_udf(col("address2")),
                            address_udf(col("address3")),
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
                            ip_date_udf(col("created"), lit("%Y-%m-%d %H:%M:%S")).alias(
                                "date"
                            ),
                        )
                    ),
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    struct(
                        lit("Оформление заказа").alias("action"),
                        col("user_agent").alias("user_agent"),
                        device_date_udf(col("created"), lit("%Y-%m-%d %H:%M:%S")).alias(
                            "date"
                        ),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("company"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "devices",
                "ips",
                "actuality",
            )
        )

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "devices",
                when(col("devices").isNotNull(), array(col("devices"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
