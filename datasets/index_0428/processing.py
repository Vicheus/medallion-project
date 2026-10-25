from pyspark import StorageLevel
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    col,
    collect_set,
    concat_ws,
    expr,
    from_unixtime,
    lit,
    max,
    size,
    when,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    address_udf,
    email_udf,
    name_parts_udf,
    phone_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0428"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0428/raw/mm.ru - @StormBaseAdapter.csv",
                sep=",",
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("customer_firstName"),
                    col("customer_lastName"),
                    col("customer_patronymic"),
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(" ", col("delivery_address"), col("delivery_apartment"))
                ),
            )
            .withColumn("phones", phone_udf(col("customer_phone")))
            .withColumn("emails", email_udf(col("customer_email")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("delivery_deliveryComment"),
                    col("delivery_deliveryComment"),
                    lit("delivery_timeFrom"),
                    col("delivery_timeFrom"),
                    lit("delivery_timeTo"),
                    col("delivery_timeTo"),
                    lit("delivery_date"),
                    from_unixtime((col("dateCreated") / 1000), "yyyy-MM-dd HH:mm:ss"),
                    lit("barcode"),
                    col("barcode"),
                    lit("price"),
                    col("price"),
                    lit("platform"),
                    col("platform"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime((col("dateCreated") / 1000), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df_with_phone = (
            df.filter(col("phones").isNotNull() & (col("phones") != ""))
            .groupBy(["phones", "names"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df_without_phone = (
            df.filter(col("phones").isNull() | (col("phones") == ""))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df = df_with_phone.unionAll(df_without_phone)

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
        )
        df = df.select(
            "names", "emails", "phones", "address", "raw_metadata", "actuality"
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
