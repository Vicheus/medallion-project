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
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0155"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0155/raw/igis_ru.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .replace("<blank>", None)
            .withColumn("names", name_parts_udf(col("I"), col("F"), col("O")))
            .withColumn("phones", phone_udf(col("Tel")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "login_date", from_unixtime(col("DateLogin"), "yyyy-MM-dd HH:mm:ss")
            )
            .withColumn(
                "date_add", from_unixtime(col("DateAdd"), "yyyy-MM-dd HH:mm:ss")
            )
            .withColumn(
                "old_ip_date", from_unixtime(col("OldDate"), "yyyy-MM-dd HH:mm:ss")
            )
            .withColumn("ip", ip_address_udf(col("IP")))
            .withColumn("ip_old", ip_address_udf(col("OldIP")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull() | col("ip_old").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                when(
                                    col("ip").isNotNull(),
                                    struct(
                                        col("ip").alias("ip"),
                                        ip_date_udf(col("login_date")).alias("date"),
                                    ),
                                ),
                                when(
                                    col("ip_old").isNotNull(),
                                    struct(
                                        col("ip_old").alias("ip"),
                                        ip_date_udf(col("old_ip_date")).alias("date"),
                                    ),
                                ),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("Pass").isNotNull() & col("Nickname").isNotNull(),
                    array(
                        struct(
                            lit("IGIS").alias("title"),
                            lit("https://igis.ru/").alias("link"),
                            col("Nickname").alias("login"),
                            col("Pass").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("date_add"), col("date_add")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("names", "phones", "emails", "ips", "accounts", "actuality")
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()

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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
