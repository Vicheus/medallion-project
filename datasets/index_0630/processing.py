from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, struct, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0630"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0630/raw/psy-in.ru - @database_bereza/wp_users.csv",
                sep=",",
                header=True,
            )
            .filter(~col("user_email").endswith(".ua"))
            .withColumn("names", name_udf(col("display_name")))
            .withColumn("emails", email_udf(col("user_email")))
            .withColumn(
                "accounts",
                when(
                    col("user_login").isNotNull() & col("user_pass").isNotNull(),
                    struct(
                        lit("Институт Инновационных Психотехнологий (ИИП)").alias(
                            "title"
                        ),
                        lit("https://psy-in.ru").alias("link"),
                        col("user_login").alias("login"),
                        col("user_pass").alias("password_hash"),
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
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
