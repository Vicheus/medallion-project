from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    struct,
    lit,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0388"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0388/raw/users_preprocessed.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email1")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("customer_phone"))))),
            )
            .withColumn("ip", ip_address_udf(col("last_ip")))
            .withColumn(
                "accounts",
                array(
                    when(
                        col("login").isNotNull() & col("password").isNotNull(),
                        struct(
                            lit("Эролайф").alias("title"),
                            lit("https://erolaif.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                            col("discont_card").alias("client_card_number"),
                        ),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("logdate"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip").isNotNull(),
                                struct(
                                    col("ip").alias("ip"),
                                    ip_date_udf(
                                        col("logdate"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .select(
                "names", "ips", "emails", "phones", "address", "accounts", "actuality"
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
