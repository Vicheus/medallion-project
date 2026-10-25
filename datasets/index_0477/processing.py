from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    from_unixtime,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0477"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0477/raw/svoboda23/preprocessed/users.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("emails", email_udf(col("umail")))
            .withColumn("phones", phone_udf(col("telefon")))
            .withColumn("address", address_udf(col("adres")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("regdate"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("svoboda23.ru").alias("title"),
                        lit("https://svoboda23.ru").alias("link"),
                        col("uname").alias("login"),
                        col("openpass").alias("password_hash"),
                    )
                ),
            )
            .withColumn("raw_metadata", lit(None))
            .select("names", "emails", "phones", "address", "actuality", "raw_metadata")
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0477/raw/svoboda23/preprocessed/orders.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("telefon")))
            .withColumn("address", address_udf(col("adres")))
            .withColumn("actuality", lit(None))
            .withColumn("accounts", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("comments"), col("comments")),
            )
            .select("names", "emails", "phones", "address", "actuality", "raw_metadata")
        )

        df = df_users.unionAll(df_orders)
        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(),
                    array_compact(array_distinct(array(col("address")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(),
                    array_compact(array_distinct(array(col("emails")))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array_distinct(array(col("raw_metadata")))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("address").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
