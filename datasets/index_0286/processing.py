from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0286"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0286/raw/neroelectronics by/sale_buyers.csv",
            sep=";",
            header=True,
        ).repartition(20)

        df = (
            df.replace("\\N", None)
            .withColumn("names", name_udf(col("Покупатель")))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("E-mail")))))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("Телефон"), lit(self.dataset_country_code.value)
                            )
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
