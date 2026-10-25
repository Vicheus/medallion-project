from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    concat,
    array,
    array_distinct,
    array_compact,
    concat_ws,
    struct,
    coalesce,
    collect_set,
    flatten,
    max,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    address_udf,
    phone_udf,
    raw_metadata_udf,
    actuality_date_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0485"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/dakotadostavka.ru - @StormBaseAdapter.txt",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        when(col("city").isNotNull(), col("city")).otherwise(None),
                        when(col("street").isNotNull(), col("street")).otherwise(None),
                        when(
                            col("house").isNotNull(),
                            concat(lit("д. "), col("house")),
                        ).otherwise(None),
                        when(
                            col("entry").isNotNull(),
                            concat(lit("к. "), col("entry")),
                        ).otherwise(None),
                        when(
                            col("apartments").isNotNull(),
                            concat(lit("кв. "), col("apartments")),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("comment"), col("comment")),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                coalesce(col("date_modified"), col("date_added")),
                                lit("%Y-%m-%d %H:%M:%S"),
                            ).alias("date"),
                        )
                    ),
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
                                coalesce(col("date_modified"), col("date_added")),
                                lit("%Y-%m-%d %H:%M:%S"),
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("date_modified"), col("date_added")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "phones", "ips", "devices", "raw_metadata", "actuality")
        )

        df = (
            df.groupBy([col("phones"), col("names")])
            .agg(
                array_distinct(array_compact(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("devices"))))
                ).alias("devices"),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .select("names", "phones", "ips", "devices", "raw_metadata", "actuality")
        )

        df = (
            df.withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
            .withColumn(
                "devices",
                when(
                    size(array_compact(col("devices"))) > 0,
                    array_compact(col("devices")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
