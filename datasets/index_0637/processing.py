from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    collect_set,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0637"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0637/raw/allo-internet.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("NAME"), col("LAST_NAME"), lit(None))
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    struct(
                        lit("allo-internet.ru").alias("title"),
                        lit("https://allo-internet.ru").alias("link"),
                        col("LOGIN").alias("login"),
                        col("PASSWORD").alias("password_hash"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "accounts", "actuality")
        )

        df = df.groupBy(["names", "emails"]).agg(
            array_compact(collect_set(col("accounts"))).alias("accounts"),
            max(col("actuality")).alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
