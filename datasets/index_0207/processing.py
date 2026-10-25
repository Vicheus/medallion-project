from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    concat_ws,
    size,
    collect_set,
    array_compact,
    struct,
    lit,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0207"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,address"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0207/raw/kvartelia.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(
                    when(
                        (col("city").isNotNull()) & (col("city") != ""),
                        concat_ws(
                            " ",
                            when(col("address") != "", col("address")).otherwise(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("profile_url").isNotNull() & (col("profile_url") != ""),
                    struct(
                        lit("Kvartelia.ru").alias("title"),
                        col("profile_url").alias("link"),
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "address", "accounts")
        )

        df = df.groupBy(["names", "phones"]).agg(
            array_compact(collect_set(col("address"))).alias("address"),
            array_compact(collect_set(col("accounts"))).alias("accounts"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )
        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
