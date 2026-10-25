from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    split,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phones_udf,
    address_udf,
    normalize_kz_letters_udf,
    email_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0610"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0610/raw/chsi_all.csv",
                sep=",",
                header=True,
            )
            .withColumn("fio", normalize_kz_letters_udf(col("fio")))
            .withColumn("names", name_udf(col("fio")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        phones_udf(
                            split(col("telephone"), ","), lit(self.dataset_country_code)
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("licenseNumber"),
                    col("licenseNumber"),
                    lit("licenseStartDate"),
                    col("licenseStartDate"),
                ),
            )
            .select("names", "address", "phones", "emails", "raw_metadata")
        )

        df.show(n=20, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(col("raw_metadata").isNotNull(), array(col("raw_metadata"))),
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
