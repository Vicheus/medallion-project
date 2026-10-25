from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
    size,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0633"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0633/raw/caraks.ru - @bd_bereza/orders - @bd_bereza.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("address", address_udf(col("Address")))
            .select("names", "emails", "phones", "address")
        )

        df_with_phones = df.filter(col("phones").isNotNull())
        df_without_phones = (
            df.filter(col("phones").isNull())
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .select("names", "phones", "emails", "address")
        )

        df_with_phones = (
            df_with_phones.groupBy(["phones"])
            .agg(
                array_compact(array_distinct(collect_list(col("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_list(col("address")))).alias(
                    "address"
                ),
            )
            .select("names", "phones", "emails", "address")
        )

        df = df_with_phones.unionAll(df_without_phones)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
