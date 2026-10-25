from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_parts_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0230"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0230/raw/РЖД Персонал (2022).txt",
                sep="\t",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Номер телефона1")),
                            phone_udf(col("Номер телефона2")),
                            phone_udf(col("Номер телефона3")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn(
                "works",
                when(
                    col("Место").isNotNull() | col("Роль").isNotNull(),
                    array(
                        work_udf(
                            col("Роль"),
                            lit(None),
                            lit(None),
                            concat_ws(" ", lit('ОАО "РЖД"'), col("Место")),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "works")
        )

        df = (
            df.groupBy("names", "works")
            .agg(
                array_compact(array_distinct(flatten(collect_set("phones")))).alias(
                    "phones"
                ),
                collect_set("emails").alias("emails"),
            )
            .withColumn("names", array(col("names")))
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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
