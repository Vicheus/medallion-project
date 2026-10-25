from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    size,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0376"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0376/raw/ASDAP_RU.csv",
            sep=";",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(array(phone_udf(col("Мобильныйтелефон"))))
                ),
            )
            .withColumn(
                "works",
                when(
                    col("Компания").isNotNull() | col("Должность").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("Должность"),
                                    lit(None),
                                    lit(None),
                                    col("Компания"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    regexp_extract("Дата регистрации", r"(\d{2}\.\d{2}\.\d{4})", 1),
                    lit("%d.%m.%Y"),
                ),
            )
            .select("names", "phones", "actuality", "works")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
