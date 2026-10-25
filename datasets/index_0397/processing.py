from pyspark import StorageLevel

from pyspark.sql.functions import when, col, lit, array, size, array_compact, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0397"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0397/raw/rusinv_users.csv"
            )
            .withColumn("names", name_udf(col("display_name")))
            .withColumn("emails", email_udf(col("user_email")))
            .withColumn(
                "accounts",
                when(
                    col("user_login").isNotNull() & col("user_pass").isNotNull(),
                    array(
                        struct(
                            lit("Русинвестпроект").alias("title"),
                            lit("https://rusinvestproject.ru").alias("link"),
                            col("user_login").alias("login"),
                            col("user_pass").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "accounts")
        )

        df.cache()

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
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
