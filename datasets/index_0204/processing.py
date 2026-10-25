from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0204"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0204/raw/vivadengi.ru.txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("address", address_udf(col("Где родился")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("emails", email_udf(col("Почта")))
            .select("names", "phones", "emails", "address", "birth_date")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.drop_duplicates(["names", "birth_date"])

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
