from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    struct,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0330"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0330/raw/kuking.net.csv",
            sep=",",
            header=True,
        )

        df = (
            df.replace("<blank>", None)
            .replace("NULL", None)
            .filter(~col("email").like("%ukr.net"))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), lit(None)
                            ),
                            name_udf(col("nick_name")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("nick_name").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Kuking.net").alias("title"),
                            lit("https://kuking.net").alias("link"),
                            col("nick_name").alias("login"),
                            col("password").alias("password_hash"),
                            col("id").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn("activation_ip", ip_address_udf(col("activation_ip")))
            .withColumn("registration_ip", ip_address_udf(col("registration_ip")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("activation_ip").isNotNull(),
                                struct(
                                    col("activation_ip").alias("ip"),
                                    ip_date_udf(
                                        col("creation_date"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            ).otherwise(None),
                            when(
                                col("registration_ip").isNotNull(),
                                struct(
                                    col("registration_ip").alias("ip"),
                                    ip_date_udf(
                                        col("registration_date"),
                                        lit("%Y-%m-%d %H:%M:%S"),
                                    ).alias("date"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("last_visit"),
                        col("change_date"),
                        col("creation_date"),
                        col("registration_date"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "emails", "ips", "accounts", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
