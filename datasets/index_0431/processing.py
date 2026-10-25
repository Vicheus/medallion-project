from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    concat_ws,
    concat,
    collect_set,
    flatten,
    max,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    raw_metadata_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0431"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0431/raw/co2-extract.ru - @StormBaseAdapter/Пользователи.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names",
                name_parts_udf(
                    col("customers_firstname"),
                    col("customers_lastname"),
                    col("entry_thirdname"),
                ),
            )
            .withColumn("sex", sex_udf(col("customers_gender")))
            .withColumn("emails1", array(email_udf(col("customers_email_address"))))
            .withColumn("phones1", array(phone_udf(col("customers_telephone"))))
            .withColumn(
                "raw_metadata1",
                array(raw_metadata_udf(lit("customers_notes"), col("customers_notes"))),
            )
            .select(
                "customers_id", "names", "sex", "phones1", "emails1", "raw_metadata1"
            )
        )

        df_users.show(n=20, truncate=False)

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0431/raw/co2-extract.ru - @StormBaseAdapter/Заказы.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("delivery_state"),
                                    col("delivery_city"),
                                    col("delivery_street_address"),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("customers_state"),
                                    col("customers_city"),
                                    col("customers_street_address"),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("billing_state"),
                                    col("billing_city"),
                                    col("billing_street_address"),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn("emails2", email_udf(col("customers_email_address")))
            .withColumn("phones2", phone_udf(col("customers_telephone")))
            .withColumn(
                "raw_metadata2",
                raw_metadata_udf(lit("payment_method"), col("payment_method")),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_modified"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "customers_id",
                "address",
                "phones2",
                "emails2",
                "raw_metadata2",
                "actuality",
            )
        )

        df_orders = (
            df_orders.groupBy(["customers_id"])
            .agg(
                array_compact(flatten(collect_set(col("address")))).alias("address"),
                collect_set(col("phones2")).alias("phones2"),
                collect_set(col("emails2")).alias("emails2"),
                collect_set(col("raw_metadata2")).alias("raw_metadata2"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "customers_id",
                "address",
                "phones2",
                "emails2",
                "raw_metadata2",
                "actuality",
            )
        )

        df_orders.show(n=10, truncate=False)

        df = (
            df_users.join(df_orders, "customers_id", "left")
            .withColumn("emails", array_compact(concat(col("emails1"), col("emails2"))))
            .withColumn("phones", array_compact(concat(col("phones1"), col("phones2"))))
            .withColumn(
                "raw_metadata",
                array_compact(concat(col("raw_metadata1"), col("raw_metadata2"))),
            )
            .select(
                "names",
                "sex",
                "phones",
                "emails",
                "address",
                "raw_metadata",
                "actuality",
            )
        )

        df.show(n=30, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_distinct(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0,
                    array_distinct(array_compact(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0,
                    array_distinct(array_compact(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_distinct(array_compact(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_distinct(array_compact(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
