from pyspark.sql.types import StructType, StringType, StructField
from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0055"

    def parser(self):

        schema = StructType(
            [
                StructField("last_name", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("city", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("email", StringType(), True),
            ]
        )
        df = self.read(path="Tinkoff Invest.txt", sep="\t", header=False, schema=schema)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("address", address_udf(col("city")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
        )
        df = df.select("names", "emails", "phones", "address")

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
