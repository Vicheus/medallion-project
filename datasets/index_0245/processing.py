from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
    array_compact,
    flatten,
    collect_set,
    max,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0245"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0245/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S")).alias(
                                "date"
                            ),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("pass").isNotNull() & col("login").isNotNull(),
                    array(
                        struct(
                            lit("Медицинская компания Моя Наука").alias("title"),
                            lit("https://naykalab.ru/").alias("link"),
                            col("login").alias("login"),
                            col("pass").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .select(
                "names", "emails", "phones", "ips", "accounts", "address", "actuality"
            )
        )

        df.persist(StorageLevel.DISK_ONLY)

        df = (
            df.groupby(["names", "phones"])
            .agg(
                array_compact(collect_set("emails")).alias("emails"),
                array_compact(collect_set("address")).alias("address"),
                array_compact(flatten(collect_set("ips"))).alias("ips"),
                array_compact(flatten(collect_set("accounts"))).alias("accounts"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names", "emails", "phones", "ips", "accounts", "address", "actuality"
            )
        )

        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
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
