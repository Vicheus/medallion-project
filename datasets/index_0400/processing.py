from pyspark import StorageLevel

from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import name_parts_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0400"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0400/raw/iw-shop.ru.txt",
                sep=",",
            )
            .withColumn("names", name_parts_udf(col("Имя"), col("Фамилия"), lit(None)))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("ip", ip_address_udf(col("IP")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip").isNotNull(),
                                struct(col("ip").alias("ip"), lit(None).alias("date")),
                            )
                        )
                    )
                ),
            )
            .select("names", "emails", "address", "ips")
        )

        df = df.drop_duplicates(["emails"])

        df.cache()

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
