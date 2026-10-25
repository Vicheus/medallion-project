from pyspark.sql.functions import when, col, lit, array, collect_set, first, size
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0050"

    def parser(self):
        schema = StructType(
            [
                StructField("last_name", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("gender", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("email", StringType(), True),
                StructField("address", StringType(), True),
            ]
        )

        df = self.read(path="5ka.csv", sep=",", header=False, schema=schema)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
        )

        df = (
            df.filter(col("names").isNotNull() & col("birth_date").isNotNull())
            .groupby(col("names"), col("birth_date"))
            .agg(
                collect_set("emails").alias("emails"),
                collect_set("phones").alias("phones"),
                collect_set("address").alias("address"),
                first("sex").alias("sex"),
            )
        )

        df = df.select("names", "address", "emails", "phones", "sex", "birth_date")

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
