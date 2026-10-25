from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, concat_ws, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0206"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0206/raw/aliexpress_ru.csv",
            sep=",",
            header=True,
        )

        df_buyers = (
            df.withColumn(
                "names",
                name_parts_udf(col("billFirstName"), col("billLastName"), lit(None)),
            )
            .withColumn("emails", email_udf(col("orderUserEmail")))
            .withColumn("phones", lit(None))
            .withColumn("address", lit(None))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("shippingMethodOrig"),
                    df["shippingMethodOrig"],
                    lit("trackNumber"),
                    df["trackNumber"],
                ),
            )
            .select("names", "phones", "emails", "address", "raw_metadata")
        )

        df_receivers = (
            df.withColumn(
                "names",
                name_parts_udf(col("shipFirstName"), col("shipLastName"), lit(None)),
            )
            .withColumn("emails", lit(None))
            .withColumn("phones", phone_udf(col("shipPhone")))
            .withColumn(
                "address",
                address_udf(
                    when(
                        (col("shipCity").isNotNull()) & (col("shipCity") != ""),
                        concat_ws(
                            ", ",
                            when(col("shipZip") != "", col("shipZip")).otherwise(None),
                            when(col("shipState") != "", col("shipState")).otherwise(
                                None
                            ),
                            when(col("shipCity") != "", col("shipCity")).otherwise(
                                None
                            ),
                            when(
                                col("shipStreet1") != "", col("shipStreet1")
                            ).otherwise(None),
                            when(
                                col("shipStreet2") != "", col("shipStreet2")
                            ).otherwise(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("shippingMethodOrig"),
                    df["shippingMethodOrig"],
                    lit("trackNumber"),
                    df["trackNumber"],
                ),
            )
            .select("names", "phones", "emails", "address", "raw_metadata")
        )

        df = df.drop_duplicates()

        df = df_buyers.unionAll(df_receivers)

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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
