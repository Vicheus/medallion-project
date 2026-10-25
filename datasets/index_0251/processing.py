from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0251"

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0251/raw/familyspace_ru.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("emails", email_udf(col("nemail")))
            .withColumn(
                "accounts",
                when(
                    col("nemail").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Familyspace").alias("title"),
                            lit("https://familyspace.ru/login/").alias("link"),
                            email_udf(col("nemail")).alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "accounts")
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
