from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    length,
    struct,
    size,
    array_compact,
    array_distinct
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0002"
    output_file_count: int = 5

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0002/raw/citilab.ru_raw/citilab.ru.csv",
            sep=",",
            header=True,
        ).replace("NULL", None)

        df = df.dropDuplicates(["cellphone", "emailname", "fname", "mname", "lname"])

        df = df.withColumn(
            "names",
            when(
                (length(col("fname")) > 2)
                & (length(col("lname")) > 2)
                & (length(col("mname")) > 2),
                concat_ws(" ", col("lname"), col("fname"), col("mname")),
            ).otherwise(None),
        ).coalesce(5)

        df = (
            df.withColumn("names", name_udf(col("names")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("address_with_type", address_with_type_udf(col("address"), lit(1)))
            .withColumn('addresses', normalize_address_batch_udf(array(col('address_with_type'))))
            .withColumn("phones", phone_udf(col("cellphone")))
            .withColumn("emails", email_udf(col("emailname")))
            .withColumn(
                "accounts",
                when(
                    col("uname").isNotNull() & col("upass").isNotNull(),
                    array(
                        struct(
                            lit("citilab").alias("title"),
                            lit("https://my.citilab.ru/client/").alias("link"),
                            col("uname").alias("login"),
                            col("upass").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("lastlogin"), lit("%Y-%m-%dT%H:%M:%S.%f")),
            )
        ).coalesce(5)

        df = df.select("names", "address", "addresses", "emails", "phones", "accounts", "actuality")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(size(array_compact(array_distinct(col("addresses"))))> 0, array_compact(array_distinct(col("address")))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.show(n=20, truncate=False)

        return df.coalesce(5)


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
