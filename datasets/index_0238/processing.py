from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, email_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0238"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0238/raw/forento.ru (09.2023).txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%m.%d"))
            )
            .withColumn("emails", email_udf(col("Логин")))
            .withColumn(
                "accounts",
                when(
                    col("Логин").isNotNull() & col("Пароль").isNotNull(),
                    array(
                        struct(
                            lit("Forento.ru").alias("title"),
                            lit("https://forento.ru").alias("link"),
                            col("Логин").alias("login"),
                            col("Пароль").alias("password"),
                        )
                    ),
                ),
            )
            .select("names", "birth_date", "emails", "accounts")
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
