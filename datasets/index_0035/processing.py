from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    coalesce,
    max,
    concat,
    struct,
    collect_set,
    size,
    array_compact,
    array_distinct,
    flatten,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
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
    dataset_code_name: str = "index_0035"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0035/raw/DeliveryClub_2022_2,2kk.json",
            header=False,
        )

        df = (
            df.withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        when(
                            col("data.customer.address.city.title").isNotNull(),
                            col("data.customer.address.city.title"),
                        ).otherwise(None),
                        when(
                            col("data.customer.address.street").isNotNull(),
                            col("data.customer.address.street"),
                        ).otherwise(None),
                        when(
                            col("data.customer.address.building").isNotNull(),
                            concat(lit("д. "), col("data.customer.address.building")),
                        ).otherwise(None),
                        when(
                            col("data.customer.address.entrance").isNotNull(),
                            concat(lit("под. "), col("data.customer.address.entrance")),
                        ).otherwise(None),
                        when(
                            col("data.customer.address.floor").isNotNull(),
                            concat(lit("эт. "), col("data.customer.address.floor")),
                        ).otherwise(None),
                        when(
                            col("data.customer.address.flatNumber").isNotNull(),
                            concat(
                                lit("кв. "), col("data.customer.address.flatNumber")
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("names", name_udf(col("data.customer.name")))
            .withColumn("phones", phone_udf(col("data.customer.phone")))
            .withColumn("emails", email_udf(col("data.customer.email")))
            .withColumn(
                "accounts",
                when(
                    col("data.customer.id").isNotNull()
                    & (col("data.customer.id") != 0),
                    array(
                        struct(
                            lit("Delivery club").alias("title"),
                            lit("https://delivery-club.ru").alias("link"),
                            col("data.customer.id").cast("string").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("data.customer.address.ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("data.customer.address.ip")).alias("ip"),
                            ip_date_udf(col("data.createdAt")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("data.createdAt"), col("data.updatedAt")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("orderCode"),
                    df["data.orderCode"],
                    lit("orderStatus"),
                    df["data.orderStatus"],
                    lit("paymentType"),
                    df["data.paymentType"],
                    lit("personCount"),
                    df["data.personCount"],
                    lit("price"),
                    df["data.price"],
                    lit("products"),
                    df["data.products"],
                ),
            )
        )

        df_registered_customers = (
            df.filter(col("accounts").isNotNull())
            .groupby(col("accounts")[0]["id"], "phones")
            .agg(
                collect_set("names").alias("names"),
                when(size(collect_set("address")) > 0, collect_set("address"))
                .otherwise(None)
                .alias("address"),
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
                when(
                    size(array_compact(array_distinct(flatten(collect_list("ips")))))
                    > 0,
                    array_compact(array_distinct(flatten(collect_list("ips")))),
                )
                .otherwise(None)
                .alias("ips"),
                when(
                    size(
                        array_compact(array_distinct(flatten(collect_list("accounts"))))
                    )
                    > 0,
                    array_compact(array_distinct(flatten(collect_list("accounts")))),
                )
                .otherwise(None)
                .alias("accounts"),
                max("actuality").alias("actuality"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
        )
        df_registered_customers = df_registered_customers.withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df_registered_customers = df_registered_customers.select(
            "names",
            "emails",
            "phones",
            "address",
            "ips",
            "accounts",
            "actuality",
            "raw_metadata",
        )

        df_not_registered_customers = (
            df.filter(col("accounts").isNull())
            .withColumn(
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
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df_not_registered_customers = df_not_registered_customers.select(
            "names",
            "emails",
            "phones",
            "address",
            "ips",
            "accounts",
            "actuality",
            "raw_metadata",
        )

        df = df_registered_customers.unionAll(df_not_registered_customers)

        df = df.filter(
            col("names").isNotNull()
            & (size(col("names")) > 0)
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
