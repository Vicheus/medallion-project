from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    concat,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    actuality_date_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0522"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0522/raw/mosgorzdrav.ru.csv",
                sep="|",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("Адрес проживания")),
                            address_udf(col("Адрес регистрации: Адрес")),
                            address_udf(col("Место работы/учебы: Фактический адрес")),
                        )
                    )
                ),
            )
            .withColumn(
                "addresses_with_type",
                array_compact(
                    array_distinct(
                        array(
                            address_with_type_udf(col("Адрес проживания"), lit(1)),
                            address_with_type_udf(
                                col("Адрес регистрации: Адрес"), lit(0)
                            ),
                            address_with_type_udf(
                                col("Место работы/учебы: Фактический адрес"), lit(3)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "addresses",
                array_compact(
                    array_distinct(
                        normalize_address_batch_udf(col("addresses_with_type"))
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("СНИЛС").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("СНИЛС"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Номер полиса ОМС").isNotNull()
                                & (col("Номер полиса ОМС") != 0),
                                document_udf(
                                    lit("номер страхового полиса"),
                                    col("Номер полиса ОМС"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Документ: Серия").isNotNull()
                                & col("Документ: Номер").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("Документ: Серия"), col("Документ: Номер")
                                    ),
                                    col("Документ: Дата выдачи"),
                                    lit(None),
                                    col("Документ: Кем выдан"),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("Место работы/учебы: Наименование").isNotNull(),
                    array(
                        work_udf(
                            col("Место работы/учебы: Должность/группа"),
                            lit(None),
                            lit(None),
                            col("Место работы/учебы: Наименование"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата заболевания"), lit("%Y-%m-%d")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Категория"),
                    col("Категория"),
                    lit("Отделение"),
                    col("Отделение"),
                    lit("ФИО врача"),
                    col("ФИО врача"),
                    lit("Предварительный диагноз"),
                    col("Предварительный диагноз"),
                    lit("ФИО отбиравшего материал"),
                    col("ФИО отбиравшего материал"),
                    lit("ФИО доставившего материал"),
                    col("ФИО доставившего материал"),
                    lit("ФИО принявшего материал"),
                    col("ФИО принявшего материал"),
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "address",
                "addresses",
                "phones",
                "raw_metadata",
                "works",
                "documents",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names", "birth_date"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(col("addresses").isNotNull(), array(col("addresses"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
