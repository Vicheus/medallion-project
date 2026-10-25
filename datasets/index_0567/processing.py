from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_list,
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
    dataset_code_name: str = "index_0567"
    validate_invalid_groupping: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0567/raw/topnlab_ru.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("fullname")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("county_name"),
                        col("region_name"),
                        col("city_name"),
                        col("street_name"),
                        col("house"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_call"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df = df.groupBy(["emails", "phones"]).agg(
            array_compact(array_distinct(collect_list(col("names")))).alias("names"),
            array_compact(array_distinct(collect_list(col("address")))).alias(
                "address"
            ),
            array_compact(array_distinct(collect_list(col("raw_metadata")))).alias(
                "raw_metadata"
            ),
            max(col("actuality")).alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
