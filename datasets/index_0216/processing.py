from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, first, collect_set, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0216"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0216/raw/astrovolga.ru.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%m.%d"))
            )
            .select("names", "phones", "emails", "address", "birth_date")
        )

        df = df.groupBy(["names", "phones"]).agg(
            collect_set(col("emails")).alias("emails"),
            collect_set(col("address")).alias("address"),
            first(col("birth_date"), ignorenulls=True).alias("birth_date"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
