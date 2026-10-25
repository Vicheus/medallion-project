from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    collect_set,
    size,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0642"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0642/raw/rg.ru order - @bereza_bd.csv",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .select("names", "address", "phones", "emails", "raw_metadata", "actuality")
        )

        df = (
            df.groupBy(["names", "emails"])
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
            )
            .select("names", "address", "phones", "emails", "raw_metadata", "actuality")
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
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
