from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0263"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0263/raw/flor2u.ru_2022.05.19/users.csv",
                sep=",",
                header=True,
            )
            .replace("'", "")
            .replace("\t", "")
            .withColumn(
                "names", name_parts_udf(col("NAME"), col("LAST_NAME"), lit(None))
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDATE"), lit("%Y.%m.%d"))
            )
            .withColumn("phones", phone_udf(col("PERSONAL_PHONE")))
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Flor2U - Доставка Цветов").alias("title"),
                            lit("https://www.flor2u.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "birth_date", "sex", "accounts")
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
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
