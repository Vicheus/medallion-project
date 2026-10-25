from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0075"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0075/raw/tvoe/tvoe-users.csv",
            sep="\t",
            header=True,
        )

        df = (
            df.withColumn(
                "names", name_parts_udf(col("NAME"), col("LAST_NAME"), lit(None))
            )
            .withColumn("phones", phone_udf(col("PERSONAL_PHONE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "accounts",
                when(
                    (col("LOGIN").isNotNull() & (col("LOGIN") != ""))
                    & (col("PASSWORD").isNotNull() & (col("PASSWORD") != "")),
                    array(
                        struct(
                            lit("ТВОЕ - интернет-магазин одежды").alias("title"),
                            lit("https://tvoe.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )
        df = df.select("names", "emails", "phones", "accounts", "actuality")

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
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
