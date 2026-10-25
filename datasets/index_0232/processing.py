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
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0232"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0232/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("fullname")), name_udf(col("fullname2")))
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("telephone")), phone_udf(col("telephone2")))
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address_1")),
                            address_udf(col("address_2")),
                            address_udf(col("address_3")),
                        )
                    )
                ),
            )
            .withColumn("ip_address_1", ip_address_udf(col("ip")))
            .withColumn("ip_address_2", ip_address_udf(col("forwarded_ip")))
            .withColumn("ip_address_3", ip_address_udf(col("ip2")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address_1").isNotNull(),
                                struct(
                                    col("ip_address_1").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ),
                            when(
                                col("ip_address_2").isNotNull(),
                                struct(
                                    col("ip_address_2").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ),
                            when(
                                col("ip_address_3").isNotNull(),
                                struct(
                                    col("ip_address_3").alias("ip"),
                                    ip_date_udf(
                                        col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(
                                    lit("https://cheryomushki.ru").alias("title"),
                                    col("user_agent").alias("user_agent"),
                                    device_date_udf(
                                        col("date_added"), lit("yyyy-MM-dd HH:mm:ss")
                                    ).alias("date"),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names", "phones", "emails", "address", "ips", "devices", "actuality"
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
        )
        df = df.drop_duplicates(["names", "phones", "emails"])

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
