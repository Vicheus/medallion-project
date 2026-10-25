from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    size,
    regexp_replace,
    regexp_extract,
    struct,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
    sex_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.financials.udfs import (
    financial_card_number_udf,
    yandex_money_number_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0070"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0070/raw/OneClickMoney.ru_04.01.2024_9.8M.txt",
            sep=";",
            header=True,
        )

        doc_number_pattern = r"^\d+ \d+"
        doc_issue_date_pattern = r"\d{4}\-\d{2}\.\d{2}"
        doc_issued_by_pattern = r"Выдан:\s*([^К]*?)"
        doc_issued_by_code_pattern = r"(\d{3}-\d{3})"

        df = (
            df.replace("", None)
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(col("Адрес регистрации")),
                            address_udf(col("Фактический адрес")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("Телефон")),
                            phone_udf(col("Домашний телефон")),
                            phone_udf(col("Телефон работы")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "doc_number",
                regexp_replace(
                    regexp_extract(col("Паспорт"), doc_number_pattern, 0), " ", ""
                ),
            )
            .withColumn(
                "doc_issue_date",
                regexp_extract(col("Паспорт"), doc_issue_date_pattern, 0),
            )
            .withColumn(
                "doc_issued_by",
                regexp_extract(col("Паспорт"), doc_issued_by_pattern, 0),
            )
            .withColumn(
                "doc_issued_by_code",
                regexp_extract(col("Паспорт"), doc_issued_by_code_pattern, 0),
            )
            .withColumn(
                "yandex_money_number", yandex_money_number_udf(col("Яндекс кошелёк"))
            )
            .withColumn("card_number", financial_card_number_udf(col("Номер карты")))
            .withColumn(
                "works",
                when(
                    col("Место работы").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                lit(None),
                                lit(None),
                                col("Место работы"),
                                address_udf(
                                    when(
                                        col("Адрес места работы").isNotNull(),
                                        col("Адрес места работы"),
                                    )
                                ),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("doc_number").isNotNull(),
                    array_compact(
                        array(
                            document_udf(
                                lit(None),
                                col("doc_number"),
                                col("doc_issue_date"),
                                lit(None),
                                col("doc_issued_by"),
                                col("doc_issued_by_code"),
                                lit("yyyy-MM-dd"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("Skype").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Skype").isNotNull(),
                                social_udf(
                                    lit("Skype"), col("Skype"), lit(None), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull()
                    | col("yandex_money_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("card_number").isNotNull(),
                                struct(
                                    lit("Неопределенный банк").alias("title"),
                                    col("card_number").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Яндекс кошелёк").isNotNull(),
                                struct(
                                    lit("Яндекс кошелёк").alias("title"),
                                    yandex_money_number_udf(
                                        col("yandex_money_number")
                                    ).alias("card_number"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("Последний онлайн"), col("Дата регистрации")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Телефон близкого человека"),
                    col("Телефон близкого человека"),
                    lit("Телефон сожителя"),
                    col("Телефон сожителя"),
                    lit("Пенсионер"),
                    col("Пенсионер"),
                    lit("Доход семьи"),
                    col("Доход семьи"),
                ),
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "birth_date",
            "sex",
            "works",
            "documents",
            "socials",
            "financials",
            "actuality",
            "raw_metadata",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
