from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    split,
    struct,
    array_compact,
    array_distinct,
    collect_set,
    flatten,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0501"
    output_file_count: int = 50
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0501/raw/s7ru/*.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("CARDHOLDER")))
            .withColumn(
                "ip",
                when(
                    size(split(col("ORDERDESCRIPTION"), ",")) == 16,
                    split(col("ORDERDESCRIPTION"), ",").getItem(1),
                ).otherwise(lit(None)),
            )
            .withColumn(
                "phone",
                when(
                    size(split(col("ORDERDESCRIPTION"), ",")) == 16,
                    split(col("ORDERDESCRIPTION"), ",").getItem(8),
                ).otherwise(
                    when(
                        size(split(col("ORDERDESCRIPTION"), ",")) == 13,
                        split(col("ORDERDESCRIPTION"), ",").getItem(5),
                    ).otherwise(lit(None))
                ),
            )
            .withColumn(
                "email",
                when(
                    size(split(col("ORDERDESCRIPTION"), ",")) == 16,
                    split(col("ORDERDESCRIPTION"), ",").getItem(9),
                ).otherwise(
                    when(
                        size(split(col("ORDERDESCRIPTION"), ",")) == 13,
                        split(col("ORDERDESCRIPTION"), ",").getItem(6),
                    ).otherwise(lit(None))
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("TRANS_DATE"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "financials",
                when(
                    col("MASK_PAN").isNotNull(),
                    array(
                        struct(
                            lit("BANK_NAME").alias("title"),
                            col("MASK_PAN").alias("card_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("AMOUNT"),
                    col("AMOUNT"),
                    lit("DEPOSITEDAMOUNT"),
                    col("DEPOSITEDAMOUNT"),
                    lit("LEAD_PAX_NAME"),
                    col("LEAD_PAX_NAME"),
                    lit("ROUTE"),
                    col("ROUTE"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("TRANS_DATE"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df_with_phone = (
            df.filter(col("phones").isNotNull())
            .groupBy(["names", "phones"])
            .agg(
                array_distinct(array_compact(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_distinct(array_compact(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("financials"))))
                ).alias("financials"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df_without_phone = (
            df.filter(col("phones").isNull())
            .drop_duplicates(["names"])
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_with_phone.unionAll(df_without_phone).select(
            "names",
            "emails",
            "phones",
            "ips",
            "financials",
            "raw_metadata",
            "actuality",
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("financials").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
