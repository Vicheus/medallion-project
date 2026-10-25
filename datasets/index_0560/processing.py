from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    collect_list,
    array,
    array_distinct,
    array_compact,
    size,
    flatten,
    concat,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0560"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.RU
    validate_invalid_groupping: bool = True
    output_file_count: int = 5

    def parser(self):
        df = self.read(
            path="/media/user/T7 Shield/Databases/anex/full/clients_*.csv",
            sep=",",
            header=True,
        )

        df.printSchema()

        df = (
            df.filter(
                (col("Гражданство") == "-2147483647") | (col("Гражданство") == "2")
            )
            .withColumn(
                "names",
                array_distinct(
                    array_compact(
                        array(
                            name_parts_udf(
                                col("Имя_кириллица"),
                                col("Фамилия_кириллица"),
                                col("Отчество_кириллица"),
                            ),
                            name_parts_udf(
                                col("Имя_латиница"),
                                col("Фамилия_латиница"),
                                col("Отчество_латиница"),
                            ),
                        )
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата_рождения"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Серия_документа").isNotNull()
                                & col("Номер_документа").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("Серия_документа"), col("Номер_документа")
                                    ),
                                    col("Документ_выдан"),
                                    col("Действителен_до"),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                    lit(self.dataset_country_code),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("ТурОператор_Мобильный"),
                    phone_udf(col("Мобильный"), lit(self.dataset_country_code)),
                    lit("ТурОператор_E-mail"),
                    email_udf(col("E-mail")),
                ),
            )
            .select("names", "birth_date", "documents", "raw_metadata")
        )

        df = (
            df.groupby(["names", "birth_date"])
            .agg(
                array_compact(array_distinct(collect_list("raw_metadata"))).alias(
                    "raw_metadata"
                ),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias(
                    "documents"
                ),
            )
            .select("names", "birth_date", "documents", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("documents").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
