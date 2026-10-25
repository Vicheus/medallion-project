from pyspark.sql.types import StructType, StringType, StructField
from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0060"

    def parser(self):
        schema = StructType(
            [
                StructField("full_name", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("address", StringType(), True),
                StructField("email", StringType(), True),
            ]
        )

        df = self.read(
            path="@StormInDataBase.csv", sep="|", header=False, schema=schema
        )

        df = (
            df.withColumn("names", name_udf(col("full_name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
        )
        df = df.select("names", "emails", "phones", "address", "birth_date")
        df = df.dropDuplicates(["names", "emails", "phones"])

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
