from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    array_compact,
    size,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0467"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0467/raw/avito.csv",
                sep=",",
                header=True,
            )
            .filter(
                (col("avito_user_name") != "Частное лицо")
                & (col("avito_user_name") != "Частное Объявление")
            )
            .withColumn("names", name_udf(col("avito_user_name")))
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("address", address_udf(col("avito_city")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("avito_user_location"),
                    col("avito_user_location"),
                    lit("avito_ad_title"),
                    col("avito_ad_title"),
                    lit("avito_ad_pdate"),
                    col("avito_ad_pdate"),
                    lit("avito_price"),
                    col("avito_price"),
                ),
            )
            .select("names", "phones", "address", "raw_metadata")
        )

        df = (
            df.groupBy(["phones"])
            .agg(
                collect_set(col("names")).alias("names"),
                collect_set(col("address")).alias("address"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
            .select("names", "phones", "address", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
