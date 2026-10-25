from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0396"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0396/raw/preprocessed/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("name1")), name_udf(col("name2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone1")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email1")),
                            email_udf(col("email2")),
                            email_udf(col("login")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_insert"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Сатро-Паладин").alias("title"),
                            lit("https://satro-paladin.com").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            ip_date_udf(col("date_insert")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("post").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                col("post"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "ips",
                "accounts",
                "works",
                "actuality",
            )
        )

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
