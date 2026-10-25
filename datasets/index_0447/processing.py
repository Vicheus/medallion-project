from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, from_unixtime

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0447"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0447/raw/users.csv",
            sep=";",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("clientFIO")))
            .withColumn("phones", phone_udf(col("clientPhone")))
            .withColumn("address", address_udf(col("clientAddress")))
            .withColumn("emails", email_udf(col("clientEmail")))
            .withColumn("raw_metadata", raw_metadata_udf(lit("note"), col("note")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("create_time"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "phones", "emails", "raw_metadata", "actuality")
        )

        df = df.drop_duplicates(["names", "phones"])

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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
