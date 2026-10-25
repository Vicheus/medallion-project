from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, size, regexp_replace
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0203"

    def parser(self):
        schema = StructType(
            [
                StructField("email", StringType(), True),
                StructField("password_hash", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("user_type", StringType(), True),
                StructField("unknown_field_1", StringType(), True),
                StructField("unknown_field_2", StringType(), True),
                StructField("unknown_field_3", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("unknown_field_4", StringType(), True),
                StructField("birth_date", StringType(), True),
            ]
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0203/raw/zaymigo.ru - @bereza_bd.csv",
                sep=";",
                header=False,
                schema=schema,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("ZAYMIGO").alias("title"),
                        lit("https://zaymigo.ru").alias("link"),
                        col("email").alias("login"),
                        regexp_replace(col("password_hash"), "',", "").alias(
                            "password_hash"
                        ),
                    )
                ),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

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
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.select("names", "phones", "emails", "birth_date", "accounts")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
