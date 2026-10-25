from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0364"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0364/raw/клиенты_smarthome_rt_ru_12_2021.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("ip1", ip_address_udf(col("IP текущей авторизации")))
            .withColumn("ip2", ip_address_udf(col("IP последней авторизации")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip1").isNotNull(),
                                struct(col("ip1").alias("ip"), lit(None).alias("date")),
                            ),
                            when(
                                col("ip2").isNotNull(),
                                struct(col("ip2").alias("ip"), lit(None).alias("date")),
                            ),
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "ips")
        )

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
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
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
