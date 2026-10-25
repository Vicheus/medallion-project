from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    concat_ws,
    array_compact,
    array_distinct,
    struct,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    address_udf,
    normalize_address_batch_udf,
    address_with_type_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0528"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0528/raw/sloganbase.ru/users_utf8.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names",
                name_parts_udf(col("us_first_name"), col("us_last_name"), lit(None)),
            )
            .withColumn("birth_date", birth_date_udf(col("us_bdate"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("us_sex")))
            .withColumn("emails", email_udf(col("us_email")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("us_region"), col("us_city")))
            )
            .withColumn(
                "address_with_type", address_with_type_udf(col("address"), lit(1))
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(array(col("address_with_type"))),
            )
            .withColumn(
                "accounts",
                when(
                    col("us_login").isNotNull(),
                    array(
                        struct(
                            lit("sloganbase").alias("title"),
                            lit("https://sloganbase.ru").alias("link"),
                            col("us_login").alias("login"),
                            col("us_pass").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("us_fraza"),
                    col("us_fraza"),
                    lit("us_comment2"),
                    col("us_comment2"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("us_lasttime"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "address",
                "addresses",
                "accounts",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(array_distinct(col("accounts")))) > 0,
                    array_compact(array_distinct(col("accounts"))),
                ).otherwise(None),
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
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
