from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    size,
    struct,
    lit,
    max,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0643"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0643/raw/ngs_users.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    struct(
                        lit("NGS").alias("title"),
                        lit("https://ngs.ru").alias("link"),
                        col("login").alias("login"),
                        col("password").alias("password_hash"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("modify_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "accounts", "actuality")
        )

        df = (
            df.groupBy(["names", "emails"])
            .agg(
                array_compact(collect_set(col("accounts"))).alias("accounts"),
                max(col("actuality")).alias("actuality"),
            )
            .select("names", "emails", "accounts", "actuality")
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
