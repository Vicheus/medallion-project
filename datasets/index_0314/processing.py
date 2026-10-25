from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0314"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0314/raw/yandex_reviews.csv",
                encoding="windows-1251",
                sep="\t",
                header=True,
            )
            .filter(~col("Телефон").startswith("3"))
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "accounts",
                when(
                    col("ЯндексID").isNotNull(),
                    array(
                        struct(
                            lit("Яндекс Отзывы").alias("title"),
                            lit("https://reviews.yandex.ru").alias("link"),
                            col("ЯндексID").alias("id"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "accounts")
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
