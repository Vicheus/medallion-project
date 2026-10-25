from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    concat,
    array_distinct,
    array_compact,
    struct,
    regexp_replace,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    name_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    name_parts_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0101"

    def parser(self):
        df_ms_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0101/raw/akbru/al_ms_orders.csv",
            sep=",",
            header=True,
        )
        df_ms_order = (
            df_ms_orders.replace("<blank>", None)
            .replace("NULL", None)
            .withColumn("names", name_udf(regexp_replace(col("name"), r"\\", "")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("phone_number"))))),
            )
            .withColumn(
                "address", address_udf(regexp_replace(col("address"), r"\\", ""))
            )
            .withColumn("sex", lit(None))
            .withColumn(
                "vehicles",
                when(
                    (col("auto").isNotNull()),
                    vehicle_udf(
                        lit(1),
                        regexp_replace(col("auto"), r"\\", ""),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn("accounts", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("created_at"), col("updated_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("google_id"),
                    col("google_id"),
                    lit("yandex_id"),
                    col("yandex_id"),
                    lit("sms_status"),
                    regexp_replace(col("sms_status"), r"\\", ""),
                    lit("utilization"),
                    regexp_replace(col("utilization"), r"\\", ""),
                    lit("order_number"),
                    regexp_replace(col("order_number"), r"\\", ""),
                    lit("description"),
                    regexp_replace(col("description"), r"\\", ""),
                    lit("delivery_cost"),
                    regexp_replace(col("delivery_cost"), r"\\", ""),
                    lit("address_coords"),
                    col("address_coords"),
                    lit("delivery_planned_moment"),
                    col("delivery_planned_moment"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "accounts",
                "vehicles",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

        df_mod_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0101/raw/akbru/mod_order.csv",
            sep=",",
            header=True,
        )
        df_mod_orders = (
            df_mod_orders.replace("<blank>", None)
            .replace("NULL", None)
            .withColumn(
                "names", name_udf(regexp_replace(col("order_client_name"), r"\\", ""))
            )
            .withColumn("emails", email_udf(col("order_client_email")))
            .withColumn("sex", lit(None))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("order_client_phone")),
                            phone_udf(col("order_client_phone2")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(regexp_replace(col("order_client_address"), r"\\", "")),
            )
            .withColumn("vehicles", lit(None))
            .withColumn("accounts", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_date"),
                    col("order_date"),
                    lit("order_cost_rub"),
                    col("order_cost_rub"),
                    lit("order_client_comment"),
                    regexp_replace(col("order_client_comment"), r"\\", ""),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "accounts",
                "vehicles",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

        df_mod_user = self.read(
            path="/media/user/SAMSUNG/Databases/index_0101/raw/akbru/mod_user.csv",
            sep=",",
            header=True,
        )
        df_mod_user = (
            df_mod_user.replace("<blank>", None)
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("user_firstname"), col("user_lastname"), lit("")),
            )
            .withColumn("emails", email_udf(col("user_email")))
            .withColumn("sex", sex_udf(col("user_sex")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("user_phone_home")),
                            phone_udf(col("user_phone_work")),
                            phone_udf(col("user_phone_mobile")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    when(
                        col("user_town").isNotNull(),
                        concat_ws(
                            ", ",
                            regexp_replace(col("user_town"), r"\\", ""),
                            when(
                                col("user_postcode") != "",
                                regexp_replace(col("user_postcode"), r"\\", ""),
                            ).otherwise(None),
                            when(
                                col("user_street") != "",
                                concat(
                                    lit("ул. "),
                                    regexp_replace(col("user_street"), r"\\", ""),
                                ),
                            ).otherwise(None),
                            when(
                                col("user_house") != "",
                                concat(
                                    lit("д. "),
                                    regexp_replace(col("user_house"), r"\\", ""),
                                ),
                            ).otherwise(None),
                            when(
                                col("user_apartment") != "",
                                concat(
                                    lit("кв. "),
                                    regexp_replace(col("user_apartment"), r"\\", ""),
                                ),
                            ).otherwise(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn("vehicles", lit(None))
            .withColumn(
                "accounts",
                when(
                    col("user_login").isNotNull(),
                    array(
                        struct(
                            lit("AKB.ru").alias("title"),
                            lit("https://akb.ru").alias("link"),
                            col("user_id").alias("id"),
                            col("user_login").alias("login"),
                            col("user_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "accounts",
                "vehicles",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

        df = (
            df_ms_order.unionAll(df_mod_user)
            .unionAll(df_mod_orders)
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "accounts",
                "vehicles",
                "sex",
                "actuality",
                "raw_metadata",
            )
        )

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(col("vehicles").isNotNull(), array(col("vehicles"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "accounts",
            "vehicles",
            "sex",
            "actuality",
            "raw_metadata",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("vehicles").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
