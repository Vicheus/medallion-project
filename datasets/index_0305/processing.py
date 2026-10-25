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
    concat_ws,
    collect_set,
    from_unixtime,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0305"

    def parser(self):
        df_addresses = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0305/raw/address_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        when(col("index") != "", col("index")).otherwise(None),
                        when(col("region") != "", col("region")).otherwise(None),
                        when(col("city") != "", col("city")).otherwise(None),
                        when(col("street") != "", col("street")).otherwise(None),
                        when(col("building") != "", col("building")).otherwise(None),
                        when(col("room") != "", col("room")).otherwise(None),
                    )
                ),
            )
            .groupBy(["user_id"])
            .agg(
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                )
            )
            .select("user_id", "address")
        )

        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0305/raw/users_preprocessed.csv",
            sep=",",
            header=True,
        )

        df = (
            df_users.join(
                df_addresses, df_users["id"] == df_addresses["user_id"], "left"
            )
            .withColumn(
                "names",
                name_udf(
                    regexp_replace(regexp_replace(col("fullname"), "\.", ""), "-", "")
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("username")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("mobilephone")))
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("lastlogin"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("nbdoc.ru").alias("title"),
                            lit("https://nbdoc.ru/").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.drop_duplicates(["names", "emails", "phones"])

        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
