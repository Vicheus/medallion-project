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
    flatten,
    collect_set,
    array_union,
    first,
    max,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0212"
    output_file_count: 3

    def parser(self):
        df_ips = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0212/raw/preprocessed/ips_users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips1",
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
            .select("customer_id", "ips1")
        )
        df_ips = (
            df_ips.groupBy(["customer_id"])
            .agg(array_distinct(flatten(collect_set("ips1"))).alias("ips1"))
            .select("customer_id", "ips1")
            .coalesce(3)
        )

        df_registered = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0212/raw/preprocessed/registered_users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .join(df_ips, "customer_id", "left")
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("name_1")),
                            name_udf(col("name_2")),
                            name_udf(col("name_3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email_1")),
                            email_udf(col("email_2")),
                            email_udf(col("email_3")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("telephone_1")),
                            phone_udf(col("telephone_2")),
                            phone_udf(col("telephone_3")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d %m %Y")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address_1")), address_udf(col("address_2"))
                        )
                    )
                ),
            )
            .withColumn("ip_address_1", ip_address_udf(col("ip_1")))
            .withColumn("ip_address_2", ip_address_udf(col("ip_2")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array_union(
                            array(
                                when(
                                    col("ip_address_1").isNotNull(),
                                    struct(
                                        col("ip_address_1").alias("ip"),
                                        ip_date_udf(
                                            col("date_added_1"),
                                            lit("%Y-%m-%d %H:%M:%S"),
                                        ).alias("date"),
                                    ),
                                ),
                                when(
                                    col("ip_address_2").isNotNull(),
                                    struct(
                                        col("ip_address_2").alias("ip"),
                                        ip_date_udf(
                                            col("date_added_2"),
                                            lit("%Y-%m-%d %H:%M:%S"),
                                        ).alias("date"),
                                    ),
                                ),
                            ),
                            col("ips1"),
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
                                col("date_added_2"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("date_added_1"), col("date_added_2")),
                    lit("%Y-%m-%d %H:%M:%S"),
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
                "birth_date",
                "actuality",
            )
            .coalesce(3)
        )

        df_registered = (
            df_registered.groupBy(["customer_id"])
            .agg(
                array_distinct(flatten(collect_set("names"))).alias("names"),
                array_distinct(flatten(collect_set("emails"))).alias("emails"),
                array_distinct(flatten(collect_set("phones"))).alias("phones"),
                array_distinct(flatten(collect_set("ips"))).alias("ips"),
                array_distinct(flatten(collect_set("devices"))).alias("devices"),
                array_distinct(flatten(collect_set("address"))).alias("address"),
                first("birth_date").alias("birth_date"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "birth_date",
                "actuality",
            )
        )

        df_not_registered = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0212/raw/preprocessed/not_registered_users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("telephone"))))),
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
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
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "birth_date",
                "actuality",
            )
        )

        df_not_registered = (
            df_not_registered.groupBy(["names", "phones"])
            .agg(
                array_distinct(flatten(collect_set("emails"))).alias("emails"),
                array_distinct(flatten(collect_set("ips"))).alias("ips"),
                array_distinct(flatten(collect_set("devices"))).alias("devices"),
                array_distinct(flatten(collect_set("address"))).alias("address"),
                first("birth_date").alias("birth_date"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "devices",
                "address",
                "birth_date",
                "actuality",
            )
            .coalesce(3)
        )

        df = df_registered.unionAll(df_not_registered)

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

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
