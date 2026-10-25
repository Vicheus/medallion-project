from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0369"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0369/raw/lk.vodo-kanal.ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Личный телефон")))
            .withColumn("emails", email_udf(col("e-mail")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Последняя авторизация"), lit("%d.%m.%Y %H:%M:%S")
                ),
            )
            .withColumn("address", address_udf(col("UF_ADDRESS")))
            .select("names", "emails", "phones", "address", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
