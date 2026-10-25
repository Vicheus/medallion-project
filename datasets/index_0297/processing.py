from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, concat_ws

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
    dataset_code_name: str = "index_0297"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0297/raw/Открытие 2023(binbank.ru).csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("name"), col("patronymic"), col("second_name")),
            )
            .withColumn("birth_date", birth_date_udf(col("BDate"), lit("%d.%m.%Y")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(" ", col("country"), col("region"), col("adress"))
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "birth_date", "emails", "phones", "address")
        )

        df = df.drop_duplicates(["names", "birth_date"])
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
