from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0636"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0636/raw/mydocuments36.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    struct(
                        lit("mydocuments36.ru").alias("title"),
                        lit("https://mydocuments36.ru").alias("link"),
                        col("username").alias("login"),
                        col("password").alias("password_hash"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("lastvisitDate"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "accounts", "actuality")
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
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
            )
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
