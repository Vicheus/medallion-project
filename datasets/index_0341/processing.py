from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
    concat_ws,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    birth_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0341"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0341/raw/filtromir.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("city"), col("address")))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("modified"), col("created")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("ФильтроМир").alias("title"),
                            lit("https://filtromir.ru").alias("link"),
                            col("email").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment"),
                    col("comment"),
                    lit("info1"),
                    col("info1"),
                    lit("info2"),
                    col("info2"),
                    lit("admin_comment"),
                    col("admin_comment"),
                    lit("orders_count"),
                    col("orders_count"),
                    lit("orders_price"),
                    col("orders_price"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "accounts",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
