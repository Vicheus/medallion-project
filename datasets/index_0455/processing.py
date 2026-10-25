from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    concat_ws,
    lit,
    struct,
    greatest,
    split,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phones_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0455"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0455/raw/partselect.ru.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("FirstName"), col("LastName"), col("SecondName")),
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phones_udf(split(col("Phones"), ",")))
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("Postcode"),
                        col("Settlement"),
                        col("Street"),
                        col("Building"),
                        col("Apartment"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("Comments"), col("Comments"))
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("DateLastVisit"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("DateFrom"), col("DateLastVisit")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "raw_metadata",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

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
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
