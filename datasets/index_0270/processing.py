from pyspark import StorageLevel
from pyspark.sql.functions import col, lit, regexp_replace, when, array, trim

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0270"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0270/raw/Юр фирма edin.center.txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                when(
                    col("first_name") != col("last_name"),
                    trim(
                        regexp_replace(
                            name_parts_udf(
                                col("first_name"), col("last_name"), lit(None)
                            ),
                            "Пр",
                            "",
                        )
                    ),
                ).otherwise(
                    trim(regexp_replace(name_udf(col("first_name")), "Пр", ""))
                ),
            )
            .withColumn("phones", phone_udf(col("phone1")))
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .select("names", "phones", "address", "raw_metadata")
        )

        df = df.drop_duplicates()

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
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
