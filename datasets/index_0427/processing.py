from pyspark import StorageLevel
from parsetron.settings import DATASET_COUNTRY_CODE

from pyspark.sql.functions import when, col, array, lit
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    phone_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0427"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0427/raw/likitoriya.com - @StormBaseAdapter.csv",
                sep=",",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "phones", phone_udf(col("phone"), lit(self.dataset_country_code.value))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("total_sum"),
                    col("total_sum"),
                    lit("comment"),
                    col("comment"),
                    lit("comment2"),
                    col("comment2"),
                ),
            )
            .select("names", "emails", "phones", "address", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "emails", "phones"])

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
