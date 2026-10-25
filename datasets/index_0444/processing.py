from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, size

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    raw_metadata_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0444"

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/new/maxxi-cafe.ru/maxxi-cafe.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("adress")))
            .withColumn("ip", ip_address_udf(col("ipadress")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn(
                "ips", when(col("ip").isNotNull(), array(struct(col("ip").alias("ip"))))
            )
            .select("names", "phones", "ips", "address", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
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
