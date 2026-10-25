from pyspark.sql.functions import when, col, array, array_compact, from_json
from pyspark.sql.types import (
    StringType,
    StructType,
    StructField,
    ArrayType,
    BooleanType,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0178"

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("name", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("email", StringType(), True),
                StructField("roles", StringType(), True),
                StructField("status", StringType(), True),
                StructField("hasCard", BooleanType(), True),
                StructField(
                    "organizations",
                    ArrayType(
                        StructType(
                            [
                                StructField("id", StringType(), True),
                                StructField("name", StringType(), True),
                            ]
                        )
                    ),
                    True,
                ),
                StructField("blocked", BooleanType(), True),
                StructField(
                    "operationAreas",
                    ArrayType(
                        StructType(
                            [
                                StructField("id", StringType(), True),
                                StructField("name", StringType(), True),
                            ]
                        )
                    ),
                    True,
                ),
            ]
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0178/raw/whoosh/whoosh.txt",
                sep="\n",
                header=False,
            )
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("names", name_udf(col("data.name")))
            .withColumn("emails", email_udf(col("data.email")))
            .withColumn("phones", phone_udf(col("data.phone")))
            .select("names", "phones", "emails")
            .drop_duplicates()
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
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
