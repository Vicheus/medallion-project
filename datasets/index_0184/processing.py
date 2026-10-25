from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    first,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0184"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0184/raw/buslik.by (06.2023).txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("Имя")))))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%m.%d"))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("Номер телефона"),
                                lit(self.dataset_country_code.value),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("Почта")))))
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            flatten(collect_set(col("names"))).alias("names"),
            first(col("birth_date")).alias("birth_date"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
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
