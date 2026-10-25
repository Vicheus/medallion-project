from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    struct,
    lit,
    array_compact,
    concat_ws,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0009"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0009/raw/cdek.market.csv",
            sep=";",
            header=True,
        )

        df.show(n=300, truncate=False)

        df = (
            df.withColumn(
                "names",
                name_udf(
                    concat_ws(
                        " ",
                        when(col("lastname").isNotNull(), col("lastname")).otherwise(
                            None
                        ),
                        when(col("firstname").isNotNull(), col("firstname")).otherwise(
                            None
                        ),
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday")))
            .withColumn(
                "phones",
                array_compact(array(phone_udf(col("phone")), phone_udf(col("fax")))),
            )
            .withColumn(
                "emails",
                array_compact(
                    array(email_udf(col("email")), email_udf(col("responsible_email")))
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("user_login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("CDEK market").alias("title"),
                            lit("https://cdek.market/").alias("link"),
                            col("user_login").alias("login"),
                            col("password").alias("password_hash"),
                            col("user_id").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("last_login"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("company"), df["company"]))
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "accounts",
            "actuality",
            "raw_metadata",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.dropDuplicates()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
