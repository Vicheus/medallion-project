from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    flatten,
    from_json,
    collect_list,
    collect_set,
    concat,
    from_unixtime,
    explode,
    regexp_replace,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    LongType,
    ArrayType,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.financials.udfs import (
    financial_card_number_udf,
    financial_date_expire_udf,
)
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0237"

    def parser(self):
        schema = StructType(
            [
                StructField("errorCode", StringType(), True),
                StructField("errorMessage", StringType(), True),
                StructField("orderNumber", StringType(), True),
                StructField("orderStatus", IntegerType(), True),
                StructField("actionCode", IntegerType(), True),
                StructField("actionCodeDescription", StringType(), True),
                StructField("amount", IntegerType(), True),
                StructField("currency", StringType(), True),
                StructField("date", LongType(), True),
                StructField("orderDescription", StringType(), True),
                StructField("ip", StringType(), True),
                StructField(
                    "merchantOrderParams",
                    ArrayType(
                        StructType(
                            [
                                StructField("name", StringType(), True),
                                StructField("value", StringType(), True),
                            ]
                        )
                    ),
                    True,
                ),
                StructField(
                    "attributes",
                    ArrayType(
                        StructType(
                            [
                                StructField("name", StringType(), True),
                                StructField("value", StringType(), True),
                            ]
                        )
                    ),
                    True,
                ),
                StructField(
                    "cardAuthInfo",
                    StructType(
                        [
                            StructField("expiration", StringType(), True),
                            StructField("cardholderName", StringType(), True),
                            StructField("approvalCode", StringType(), True),
                            StructField("pan", StringType(), True),
                        ]
                    ),
                    True,
                ),
                StructField("authDateTime", LongType(), True),
                StructField("terminalId", StringType(), True),
                StructField("authRefNum", StringType(), True),
                StructField(
                    "paymentAmountInfo",
                    StructType(
                        [
                            StructField("paymentState", StringType(), True),
                            StructField("approvedAmount", IntegerType(), True),
                            StructField("depositedAmount", IntegerType(), True),
                            StructField("refundedAmount", IntegerType(), True),
                        ]
                    ),
                    True,
                ),
                StructField(
                    "bankInfo",
                    StructType(
                        [
                            StructField("bankName", StringType(), True),
                            StructField("bankCountryCode", StringType(), True),
                            StructField("bankCountryName", StringType(), True),
                        ]
                    ),
                    True,
                ),
            ]
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0237/raw/users_preprocessed.csv",
            sep=";",
            header=True,
        ).withColumn(
            "data",
            from_json(regexp_replace(col("debug_notification"), '""', '"'), schema),
        )

        df = df.withColumn(
            "merchantOrderParam", explode(col("data.merchantOrderParams"))
        ).select(
            "*",
            when(
                col("merchantOrderParam.name") == "sber_safe_email",
                col("merchantOrderParam.value"),
            ).alias("email_merchant"),
            when(
                col("merchantOrderParam.name") == "sber_safe_phone",
                col("merchantOrderParam.value"),
            ).alias("phone_merchant"),
        )

        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("phone_merchant")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email_merchant")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("ip_address", ip_address_udf(col("data.ip")))
            .withColumn("ip_address_date", ip_date_udf(from_unixtime(col("data.date"))))
            .withColumn(
                "card_number", financial_card_number_udf(col("data.cardAuthInfo.pan"))
            )
            .withColumn(
                "card_expiration_date",
                financial_date_expire_udf(
                    concat(
                        col("data.cardAuthInfo.expiration").substr(1, 4),
                        lit("-"),
                        col("data.cardAuthInfo.expiration").substr(5, 2),
                        lit("-01"),
                    )
                ),
            )
            .withColumn("bank_name", col("data.bankInfo.bankName"))
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull() & (col("card_number") != ""),
                    array_compact(
                        array(
                            when(
                                col("card_number").isNotNull(),
                                struct(
                                    col("bank_name").alias("title"),
                                    col("card_number").alias("card_number"),
                                    col("card_expiration_date").alias("date_expire"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            col("ip_address_date").alias("date"),
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "ips", "address", "financials")
        )

        df = df.groupBy(["names"]).agg(
            array_distinct(flatten(collect_list("phones"))).alias("phones"),
            collect_set("emails").alias("emails"),
            collect_set("address").alias("address"),
            array_distinct(flatten(collect_set("ips"))).alias("ips"),
            array_distinct(flatten(collect_set("financials"))).alias("financials"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
