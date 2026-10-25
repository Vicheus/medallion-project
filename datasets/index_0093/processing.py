from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0093"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0093/raw/Dump_public_bookmate.com_08.07.2018_Sha512salt/BookMate_BF/data/Bookmate.json",
            sep="\n",
        )

        df = (
            df.filter(col("n").isNotNull() & col("e").isNotNull())
            .withColumn("names", name_udf(col("n")))
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%Y-%m-%d")))
            .withColumn("emails", email_udf(col("e")))
            .withColumn(
                "ips",
                when(
                    col("i").isNotNull() | col("i2").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("i").isNotNull(),
                                    struct(
                                        col("i").alias("ip"),
                                        ip_date_udf(
                                            col("did"), lit("%Y-%m-%d %H:%M:%S")
                                        ).alias("date"),
                                    ),
                                ).otherwise(None),
                                when(
                                    col("i2").isNotNull(),
                                    struct(
                                        col("i2").alias("ip"),
                                        ip_date_udf(
                                            col("did"), lit("%Y-%m-%d %H:%M:%S")
                                        ).alias("date"),
                                    ),
                                ).otherwise(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("u").isNotNull(),
                    array(
                        struct(
                            lit("Bookmate").alias("title"),
                            lit("https://bookmate.com").alias("link"),
                            col("u").alias("login"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("did"), lit("%Y-%m-%d %H:%M:%S"))
            )
        )
        df = df.select("names", "birth_date", "emails", "ips", "accounts", "actuality")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
