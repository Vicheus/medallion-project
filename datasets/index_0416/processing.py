from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    size,
    array,
    lit,
    collect_set,
    array_compact,
    array_distinct,
    struct,
    from_unixtime,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0416"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0416/raw/preprocessed/users.csv",
                sep=";",
            )
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone1")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email1")))))
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address1")), address_udf(col("address2"))
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("user_login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Био-фарма").alias("title"),
                            lit("https://biofarma.ru").alias("link"),
                            col("user_login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("last_login"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "user_id",
                "names",
                "phones",
                "emails",
                "address",
                "accounts",
                "actuality",
            )
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0416/raw/preprocessed/orders.csv",
                sep=";",
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("total"),
                    col("total"),
                    lit("subtotal"),
                    col("subtotal"),
                    lit("notes"),
                    col("notes"),
                    lit("timestamp"),
                    col("timestamp"),
                ),
            )
            .select("user_id", "raw_metadata")
        )

        df_orders = df_orders.groupBy(["user_id"]).agg(
            collect_set(col("raw_metadata")).alias("raw_metadata")
        )

        df = df.join(df_orders, on="user_id", how="left").select(
            "names",
            "phones",
            "emails",
            "address",
            "accounts",
            "raw_metadata",
            "actuality",
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "accounts",
            "raw_metadata",
            "actuality",
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
