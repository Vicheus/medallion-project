from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    split,
    array,
    array_distinct,
)
from parsetron.settings import DATASET_COUNTRY_CODE

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phones_udf,
    email_udf,
    raw_metadata_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0432"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0432/raw/oirr.kz - @StormBaseAdapter/**/*.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("author")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                phones_udf(
                    split(col("phone"), ","), lit(self.dataset_country_code.value)
                ),
            )
            .withColumn(
                "raw_metadata",
                array(
                    raw_metadata_udf(
                        lit("description"),
                        col("description"),
                        lit("title"),
                        col("title"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("datetime"), lit("%Y-%m-%dT%H:%M:%S%z")),
            )
            .select("names", "address", "phones", "emails", "raw_metadata", "actuality")
        )

        df.show(n=20, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_distinct(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(), array_distinct(array(col("address")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_distinct(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_distinct(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_distinct(array(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
