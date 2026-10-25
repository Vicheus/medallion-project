from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    struct,
    udf,
    flatten,
    concat,
    size,
    coalesce,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    sex_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
    birth_date_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from pyspark.sql.types import StringType


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0479"
    validate_invalid_groupping: bool = True

    def parser(self):
        def decode_unicode_escapes(s):
            if s is None:
                return None
            try:
                s = s.replace("\\\\u", "\\u")
                return s.encode("utf-8").decode("unicode_escape")
            except Exception:
                return s

        decode_udf = udf(decode_unicode_escapes, StringType())

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0479/raw/prosushi.ru/Первый.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(decode_udf(col("PS_CUSTOMER_FULL"))))
            .withColumn("sex", sex_udf(decode_udf(col("PS_CUSTOMER_GENDER"))))
            .withColumn(
                "birth_date",
                birth_date_udf(col("PS_CUSTOMER_DATE_OF_BIRTH"), lit("%Y-%m-%d")),
            )
            .withColumn("phones", phone_udf(col("PS_CUSTOMER_PHONE")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("PS_CUSTOMER_DATE_UPDATE"), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select(
                "ID_PS_CUSTOMER", "names", "sex", "birth_date", "phones", "actuality"
            )
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0479/raw/prosushi.ru/Второй.csv",
                sep=",",
                header=True,
            )
            .withColumn("order_phones", phone_udf(col("PS_ORDER_PHONE")))
            .withColumn("address", address_udf(decode_udf(col("PS_ORDER_ADDRESS"))))
            .withColumn("ip_address", ip_address_udf(col("PS_ORDER_IP")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("PS_ORDER_DATETIME"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("PS_ORDER_SUM"),
                    col("PS_ORDER_SUM"),
                    lit("PS_ORDER_COMMENT"),
                    decode_udf(col("PS_ORDER_COMMENT")),
                ),
            )
            .select("ID_PS_CUSTOMER", "order_phones", "address", "ips", "raw_metadata")
        )

        df_orders = (
            df_orders.groupBy(["ID_PS_CUSTOMER"])
            .agg(
                array_compact(array_distinct(collect_set("order_phones"))).alias(
                    "order_phones"
                ),
                array_compact(array_distinct(collect_set("address"))).alias("address"),
                array_compact(array_distinct(collect_set("raw_metadata"))).alias(
                    "raw_metadata"
                ),
                array_compact(array_distinct(flatten(collect_set("ips")))).alias("ips"),
            )
            .select("ID_PS_CUSTOMER", "order_phones", "address", "ips", "raw_metadata")
        )

        df = (
            df_users.join(df_orders, "ID_PS_CUSTOMER", "left")
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        concat(
                            array(col("phones")), coalesce(col("order_phones"), array())
                        )
                    )
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "address",
                "ips",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
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
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn("ips", expr("slice(ips, 1, 20)"))
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 20)"))
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("address").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
