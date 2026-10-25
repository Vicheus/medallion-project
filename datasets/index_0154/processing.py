from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0154"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0154/raw/metro-cc.ru.csv",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("NAME")))
            .withColumn("phones", phone_udf(col("PHONE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "accounts",
                when(
                    col("CARD").isNotNull(),
                    array(
                        struct(
                            lit("Карта лояльности METRO").alias("title"),
                            col("CARD").alias("client_card_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("DATE_CREATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "phones", "emails", "accounts", "actuality")
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select("names", "phones", "emails", "accounts", "actuality")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
