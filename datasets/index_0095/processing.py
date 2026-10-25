from pyspark import StorageLevel
from pyspark.sql.functions import (
    size,
    when,
    col,
    lit,
    array,
    struct,
    array_distinct,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0095"

    def parser(self):
        df = self.read(path="askona_preprocessed.csv", sep=";", header=True)

        df = (
            df.withColumn("names", name_udf(col("full_name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email1")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("birth_date", birth_date_udf("birth_date", lit("%Y-%m-%d")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Аскона").alias("title"),
                            lit("https://www.askona.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
        )

        df = df.select("names", "sex", "birth_date", "emails", "phones", "accounts")

        df = df.dropDuplicates(["names", "emails", "phones"])

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), col("accounts")).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
