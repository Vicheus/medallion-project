from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    concat_ws,
    array,
    max,
    array_distinct,
    array_compact,
    flatten,
    struct,
    collect_list,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0175"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0175/raw/preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fullname")))
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(
                        array(
                            email_udf(col("customers_email_address")),
                            email_udf(col("email2")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("customers_telephone")),
                            phone_udf(col("phone2")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(col("address2")),
                            address_udf(
                                when(
                                    col("street").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("postcode") != "", col("postcode")
                                        ).otherwise(None),
                                        when(col("city") != "", col("city")).otherwise(
                                            None
                                        ),
                                        col("street"),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("customers_id").isNotNull()
                    & col("customers_password").isNotNull(),
                    array(
                        struct(
                            lit("Hairpersona.ru").alias("title"),
                            lit("https://www.hairpersona.ru").alias("link"),
                            col("customers_id").alias("id"),
                            col("customers_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(col("ip_date")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("ip_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "customers_id",
                "names",
                "emails",
                "address",
                "phones",
                "ips",
                "accounts",
                "actuality",
            )
        )

        df = (
            df.groupBy(["customers_id", "names", "phones"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("ips")))).alias(
                    "ips"
                ),
                array_compact(array_distinct(flatten(collect_list("accounts")))).alias(
                    "accounts"
                ),
                max("actuality").alias("actuality"),
            )
            .select(
                "names", "emails", "phones", "ips", "address", "accounts", "actuality"
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
