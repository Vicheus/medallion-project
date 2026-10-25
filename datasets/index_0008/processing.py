from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, struct, lit, coalesce

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0008"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0008/raw/cdek.shopping.csv",
            sep=";",
            header=True,
        )

        df.show(n=300, truncate=False)

        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", birth_date_udf(col("dob")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("CDEK shopping").alias("title"),
                            lit("https://cdek.shopping").alias("link"),
                            col("password").alias("password_hash"),
                            col("id").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.select(
            "names", "phones", "emails", "birth_date", "accounts", "actuality"
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        df = df.dropDuplicates()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
