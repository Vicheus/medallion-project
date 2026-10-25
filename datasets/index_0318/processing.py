from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, concat_ws

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0318"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0318/raw/папироска.рф 09.2024.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("firstname lastname")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("create_datetime"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("address_zip"),
                        col("address_country"),
                        col("address_city"),
                        col("address_street"),
                        col("address_dom"),
                        col("address_kvartira"),
                    )
                ),
            )
            .select("names", "emails", "address", "actuality")
        )

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
