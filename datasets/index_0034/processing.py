from pyspark.sql.functions import when, col, lit, array, struct
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0034"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails"
    calc_completeness: bool = False

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), nullable=True),
                StructField("username", StringType(), nullable=True),
                StructField("phone", StringType(), nullable=True),
                StructField("email", StringType(), nullable=True),
                StructField("name", StringType(), nullable=True),
                StructField("unknown_field_1", IntegerType(), nullable=True),
                StructField("unknown_field_2", StringType(), nullable=True),
                StructField("unknown_field_3", StringType(), nullable=True),
                StructField("unknown_field_4", StringType(), nullable=True),
                StructField("unknown_field_5", StringType(), nullable=True),
                StructField("unknown_field_6", StringType(), nullable=True),
                StructField("unknown_field_7", StringType(), nullable=True),
                StructField("unknown_field_8", IntegerType(), nullable=True),
                StructField("unknown_field_9", StringType(), nullable=True),
                StructField("unknown_field_10", StringType(), nullable=True),
                StructField("unknown_field_11", StringType(), nullable=True),
                StructField("unknown_field_12", IntegerType(), nullable=True),
                StructField("unknown_field_13", StringType(), nullable=True),
                StructField("unknown_field_14", StringType(), nullable=True),
                StructField("unknown_field_15", IntegerType(), nullable=True),
                StructField("unknown_field_16", IntegerType(), nullable=True),
                StructField("unknown_field_17", StringType(), nullable=True),
            ]
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0034/raw/dns-shop-users.txt",
            sep="\t",
            schema=schema,
            header=False,
        )

        df = (
            df.filter(col("name").isNotNull())
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & (~df.username.contains("Пришелец")),
                    array(
                        struct(
                            lit("DNS shop").alias("title"),
                            lit("https://www.dns-shop.ru").alias("link"),
                            col("id").alias("id"),
                            col("username").alias("login"),
                        )
                    ),
                ),
            )
        )

        df = df.select("names", "emails", "phones", "accounts")

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
