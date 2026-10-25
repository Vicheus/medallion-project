from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
    flatten,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf, email_udf
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0576"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0576/raw/Scardio.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fullname_ru")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address_ru")))
            .withColumn(
                "works",
                when(
                    col("job_title").isNotNull() | col("employer").isNotNull(),
                    array(
                        work_udf(
                            col("job_title"),
                            lit(None),
                            lit(None),
                            col("employer"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "address", "works")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_distinct(array_compact(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_distinct(array_compact(collect_list(col("address")))).alias(
                    "address"
                ),
                array_distinct(
                    array_compact(flatten(collect_list(col("works"))))
                ).alias("works"),
            )
            .select("names", "phones", "emails", "address", "works")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "works",
                when(size(col("works")) > 0, col("works")).otherwise(None),
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
