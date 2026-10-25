from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, size, lit, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    sex_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0385"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0385/raw/burgerheroes.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Burger Heroes").alias("title"),
                            lit("https://burgerheroes.ru").alias("link"),
                            col("email").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select("names", "sex", "phones", "accounts", "actuality")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
