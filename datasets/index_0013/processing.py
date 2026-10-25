from pyspark import StorageLevel
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0013"

    def parser(self):
        schema = StructType(
            [
                StructField("user_id", StringType(), True),
                StructField("unknown_date_1", StringType(), True),
                StructField("email", StringType(), True),
                StructField("password", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("email2", StringType(), True),
                StructField("unknown_date_2", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("middle_name", StringType(), True),
            ]
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0013/raw/alfastrah_2023_1kk.csv/alfastrah-users.csv",
            sep="\t",
            schema=schema,
            header=False,
        )

        df = df.replace(to_replace="\\N", value=None)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("middle_name"), col("last_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("email").isNotNull(),
                    array(
                        struct(
                            lit("Альфастрахование").alias("title"),
                            lit("https://alfastrah.ru/login/").alias("link"),
                            email_udf(col("email")).alias("login"),
                            col("password").alias("password_hash"),
                            col("user_id").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("unknown_date_1"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )

        df = df.select(
            "names", "birth_date", "phones", "emails", "accounts", "actuality"
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("accounts").isNotNull()
            )
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
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
