from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array_compact,
    size,
    array,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0548"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0548/raw/cardsi_by/orders.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", array_compact(array(name_udf("customer"))))
            .withColumn("address", array(address_udf(col("delivery_address"))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn(
                "phones",
                array_compact(
                    array(phone_udf(col("phone"), lit(self.dataset_country_code.value)))
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment"),
                    col("comment"),
                    lit("amount"),
                    col("amount"),
                    lit("payment_method"),
                    col("payment_method"),
                    lit("delivery_type"),
                    col("delivery_type"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "address", "emails", "phones", "raw_metadata", "actuality")
        )

        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
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
