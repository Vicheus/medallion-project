from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
    concat_ws,
    array_compact,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    relations_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0340"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0340/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name2")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("username")))
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Страховая компания - Армеец").alias("title"),
                            lit("https://www.armeec.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "relations",
                relations_udf(
                    concat_ws(" ", lit("Участники страхового договора"), col("insured"))
                ),
            )
            .select("names", "phones", "emails", "address", "accounts", "relations")
        )

        df = (
            df.groupBy(col("names"))
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(collect_set(col("relations"))).alias("relations"),
                array_compact(flatten(collect_set(col("accounts")))).alias("accounts"),
            )
            .select("names", "phones", "emails", "address", "accounts", "relations")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
