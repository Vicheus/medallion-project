from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0014"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0014/raw/Yandex_practicum/Yandex Praktikum Part.txt",
            sep="\t",
        )

        df = (
            df.withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(""))
            )
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("yauid").isNotNull(),
                    array(
                        struct(
                            lit("Яндекс практикум").alias("title"),
                            lit("https://practicum.yandex.ru").alias("link"),
                            col("username").alias("login"),
                            col("yauid").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
        )

        df = df.select("names", "phones", "emails", "accounts")

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
