from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, phone_udf, email_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0140"

    def parser(self):
        schema = (
            StructType()
            .add("_c0", StringType(), True)
            .add("username", StringType(), True)
            .add("password", StringType(), True)
            .add("_c3", StringType(), True)
            .add("first_name", StringType(), True)
            .add("last_name", StringType(), True)
            .add("email", StringType(), True)
            .add("_c7", StringType(), True)
            .add("_c8", StringType(), True)
            .add("_c9", StringType(), True)
            .add("_c10", StringType(), True)
            .add("_c11", StringType(), True)
            .add("_c12", StringType(), True)
            .add("_c13", StringType(), True)
            .add("_c14", StringType(), True)
            .add("_c15", StringType(), True)
            .add("number", StringType(), True)
            .add("", StringType(), True)
            .add("_c18", StringType(), True)
            .add("_c19", StringType(), True)
            .add("_c20", StringType(), True)
            .add("_c21", StringType(), True)
            .add("_c22", StringType(), True)
            .add("_c23", StringType(), True)
            .add("_c24", StringType(), True)
            .add("_c25", StringType(), True)
            .add("_c26", StringType(), True)
            .add("_c27", StringType(), True)
            .add("_c28", StringType(), True)
            .add("_c29", StringType(), True)
            .add("_c30", StringType(), True)
            .add("_c31", StringType(), True)
            .add("_c32", StringType(), True)
            .add("_c33", StringType(), True)
            .add("_c34", StringType(), True)
            .add("_c35", StringType(), True)
            .add("middle_name", StringType(), True)
            .add("_c37", StringType(), True)
            .add("_c38", StringType(), True)
            .add("_c39", StringType(), True)
            .add("_c40", StringType(), True)
            .add("_c41", StringType(), True)
            .add("_c42", StringType(), True)
            .add("_c43", StringType(), True)
        )

        df = (
            self.read(
                path="/home/user/Documents/data/index_0140/raw/club.alfabank.ru_2.txt",
                sep="\t",
                header=False,
                schema=schema,
            )
            .withColumn(
                "names",
                when(
                    col("first_name") != col("last_name"),
                    name_parts_udf(
                        col("first_name"), col("last_name"), col("middle_name")
                    ),
                ).otherwise(name_udf(col("first_name"))),
            )
            .withColumn("phones", phone_udf(col("number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() | col("password").isNotNull(),
                    array(
                        struct(
                            lit("Альфабанк-клуб").alias("title"),
                            lit("https://club.alfabank.ru").alias("link"),
                            col("username").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "emails", "accounts")
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
        df = df.select("names", "phones", "emails", "accounts")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.dropDuplicates()

        df.show(n=10, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
