from pyspark import StorageLevel
from pyspark.sql.functions import col, lit, collect_set, when, size, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0201"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0201/raw/preprocessed/barahla_net_2025_users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date", birth_date_udf(col("birthdate"), lit('"%m/%d/%Y"'))
            )
            .withColumn("address", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select("names", "phones", "birth_date", "address", "raw_metadata")
        )

        df_geo = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0201/raw/preprocessed/barahla_net_2025_geo.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date", birth_date_udf(col("birthdate"), lit('"%m/%d/%Y"'))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("operator"), col("operator"))
            )
            .select("names", "phones", "birth_date", "address", "raw_metadata")
        )

        df = df_users.unionAll(df_geo)

        df = (
            df.groupBy(["names", "phones", "birth_date"])
            .agg(
                collect_set("address").alias("address"),
                collect_set("raw_metadata").alias("raw_metadata"),
            )
            .select("names", "phones", "birth_date", "address", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .select("names", "phones", "birth_date", "address", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
