from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    calc_completeness: bool = True
    dataset_code_name: str = "index_0620"

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/upload/index_0620/raw/rosodezhdaspb.csv",
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
                        lit("Mooriposh").alias("title"),
                        lit("https://www.rosodezhdaspb.ru").alias("link"),
                        col("LOGIN").alias("login"),
                        col("PASSWORD").alias("password_hash"),
                    ),
                ),
            )
            .select("names", "emails", "accounts")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
