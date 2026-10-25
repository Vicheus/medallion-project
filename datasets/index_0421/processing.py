from pyspark import StorageLevel

from pyspark.sql.functions import when, col, lit, array, size, array_compact, concat_ws

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    birth_date_udf,
    phone_udf,
    email_udf,
    address_udf,
    name_udf,
    raw_metadata_udf,
    relations_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0421"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0421/raw/itlyceum.kz - @bereza_bd.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("ФИО Студента")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "phones",
                phone_udf(col("Телефон"), lit(self.dataset_country_code.value)),
            )
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("1С Идентификатор"),
                    col("1С Идентификатор"),
                    lit("Логин MyStat"),
                    col("Логин MyStat"),
                    lit("Пароль MyStat"),
                    col("Пароль MyStat"),
                    lit("MyStat"),
                    col("MyStat"),
                    lit("Поток"),
                    col("Поток"),
                    lit("Группа"),
                    col("Группа"),
                    lit("Форма обучения"),
                    col("Форма обучения"),
                    lit("Статус студента"),
                    col("Статус студента"),
                ),
            )
            .withColumn("relative_1_name", name_udf(col("ФИО Родственник 1")))
            .withColumn("relative_2_name", name_udf(col("ФИО Родственник 2")))
            .withColumn("relative_3_name", name_udf(col("ФИО Родственник 3")))
            .withColumn(
                "relations",
                when(
                    col("relative_1_name").isNotNull()
                    | col("relative_2_name").isNotNull()
                    | col("relative_3_name").isNotNull(),
                    array(
                        when(
                            col("relative_1_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("relative_1_name"),
                                    phone_udf(col("Домашний тел 1")),
                                    phone_udf(col("Мобильный тел 1")),
                                    phone_udf(col("Рабочий тел 1")),
                                    email_udf(col("Email Родственник 1")),
                                    col("Кем приходится 1"),
                                )
                            ),
                        ).otherwise(None),
                        when(
                            col("relative_2_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("relative_2_name"),
                                    phone_udf(col("Домашний тел 2")),
                                    phone_udf(col("Мобильный тел 2")),
                                    phone_udf(col("Рабочий тел 2")),
                                    email_udf(col("Email Родственник 2")),
                                    col("Кем приходится 2"),
                                )
                            ),
                        ).otherwise(None),
                        when(
                            col("relative_3_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("relative_3_name"),
                                    phone_udf(col("Домашний тел 3")),
                                    phone_udf(col("Мобильный тел 3")),
                                    phone_udf(col("Рабочий тел 3")),
                                    email_udf(col("Email Родственник 3")),
                                    col("Кем приходится 3"),
                                )
                            ),
                        ).otherwise(None),
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "relations",
                "raw_metadata",
            )
        )

        df = (
            df.withColumn(
                "relations",
                when(
                    size(array_compact(col("relations"))) > 0,
                    array_compact(col("relations")),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
                | col("address").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
