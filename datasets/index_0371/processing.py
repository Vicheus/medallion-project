from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, from_unixtime

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0371"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0371/raw/orders.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("mail")))
            .withColumn("order_date", from_unixtime(col("date"), "yyyy-MM-dd HH:mm:ss"))
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("info"), col("info")))
            .select("names", "emails", "phones", "actuality", "raw_metadata")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
