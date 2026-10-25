from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    regexp_replace,
    struct,
    collect_set,
    flatten,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    address_udf,
    phone_udf,
    raw_metadata_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0486"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/mcvita.ru - @StormBaseAdapter/Клиенты.txt",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone1")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment1"),
                    col("comment1"),
                    lit("comment2"),
                    col("comment2"),
                    lit("comment3"),
                    col("comment3"),
                    lit("birth_year"),
                    col("birth_year"),
                    lit("height"),
                    col("height"),
                    lit("weight"),
                    col("weight"),
                    lit("source"),
                    col("source"),
                ),
            )
            .withColumn(
                "ip_address",
                ip_address_udf(
                    regexp_replace(regexp_replace(col("ip"), "ip:", ""), '"', "")
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ),
            )
            .select("names", "phones", "address", "ips", "raw_metadata")
        )

        df = (
            df.groupBy([col("phones"), col("names")])
            .agg(
                array_distinct(array_compact(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_distinct(array_compact(collect_set(col("address")))).alias(
                    "address"
                ),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .filter(col("names") != "Иванов Иван")
            .select("names", "phones", "address", "ips", "raw_metadata")
        )

        df = (
            df.withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
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

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
