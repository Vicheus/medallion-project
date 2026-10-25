from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    max,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    regexp_replace,
    flatten,
    collect_set,
    first,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    relationship_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0268"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0268/raw/Sovcombank/pyrus.com_loan_request_*utf8.csv",
            sep="\t",
            header=True,
        )
        df1 = (
            df.withColumn("names", name_udf(col("ФИО *")))
            .withColumn("sex", sex_udf(col("Пол *")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения *"), lit("%d.%m.%Y"))
            )
            .withColumn("birth_place", address_udf(col("Место рождения *")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Телефон мобильный")),
                            phone_udf(col("Домашний телефон")),
                            phone_udf(col("Рабочий телефон")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("Адрес электронной почты")),
                            email_udf(col("Электронная почта")),
                        )
                    )
                ),
            )
            .withColumn("relationship", relationship_udf(col("Семейное положение")))
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ФИО супруга(и)").isNotNull()
                                & (col("ФИО супруга(и)") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО супруга(и)")),
                                    phone_udf(col("Телефон супруга(и)")),
                                    lit("Супруг(а)"),
                                ),
                            ).otherwise(lit(None)),
                            when(
                                col("ФИО доп 1").isNotNull() & (col("ФИО доп 1") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО доп 1")),
                                    phone_udf(col("Доп телефон 1")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None)),
                            when(
                                col("ФИО доп 2").isNotNull() & (col("ФИО доп 2") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО доп 2")),
                                    phone_udf(col("Доп телефон 2")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None)),
                            when(
                                col("ФИО доп 3").isNotNull() & (col("ФИО доп 3") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО доп 3")),
                                    phone_udf(col("Доп телефон 3")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None)),
                            when(
                                col("ФИО руководителя").isNotNull()
                                & (col("ФИО руководителя") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО руководителя")),
                                    lit("Руководитель"),
                                ),
                            ).otherwise(lit(None)),
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
                                col("Серия и номер паспорта *").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Серия и номер паспорта *").alias("serial"),
                                    col("Дата выдачи паспорта *").alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("Кем выдан паспорт *").alias("authority"),
                                    regexp_replace(
                                        col("Код подразделения"), r"[^0-9]", ""
                                    ).alias("authority_code"),
                                ),
                            )
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
                                concat_ws(
                                    ", ",
                                    when(
                                        col("Адрес регистрации: индекс").isNotNull()
                                        & (
                                            col("Адрес регистрации: индекс") != "111111"
                                        ),
                                        col("Адрес регистрации: индекс"),
                                    ).otherwise(None),
                                    when(
                                        col("Адрес регистрации: регион").isNotNull(),
                                        col("Адрес регистрации: регион"),
                                    ).otherwise(None),
                                    when(
                                        col(
                                            "Адрес регистрации: город/населенный пункт *"
                                        ).isNotNull(),
                                        col(
                                            "Адрес регистрации: город/населенный пункт *"
                                        ),
                                    ).otherwise(None),
                                    when(
                                        col("Адрес регистрации: улица *").isNotNull(),
                                        col("Адрес регистрации: улица *"),
                                    ).otherwise(None),
                                    when(
                                        col(
                                            "Адрес регистрации: номер дома, корпус/строение *"
                                        ).isNotNull(),
                                        col(
                                            "Адрес регистрации: номер дома, корпус/строение *"
                                        ),
                                    ).otherwise(None),
                                    when(
                                        col("Адрес регистрации: квартира").isNotNull(),
                                        col("Адрес регистрации: квартира"),
                                    ).otherwise(None),
                                )
                            ),
                            address_udf(col("Адрес фактического проживания")),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("Название организации").isNotNull()
                    | col("Должность/профессия").isNotNull(),
                    array(
                        work_udf(
                            col("Должность/профессия"),
                            lit(None),
                            lit(None),
                            col("Название организации"),
                            address_udf(col("Адрес места работы")),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Последняя активность"), lit("%d.%m.%Y %H:%M")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Какой продукт Банка хотели бы оформить?"),
                    col("Какой продукт Банка хотели бы оформить?"),
                    lit("Цель кредита"),
                    col("Цель кредита"),
                    lit("На какую сумму Вы рассчитываете?"),
                    col("На какую сумму Вы рассчитываете?"),
                    lit("Срок кредитования"),
                    col("Срок кредитования"),
                    lit("Комфортный ежемесячный платеж"),
                    col("Комфортный ежемесячный платеж"),
                    lit("Социальный статус"),
                    col("Социальный статус"),
                    lit("Основной доход"),
                    col("Основной доход"),
                    lit("Пенсия"),
                    col("Пенсия"),
                    lit("Доход супруга(и)"),
                    col("Доход супруга(и)"),
                    lit("Доход по совместительству"),
                    col("Доход по совместительству"),
                    lit("Другое"),
                    col("Другое"),
                    lit("У клиента есть имущество? *"),
                    col("У клиента есть имущество? *"),
                    lit("Комментарий для андеррайтинга"),
                    col("Комментарий для андеррайтинга"),
                    lit("Тип недвижимости"),
                    col("Тип недвижимости"),
                    lit("Размер/Марка"),
                    col("Размер/Марка"),
                    lit("Год выпуска/покупки"),
                    col("Год выпуска/покупки"),
                    lit("Собственник"),
                    col("Собственник"),
                    lit("Доля заявителя"),
                    col("Доля заявителя"),
                    lit("Оценочная стоимость"),
                    col("Оценочная стоимость"),
                    lit("Залог соответствует_требованиям Банка?"),
                    col("Залог соответствует_требованиям Банка?"),
                    lit("Заявитель согласен под залог?*"),
                    col("Заявитель согласен под залог?*"),
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df2 = (
            df.filter(
                (col("ФИО супруга(и)").isNotNull() & (col("ФИО супруга(и)") != ""))
                & (
                    col("Телефон супруга(и)").isNotNull()
                    & (col("Телефон супруга(и)") != "")
                )
            )
            .withColumn("names", name_udf(col("ФИО супруга(и)")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(array(phone_udf(col("Телефон супруга(и)"))))
                ),
            )
            .withColumn("emails", array())
            .withColumn("relationship", lit(None))
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ФИО *").isNotNull() & (col("ФИО *") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО *")),
                                    phone_udf(col("Телефон мобильный")),
                                    lit("Супруг(а)"),
                                ),
                            ).otherwise(lit(None))
                        )
                    )
                ),
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("Последняя активность"), lit("%d.%m.%Y %H:%M")),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df3 = (
            df.filter(
                (col("ФИО доп 1").isNotNull() & (col("ФИО доп 1") != ""))
                & (col("Доп телефон 1").isNotNull() & (col("Доп телефон 1") != ""))
            )
            .withColumn("names", name_udf(col("ФИО доп 1")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Доп телефон 1"))))),
            )
            .withColumn("emails", array())
            .withColumn("relationship", lit(None))
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ФИО *").isNotNull() & (col("ФИО *") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО *")),
                                    phone_udf(col("Телефон мобильный")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None))
                        )
                    )
                ),
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("Последняя активность"), lit("%d.%m.%Y %H:%M")),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df4 = (
            df.filter(
                (col("ФИО доп 2").isNotNull() & (col("ФИО доп 2") != ""))
                & (col("Доп телефон 2").isNotNull() & (col("Доп телефон 2") != ""))
            )
            .withColumn("names", name_udf(col("ФИО доп 2")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Доп телефон 2"))))),
            )
            .withColumn("emails", array())
            .withColumn("relationship", lit(None))
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ФИО *").isNotNull() & (col("ФИО *") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО *")),
                                    phone_udf(col("Телефон мобильный")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None))
                        )
                    )
                ),
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("Последняя активность"), lit("%d.%m.%Y %H:%M")),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df5 = (
            df.filter(
                (col("ФИО доп 3").isNotNull() & (col("ФИО доп 3") != ""))
                & (col("Доп телефон 3").isNotNull() & (col("Доп телефон 3") != ""))
            )
            .withColumn("names", name_udf(col("ФИО доп 3")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Доп телефон 3"))))),
            )
            .withColumn("emails", array())
            .withColumn("relationship", lit(None))
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ФИО *").isNotNull() & (col("ФИО *") != ""),
                                concat_ws(
                                    " ",
                                    name_udf(col("ФИО *")),
                                    phone_udf(col("Телефон мобильный")),
                                    lit("Контактное лицо"),
                                ),
                            ).otherwise(lit(None))
                        )
                    )
                ),
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("Последняя активность"), lit("%d.%m.%Y %H:%M")),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df = df1.unionAll(df2).unionAll(df3).unionAll(df4).unionAll(df5)

        df_with_birth_date = (
            df.filter(col("birth_date").isNotNull())
            .groupBy(["names", "birth_date"])
            .agg(
                first("sex").alias("sex"),
                first("birth_place").alias("birth_place"),
                first("relationship").alias("relationship"),
                array_compact(
                    array_distinct(flatten(collect_set(col("relations"))))
                ).alias("relations"),
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                max(col("actuality")).alias("actuality"),
                array_compact(
                    array_distinct(flatten(collect_set(col("raw_metadata"))))
                ).alias("raw_metadata"),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df_without_birth_date = (
            df.filter(col("birth_date").isNull())
            .groupBy(["names", "phones"])
            .agg(
                first("sex").alias("sex"),
                first("birth_place").alias("birth_place"),
                first("birth_date").alias("birth_date"),
                first("relationship").alias("relationship"),
                array_compact(
                    array_distinct(flatten(collect_set(col("relations"))))
                ).alias("relations"),
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                max(col("actuality")).alias("actuality"),
                array_compact(
                    array_distinct(flatten(collect_set(col("raw_metadata"))))
                ).alias("raw_metadata"),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "relationship",
                "relations",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_with_birth_date.unionAll(df_without_birth_date)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
