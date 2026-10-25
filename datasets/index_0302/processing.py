from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.ips.udfs import ip_date_udf, ip_address_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0302"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0302/raw/raw/cp_order_@DBC_links.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("fone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("adress")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "order_date", from_unixtime(col("date_order"), "yyyy-MM-dd HH:mm:ss")
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull() & (col("company") != ""),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("company"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    col("ip_address").alias("ip"),
                                    ip_date_udf(
                                        col("order_date"), lit("%Y-%m-%d %H:%M:%S")
                                    ).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("goods"),
                    col("goods"),
                    lit("vsego"),
                    col("vsego"),
                    lit("desc"),
                    col("desc"),
                    lit("comment"),
                    col("comment"),
                    lit("order_number"),
                    col("order_number"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.drop_duplicates()

        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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
