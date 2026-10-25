from pyspark.sql.functions import when, col, lit, array
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0062"

    def parser(self):
        schema = StructType(
            [
                StructField("phone", StringType(), True),
                StructField("full_name", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("address", StringType(), True),
                StructField("doc_number", StringType(), True),
                StructField("doc_issue_date", StringType(), True),
                StructField("doc_issued_by", StringType(), True),
            ]
        )
        df = self.read(
            path="beeline2021.txt",
            sep="\t",
            schema=schema,
            header=False,
            encoding="windows-1251",
        )

        df = (
            df.withColumn("names", name_udf(col("full_name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    col("doc_number").isNotNull(),
                    document_udf(
                        lit(None),
                        col("doc_number"),
                        col("doc_issue_date"),
                        lit(None),
                        col("doc_issued_by"),
                        lit(None),
                        lit("%Y-%m-%d"),
                    ),
                ),
            )
        )

        df = df.select("names", "phones", "birth_date", "address", "documents")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(col("documents").isNotNull(), array(col("documents"))).otherwise(
                    None
                ),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
