from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0449"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0449/raw/Магазин_женской_одежды_Mila_2024.csv",
            sep=";",
            header=True,
        ).filter(col("ФИО") != "Без Имени")

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("Адрес")))
            .select("names", "emails", "phones", "birth_date", "address")
        )

        df = df.drop_duplicates(["names", "phones"])

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
