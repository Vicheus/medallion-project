from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, array_size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    raw_metadata_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0514"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 5

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/РФ Автобусные билеты 2021./Автобусные билеты 2021 не чищенные_new.txt",
            sep="|",
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "documents",
                when(
                    col("Номер документа").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Номер документа").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("Номер документа"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("BUYDATE"),
                    lit("%d.%m.%Y %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Место отправления"),
                    col("Место отправления"),
                    lit("Место прибытия"),
                    col("Место прибытия"),
                    lit("Дата отправления"),
                    col("Дата отправления"),
                    lit("Дата прибытия"),
                    col("Дата прибытия"),
                    lit("ROUTE"),
                    col("ROUTE"),
                    lit("PLACES"),
                    col("PLACES"),
                    lit("ТС модель"),
                    col("ТС модель"),
                    lit("Рег знак ТС"),
                    col("Рег знак ТС"),
                ),
            )
            .select("names", "birth_date", "sex", "documents", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(array_size(col("documents")) > 0, col("documents")).otherwise(
                    None
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("birth_date").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
