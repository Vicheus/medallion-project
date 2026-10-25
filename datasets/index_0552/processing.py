from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    lit,
    array,
    array_compact,
    when,
    size,
    lower,
    concat_ws,
    collect_list,
    flatten,
    array_distinct,
    substring_index,
    try_element_at,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    name_udf,
    email_udf,
    address_udf,
    relations_udf,
    birth_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0552"
    validate_invalid_groupping: bool = True

    ignore_email_patterns = [
        "kmarchenkov@kdl.ru",
        "okorabenkov@kdl.ru",
        "test2@test.ru",
        "test@test.ru",
        "ebal@vash.rot",
    ]
    ignore_org_stop_words = [
        "-",
        "--",
        "---",
        "-/-",
        "\\+\\+\\+",
        "\\.",
        "kdlв",
        "аренда от собственника",
        "аренда помещений",
        "аренда",
        "без названия",
        "блогер",
        "высшее",
        "газизов нияз вилевич",
        "группа компаний",
        "декрет",
        "запрос на франшизу",
        "интересует франшиза",
        "кдл",
        "клиника",
        "на стадии организации",
        "на стадии открытия",
        "не имею",
        "неиз",
        "нет",
        "нету",
        "онлайн прием",
        "онлайн",
        "ооо",
        "оформление входной группы при открытии вашего филиала",
        "предложение аренды, город железнодорожный",
        "предложение о сотрудничестве",
        "предложение сотрудничества по рекламе",
        "работаю онлайн",
        "сайты",
        "самоазанятый",
        "самозанятая",
        "самозанятость",
        "самозанятый",
        "своё дело",
        "сдам в аренду 60кв.м. в новороссийске",
        "сибирь",
        "собственник отдельно стоящего здания",
        "стоматология",
        "студия красоты",
        "физ лицо",
        "физ.лицо",
        "физическое лицо",
        "физлицо владелец помещения",
        "франшиза",
        "хочу предложить вам помещение в жк семеновский парк. москва",
        "частная практика",
        "частная",
        "частное лицо",
        "частный медцентр",
        "частный специалист",
        "ю",
    ]

    def _add_works_column(self, df):
        return df.withColumn(
            "works",
            when(
                col("organization").isNotNull()
                & ~lower(col("organization")).rlike(
                    f"^\\s*({"|".join(self.ignore_org_stop_words)})\\s*$"
                ),
                when(
                    lower(col("organization")).rlike(
                        r"^\s*(ип|и.п.|индивидуальный предприниматель|пока ип)\b"
                    ),
                    array_compact(
                        array(
                            work_udf(
                                col("organization"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ).otherwise(
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                lit(None),
                                lit(None),
                                col("organization"),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            ).otherwise(None),
        )

    def _prepare_corporate(self, filename: str):
        df = (
            self.read(path=filename, sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
        )

        df = (
            self._add_works_column(df)
            .select("names", "emails", "phones", "works")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        return df

    def _prepare_corporate_private_medical_center(self):
        return self._prepare_corporate("corporate-private-medical-center.csv")

    def _prepare_corporate_state_customer(self):
        return self._prepare_corporate("corporate-state-customer.csv")

    def _prepare_doctor_cooperation(self):
        df = (
            self.read(path="doctor-cooperation.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn(
                "works",
                array_compact(
                    array(
                        work_udf(
                            when(
                                col("spec").isNull()
                                | lower(col("spec")).rlike(
                                    f"^\\s*({"|".join(self.ignore_org_stop_words)})\\s*$"
                                ),
                                lit(None),
                            ).otherwise(col("spec")),
                            lit(None),
                            lit(None),
                            when(
                                col("lpu").isNull()
                                | lower(col("lpu")).rlike(
                                    f"^\\s*({"|".join(self.ignore_org_stop_words)})\\s*$"
                                )
                                | col("lpu").startswith("Добрый день!"),
                                lit(None),
                            ).otherwise(col("lpu")),
                            lit(None),
                            lit(None),
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "works")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "works",
                when(size(col("works")) > 0, col("works")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        return df

    def _prepare_feedback(self, filename: str):
        df = (
            self.read(path=filename, sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .select("names", "emails", "phones")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        return df

    def _prepare_feedback_commend(self):
        return self._prepare_feedback("feedback-commend.csv")

    def _prepare_feedback_pay_error(self):
        return self._prepare_feedback("feedback-pay-error.csv")

    def _prepare_feedback_prices(self):
        return self._prepare_feedback("feedback-prices.csv")

    def _prepare_feedback_question(self):
        return self._prepare_feedback("feedback-question.csv")

    def _prepare_feedback_report(self):
        return self._prepare_feedback("feedback-report.csv")

    def _prepare_feedback_transcript(self):
        return self._prepare_feedback("feedback-transcript.csv")

    def _prepare_home_order(self):
        df = (
            self.read(path="home-order.csv", sep=",", header=True)
            .select("fio", "phone", "region")
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .select("names", "phones")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(col("names").isNotNull() & col("phones").isNotNull())
            .distinct()
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df

    def _prepare_make_covid(self):
        df = (
            self.read(path="make-covid.csv", sep=",", header=True)
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .select("names", "phones")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(col("names").isNotNull() & col("phones").isNotNull())
            .distinct()
        )

        return df

    def _prepare_patient_ask(self):
        df = (
            self.read(path="patient-ask.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn(
                "emails",
                array_compact(
                    array(email_udf(col("email")), email_udf(col("address")))
                ),
            )
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn("address", array_compact(array(address_udf(col("address")))))
            .select("names", "emails", "phones", "address")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        return df

    def _prepare_patient_corporate_health_card(self):
        df = (
            self.read(path="patient-corporate-health-card.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
        )

        df = (
            self._add_works_column(df)
            .select("names", "emails", "phones", "works")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "works",
                when(size(col("works")) > 0, col("works")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        return df

    def _prepare_tax_help(self):
        df = (
            self.read(path="tax-help.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("fio_tax", name_udf(col("fio_tax")))
            .filter(col("fio_tax").isNotNull())
            .withColumn("fio", name_udf(col("fio")))
            .withColumn("birth", birth_date_udf(col("birth"), lit("%d.%m.%Y")))
            .withColumn("names", array_compact(array(col("fio_tax"))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn(
                "documents", array_compact(array(document_udf(lit("инн"), col("inn"))))
            )
            .withColumn(
                "birth_date",
                when(col("fio") == col("fio_tax"), col("birth")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    (col("fio") != col("fio_tax"))
                    & col("birth").isNotNull()
                    & try_element_at(col("documents"), lit(1))["serial"].isNotNull(),
                    array_compact(
                        array(relations_udf(concat_ws(" ", col("fio"), col("birth"))))
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "birth_date", "documents", "relations")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("documents").isNotNull())
            )
            .distinct()
        )
        dependent_df = (
            self.read(path="tax-help.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("fio", name_udf(col("fio")))
            .filter(col("fio").isNotNull())
            .withColumn("fio_tax", name_udf(col("fio_tax")))
            .filter(col("fio") != col("fio_tax"))
            .withColumn("names", array_compact(array(col("fio"))))
            .withColumn("birth_date", birth_date_udf(col("birth"), lit("%d.%m.%Y")))
            .withColumn(
                "documents", array_compact(array(document_udf(lit("инн"), col("inn"))))
            )
            .withColumn(
                "relations",
                when(
                    col("fio_tax").isNotNull()
                    & col("birth_date").isNotNull()
                    & try_element_at(col("documents"), lit(1))["serial"].isNotNull(),
                    array_compact(
                        array(
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("fio_tax"),
                                    try_element_at(col("documents"), lit(1))["serial"],
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "birth_date", "relations")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .filter(col("names").isNotNull() & col("relations").isNotNull())
            .distinct()
        )

        df = df.unionByName(dependent_df, allowMissingColumns=True)
        df.persist(StorageLevel.DISK_ONLY).count()

        return df

    def _prepare_vacancy(self):
        ignore_history_stop_words = [
            "прикрепила выше",
            "указал в резюме",
            "в резюме",
            "указано в резюме.",
        ]
        df = (
            self.read(path="vacancy.csv", sep=",", header=True)
            .filter(~col("email").rlike(f"{'|'.join(self.ignore_email_patterns)}"))
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn(
                "birth",
                when(
                    col("birth").isNotNull(), substring_index(col("birth"), " ", 1)
                ).otherwise(None),
            )
            .withColumn("birth_date", birth_date_udf(col("birth"), lit("%d.%m.%Y")))
            .withColumn(
                "birth_date",
                when(
                    col("birth_date").isNull() & col("birth").isNotNull(),
                    birth_date_udf(col("birth"), lit("%d%m%Y")),
                ).otherwise(col("birth_date")),
            )
            .withColumn(
                "birth_date",
                when(
                    col("birth_date").isNull() & col("birth").isNotNull(),
                    birth_date_udf(col("birth"), lit("%d.%m.%y")),
                ).otherwise(col("birth_date")),
            )
            .withColumn(
                "raw_metadata",
                when(
                    lower(col("history")).rlike(
                        f"^\\s*({"|".join(ignore_history_stop_words)})\\s*$"
                    ),
                    lit(None),
                ).otherwise(
                    array_compact(
                        array(raw_metadata_udf(lit("history"), col("history")))
                    )
                ),
            )
            .select("names", "emails", "phones", "birth_date", "raw_metadata")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | (col("phones").isNotNull()))
            )
            .distinct()
        )

        return df

    def parser(self):
        df = (
            self._prepare_corporate_private_medical_center()
            .unionByName(self._prepare_corporate_state_customer())
            .unionByName(self._prepare_doctor_cooperation())
            .unionByName(self._prepare_feedback_commend(), True)
            .unionByName(self._prepare_feedback_pay_error(), True)
            .unionByName(self._prepare_feedback_prices(), True)
            .unionByName(self._prepare_feedback_question(), True)
            .unionByName(self._prepare_feedback_report(), True)
            .unionByName(self._prepare_feedback_transcript(), True)
            .unionByName(self._prepare_home_order(), True)
            .unionByName(self._prepare_make_covid(), True)
            .unionByName(self._prepare_patient_ask(), True)
            .unionByName(self._prepare_patient_corporate_health_card(), True)
            .unionByName(self._prepare_tax_help(), True)
            .unionByName(self._prepare_vacancy(), True)
            .distinct()
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        null_df = df.filter(col("emails").isNull() | col("phones").isNull())
        email_phone_df = df.filter(
            col("emails").isNotNull() & col("phones").isNotNull()
        )
        email_phone_df = email_phone_df.groupBy("emails", "phones").agg(
            array_distinct(flatten(collect_list("names"))).alias("names"),
            array_distinct(flatten(collect_list("works"))).alias("works"),
            array_distinct(flatten(collect_list("address"))).alias("address"),
            array_distinct(flatten(collect_list("documents"))).alias("documents"),
            array_distinct(flatten(collect_list("relations"))).alias("relations"),
            array_distinct(flatten(collect_list("raw_metadata"))).alias("raw_metadata"),
        )

        grouped_df = null_df.unionByName(email_phone_df, True)
        grouped_df.persist(StorageLevel.DISK_ONLY).count()
        df.unpersist()

        null_df = grouped_df.filter(col("birth_date").isNull())
        date_df = grouped_df.filter(col("birth_date").isNotNull())

        df = (
            date_df.groupBy("names", "birth_date")
            .agg(
                array_distinct(flatten(collect_list("emails"))).alias("emails"),
                array_distinct(flatten(collect_list("phones"))).alias("phones"),
                array_distinct(flatten(collect_list("works"))).alias("works"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                array_distinct(flatten(collect_list("relations"))).alias("relations"),
                array_distinct(flatten(collect_list("raw_metadata"))).alias(
                    "raw_metadata"
                ),
            )
            .unionByName(null_df)
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "works",
                when(size(col("works")) > 0, col("works")).otherwise(None),
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
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .filter(
                col("names").isNotNull()
                & (
                    col("emails").isNotNull()
                    | col("phones").isNotNull()
                    | col("relations").isNotNull()
                    | col("documents").isNotNull()
                )
            )
        )
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
