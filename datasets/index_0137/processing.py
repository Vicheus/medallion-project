from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    expr,
    greatest,
    max,
    array_compact,
    flatten,
    size,
    collect_set,
    regexp_replace,
    array_distinct,
    split,
    first,
)

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    address_udf,
    phone_udf,
    email_udf,
    name_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0137"
    validate_invalid_groupping: bool = True

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0137/raw/Vse_Zakazy.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("auto", regexp_replace(col("auto"), "\\\\", ""))
            .withColumn("email", regexp_replace(col("email"), "\\\\", ""))
            .withColumn("name", regexp_replace(col("name"), "\\\\", ""))
            .withColumn("address", regexp_replace(col("address"), "\\\\", ""))
            .withColumn("phone_number", regexp_replace(col("phone_number"), "\\\\", ""))
            .withColumn("lat", split(col("phone_number"), ",")[0])
            .withColumn("long", split(col("phone_number"), ",")[1])
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("phone_number"))))),
            )
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn(
                "coordinates",
                when(
                    (
                        col("long").isNotNull()
                        & (col("long") != 0.0)
                        & col("lat").isNotNull()
                        & (col("lat") != 0.0)
                    ),
                    array(array(col("long").cast("float"), col("lat").cast("float"))),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("auto").isNotNull() & (col("auto") != "")),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("auto"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .where(col("name") != "Akbmoscow")
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created_at"), col("updated_at")),
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
                "emails",
                "phones",
                "address",
                "vehicles",
                "coordinates",
                "actuality",
                "raw_metadata",
            )
        )
        df_1.cache()

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0137/raw/Zakazy.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "order_client_name",
                regexp_replace(col("order_client_name"), "\\\\", ""),
            )
            .withColumn(
                "order_client_email",
                regexp_replace(col("order_client_email"), "\\\\", ""),
            )
            .withColumn(
                "order_client_phone",
                regexp_replace(col("order_client_phone"), "\\\\", ""),
            )
            .withColumn(
                "order_client_phone2",
                regexp_replace(col("order_client_phone2"), "\\\\", ""),
            )
            .withColumn(
                "order_client_address",
                regexp_replace(col("order_client_address"), "\\\\", ""),
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(array(name_udf(col("order_client_name"))))
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(array(email_udf(col("order_client_email"))))
                ),
            )
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
                array_compact(
                    array_distinct(array(address_udf(col("order_client_address"))))
                ),
            )
            .withColumn("coordinates", array())
            .withColumn("vehicles", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_status"),
                    col("order_status"),
                    lit("order_cost_rub"),
                    col("order_cost_rub"),
                    lit("order_client_comment"),
                    regexp_replace(col("order_client_comment"), r"\\", ""),
                ),
            )
            .where(col("order_client_name") != "Akbmoscow")
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "vehicles",
                "coordinates",
                "actuality",
                "raw_metadata",
            )
        )
        df_2.cache()

        df = df_1.unionAll(df_2)

        df = (
            df.groupby(["names", "phones", "emails"])
            .agg(
                flatten(collect_set("address")).alias("address"),
                flatten(collect_set("vehicles")).alias("vehicles"),
                collect_set("raw_metadata").alias("raw_metadata"),
                first(col("coordinates")).alias("coordinates"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array_distinct(array_compact(col("names"))))
            .withColumn("phones", array_distinct(array_compact(col("phones"))))
            .withColumn("vehicles", array_distinct(array_compact(col("vehicles"))))
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "vehicles",
                "coordinates",
                "actuality",
                "raw_metadata",
            )
        )

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
            .withColumn(
                "coordinates",
                when(size(col("coordinates")) > 0, col("coordinates")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
                | col("vehicles").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
