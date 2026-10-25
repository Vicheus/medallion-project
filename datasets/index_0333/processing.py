from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    split,
    size,
    concat_ws,
    array_compact,
    slice,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, address_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0333"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0333/raw/reestr.nostroy_ru_09_2023.txt",
            sep="\t",
            header=True,
        )

        df = (
            df.withColumn("parts", split(col("Должность/ФИО"), " "))
            .withColumn("parts_count", size("parts"))
            .withColumn(
                "fio",
                when(
                    col("parts_count") > 3, concat_ws(" ", slice(col("parts"), -3, 3))
                ).otherwise(col("Должность/ФИО")),
            )
            .withColumn(
                "position",
                when(
                    col("parts_count") > 3,
                    concat_ws(" ", slice(col("parts"), 1, col("parts_count") - 3)),
                ).otherwise(lit(None)),
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("Компания").isNotNull() | col("position").isNotNull(),
                    array(
                        work_udf(
                            col("position"),
                            lit(None),
                            lit(None),
                            col("Компания"),
                            address_udf(col("Адрес работы")),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "documents", "works")
        )

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
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
