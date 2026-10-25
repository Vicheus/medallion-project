from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    concat_ws,
    concat,
    max,
    size,
    array_distinct,
    flatten,
    collect_list,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)
from parsetron.sections.device.udfs import device_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 5
    dataset_code_name: str = "index_0015"
    calc_completeness: bool = False

    def parser(self):
        df_with_address = self.read(
            path="/media/user/SAMSUNG/Databases/index_0015/raw/eda.yandex.ru CSV/*.csv",
            sep=",",
        )

        # filter out users with invalid ids
        df_with_address = df_with_address.filter(col("id").rlike("^[0-9]+$")).filter(
            col("user_id").isNotNull()
        )

        df_with_address = (
            df_with_address.withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        when(
                            col("address_city").isNotNull(), col("address_city")
                        ).otherwise(None),
                        when(
                            col("address_street").isNotNull(), col("address_street")
                        ).otherwise(None),
                        when(
                            col("address_house").isNotNull(),
                            concat(lit("д. "), col("address_house")),
                        ).otherwise(None),
                        when(
                            col("address_entrance").isNotNull(),
                            concat(lit("под. "), col("address_entrance")),
                        ).otherwise(None),
                        when(
                            col("address_floor").isNotNull(),
                            concat(lit("эт. "), col("address_floor")),
                        ).otherwise(None),
                        when(
                            col("address_office").isNotNull(),
                            concat(lit("оф. "), col("address_office")),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "names",
                when(
                    col("full_name").isNotNull(), name_udf(col("full_name"))
                ).otherwise(name_udf(col("first_name"))),
            )
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("user_agent").alias("user_agent"),
                            device_date_udf(col("created_at")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("user_id").isNotNull(),
                    array(
                        struct(
                            lit("Яндекс еда").alias("title"),
                            lit("https://eda.yandex.ru").alias("link"),
                            col("user_id").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%dT%H:%M:%S.%fZ")),
            )
        )

        df_with_address = df_with_address.select(
            "user_id",
            "names",
            "phones",
            "emails",
            "address",
            "devices",
            "accounts",
            "actuality",
        )

        df_with_address = (
            df_with_address.groupby(["names", "phones"])
            .agg(
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
                when(size(collect_set("address")) > 0, collect_set("address"))
                .otherwise(None)
                .alias("address"),
                when(
                    size(array_distinct(flatten(collect_list("devices")))) > 0,
                    array_distinct(flatten(collect_list("devices"))),
                )
                .otherwise(None)
                .alias("devices"),
                when(
                    size(array_distinct(flatten(collect_list("accounts")))) > 0,
                    array_distinct(flatten(collect_list("accounts"))),
                )
                .otherwise(None)
                .alias("accounts"),
                max(col("actuality")).alias("actuality"),
            )
            .drop("user_id")
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df_with_address.persist(StorageLevel.DISK_ONLY).count()

        df_without_address = self.read(
            path="/media/user/SAMSUNG/Databases/index_0015/raw/eda.yandex.ru CSV/no-address/*.csv",
            sep=",",
            header=True,
        )

        df_without_address = df_without_address.dropDuplicates(
            subset=["full_name", "phone_number", "email"]
        )

        df_without_address = (
            df_without_address.withColumn("names", name_udf(col("full_name")))
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull(),
                    array(
                        struct(
                            lit("Яндекс еда").alias("title"),
                            lit("https://eda.yandex.ru").alias("link"),
                            col("id").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("address", lit(None))
            .withColumn("devices", lit(None))
            .withColumn("actuality", lit(None))
        )

        df_without_address = df_without_address.filter(col("names").isNotNull())
        df_without_address = df_without_address.filter(
            col("phones").isNotNull() | col("emails").isNotNull()
        )

        df_without_address = df_without_address.select(
            "names", "phones", "emails", "address", "devices", "accounts", "actuality"
        )
        df_without_address.persist(StorageLevel.DISK_ONLY).count()

        df_without_address = (
            df_without_address.withColumn(
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
        )

        df = df_with_address.union(df_without_address)

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("devices").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
