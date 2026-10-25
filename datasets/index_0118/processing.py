from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    array_distinct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0118"

    def parser(self):
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0118/raw/spasskie_vorota_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("Страховая компания Спасские ворота").alias("title"),
                            lit("https://spasskievorota.ru").alias("link"),
                            col("email").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "accounts")
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
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select("names", "emails", "phones", "accounts")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
