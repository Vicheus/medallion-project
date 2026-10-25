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
    concat,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    relations_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0473"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0473/raw/astrodent-clinic.ru - @StormBaseAdapter.txt",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("birth_place", address_udf(col("Место рождения")))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Мобильный телефон")),
                            phone_udf(col("Домашний телефон")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("Город").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("Город"),
                                        when(
                                            col("Улица") != "",
                                            concat(lit("ул. "), col("Улица")),
                                        ).otherwise(None),
                                        when(
                                            col("Дом") != "",
                                            concat(lit("д. "), col("Дом")),
                                        ).otherwise(None),
                                        when(
                                            col("Корпус") != "",
                                            concat(lit("кор. "), col("Корпус")),
                                        ).otherwise(None),
                                        when(
                                            col("Квартира") != "",
                                            concat(lit("кв. "), col("Квартира")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            address_udf(col("Адрес и дата регистрации")),
                        )
                    )
                ),
            )
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Родитель").isNotNull(),
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        name_udf(col("Родитель")),
                                        lit("родитель"),
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("Представитель Имя").isNotNull(),
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        name_parts_udf(
                                            col("Представитель Имя"),
                                            col("Представитель Фамилия"),
                                            col("Представитель Отчество"),
                                        ),
                                        lit("представитель"),
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("Семья").isNotNull(),
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        col("Семья"),
                                        lit("семья"),
                                    )
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
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
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("СНИЛС").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("СНИЛС"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Паспорт Серия и номер").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("Паспорт Серия и номер"),
                                    col("Паспорт Дата выдачи"),
                                    lit(None),
                                    col("Паспорт Кем выдан"),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Первый прием"),
                    col("Первый прием"),
                    lit("Последний прием"),
                    col("Последний прием"),
                    lit("Завершено"),
                    col("Завершено"),
                    lit("Личный счет"),
                    col("Личный счет"),
                    lit("Счет семьи"),
                    col("Счет семьи"),
                    lit("Сумма выставленных счетов"),
                    col("Сумма выставленных счетов"),
                    lit("Комментарий"),
                    col("Комментарий"),
                    lit("Доп комментарий"),
                    col("Доп комментарий"),
                    lit("Полисы"),
                    col("Полисы"),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("Последний прием"), lit("%d.%M.%y"))
            )
            .select(
                "names",
                "birth_date",
                "birth_place",
                "sex",
                "emails",
                "phones",
                "address",
                "relations",
                "documents",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(),
                    array_compact(array_distinct(array(col("emails")))),
                ).otherwise(None),
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
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
