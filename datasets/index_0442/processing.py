from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    size,
    collect_set,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0442"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0442/raw/weltrade.ru.csv",
            sep=";",
            header=True,
        )

        df = df.filter(
            (~col("Phone").startswith("38"))
            & (~col("Phone").startswith("80"))
            & (~col("Phone").startswith("+3"))
        )

        df = (
            df.withColumn("names", name_udf(col("Name")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("address", address_udf(col("City")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Comment"), col("Comment"), lit("Balance"), col("Balance")
                ),
            )
            .select("names", "emails", "phones", "address", "raw_metadata")
        )

        df = df.groupBy(["names", "emails", "phones"]).agg(
            array_compact(array_distinct(collect_set(col("address")))).alias("address"),
            array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                "raw_metadata"
            ),
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
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
