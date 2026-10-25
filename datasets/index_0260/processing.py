from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    regexp_replace,
    collect_set,
    array_compact,
    array_distinct,
)
from pyspark.sql.types import StringType, StructField, StructType

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0260"
    validate_invalid_groupping: bool = True

    def parser(self):
        schema = StructType(
            [
                StructField("name", StringType(), True),
                StructField("email", StringType(), True),
                StructField("phone", StringType(), True),
            ]
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0260/raw/1click_ru.csv",
                sep="|",
                header=False,
                schema=schema,
            )
            .withColumn("names", name_udf(regexp_replace(col("name"), r"\.|-", "")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "emails", "phones")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df_without_phone = df.filter(col("phones").isNull()).withColumn(
            "emails", array_compact(array_distinct(array(col("emails"))))
        )

        df_with_phone = df.filter(col("phones").isNotNull())
        df_with_phone = (
            df_with_phone.groupby(["names", "phones"])
            .agg(collect_set("emails").alias("emails"))
            .select("names", "emails", "phones")
        )

        df = df_with_phone.unionAll(df_without_phone)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
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
