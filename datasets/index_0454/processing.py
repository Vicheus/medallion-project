from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    concat_ws,
    lit,
    struct,
    array_compact,
    array_distinct,
    greatest,
    collect_set,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0454"

    def parser(self):
        df_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0454/raw/customers.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), lit(None)
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "accounts",
                when(
                    col("user_name").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit(
                                "Mimigram - лучшее приложение для печати фотографий"
                            ).alias("title"),
                            lit("https://mimigram.ru").alias("link"),
                            col("user_name").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vkontakte_id").isNotNull()
                    | col("facebook_id").isNotNull()
                    | col("odnoklassniki_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vkontakte_id").isNotNull()
                                & (col("vkontakte_id") != ""),
                                social_udf(
                                    lit("Vk"), col("vkontakte_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull()
                                & (col("facebook_id") != ""),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("odnoklassniki_id").isNotNull()
                                & (col("odnoklassniki_id") != ""),
                                social_udf(
                                    lit("Ok"),
                                    col("odnoklassniki_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created_at"), col("updated_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("phones", array())
            .withColumn("address", array())
            .withColumn("raw_metadata", array())
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_customer_addresses = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0454/raw/customers_address.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("customer_first_name"), col("customer_last_name"), lit(None)
                ),
            )
            .withColumn("phones", phone_udf(col("customer_phone_number")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("post_code"),
                        col("delivery_status_city"),
                        col("street"),
                        col("house"),
                        col("flat"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("cash_on_delivery_fact"),
                    col("cash_on_delivery_fact"),
                    lit("delivery_price"),
                    col("delivery_price"),
                    lit("delivery_substatus_description"),
                    col("delivery_substatus_description"),
                    lit("delivery_status_date"),
                    col("delivery_status_date"),
                    lit("delivery_dispatch_number"),
                    col("delivery_dispatch_number"),
                ),
            )
            .select("customer_id", "names", "phones", "address", "raw_metadata")
        )

        df_customer_addresses = (
            df_customer_addresses.groupBy(["customer_id"])
            .agg(
                array_compact(array_distinct(collect_set(col("names")))).alias("names"),
                array_compact(array_distinct(collect_set(col("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .withColumn("emails", array())
            .withColumn("accounts", array())
            .withColumn("socials", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_customers.unionAll(df_customer_addresses)

        df = df.drop_duplicates(["names", "phones", "emails"])

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
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
