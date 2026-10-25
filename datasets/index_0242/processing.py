from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0242"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0242/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telephone")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("date_added"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("аэробас.рф").alias("title"),
                            lit("https://аэробас.рф").alias("link"),
                            col("email").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array_compact(
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
                    ),
                ),
            )
            .withColumn(
                "address",
                when(
                    col("city").isNotNull(),
                    address_udf(
                        concat_ws(", ", col("postcode"), col("city"), col("address_1"))
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_added"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "ips",
                "works",
                "accounts",
                "actuality",
            )
        )

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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
