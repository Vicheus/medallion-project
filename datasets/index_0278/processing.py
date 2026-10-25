from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, coalesce

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0278"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0278/raw/akkamulik.by/user_admin (2).csv",
            sep=";",
            header=True,
        ).repartition(20)

        df = (
            df.replace("NULL", None)
            .withColumn("names", name_parts_udf(col("Имя"), col("Фамилия"), lit(None)))
            .withColumn("emails", email_udf(col("E-Mail")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("Последняя авторизация"), col("Дата изменения")),
                    lit("%d.%m.%Y %H:%M:%S"),
                ),
            )
            .withColumn(
                "phones", phone_udf(col("Логин"), lit(self.dataset_country_code.value))
            )
            .select("names", "emails", "phones", "actuality")
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.drop_duplicates()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
