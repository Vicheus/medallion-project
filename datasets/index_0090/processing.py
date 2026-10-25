from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0090"

    def parser(self):
        df = self.read(
            path="Ренессанс_Страхование_preprocessed.csv", sep=";", header=True
        )
        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Ренессанс страхование").alias("title"),
                            lit("https://www.renins.ru").alias("link"),
                            when(col("login").startswith("PersArea"), lit(None))
                            .otherwise(col("login"))
                            .alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
        )

        df = df.select("names", "emails", "phones", "accounts")

        df.persist(StorageLevel.DISK_ONLY).count()

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
                "accounts",
                when(col("accounts").isNotNull(), col("accounts")).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
