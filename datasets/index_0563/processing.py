from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    when,
    regexp_extract,
    lit,
    array_distinct,
    array_compact,
    array,
    max,
    size,
    greatest,
    concat_ws,
    flatten,
    collect_list,
    coalesce,
    first,
    split,
    expr,
    regexp_replace,
    lower,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    actuality_date_udf,
    sex_udf,
    email_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0563"
    validate_invalid_groupping: bool = True

    name_ignore_pattern = r"\s[\d\.]+$"
    raw_date_time_pattern = "%Y-%m-%d %H:%M:%S"
    excluded_address_prefixes = [
        "австрия",
        "азербайджае",
        "азербайджан",
        "алжир",
        "америка",
        "армения",
        "афганистан",
        "бангладеш",
        "беларусь",
        "белоруссия",
        "белорусь",
        "бразилия",
        "великобритания",
        "веьтнам",
        "германия",
        "греция",
        "грузия",
        "египет",
        "израиль",
        "индонезия",
        "ирак",
        "италия",
        "йемен",
        "казахстан",
        "киргизия",
        "китай",
        "кндр пхеньян",
        "конго",
        "куба",
        "кыргизия",
        "кыргыстан",
        "кырыгызстан",
        "латвия",
        "ливия",
        "республика беларусь",
        "сша",
        "таджикистан",
        "тайланд",
        "туркменистан",
        "туркмения",
        "турция",
        "убекистан",
        "узбекистан",
        "украина",
        "эстония",
    ]
    excluded_address_prefixes_pattern = "^(" + "|".join(excluded_address_prefixes) + ")"
    excluded_addresses = [
        "д. корп. стр. кв. п. эт.",
        "не проживает",
        "общежитие",
        "гостиница",
    ]
    excluded_addresses_pattern = ",".join([f"'{w}'" for w in excluded_addresses])

    def _add_patient_phones_column(self, df):
        return (
            df.withColumn("phones_arr", split(col("Номер телефона"), ",|;|/"))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(expr("get(phones_arr, 0)")),
                            phone_udf(expr("get(phones_arr, 1)")),
                            phone_udf(expr("get(phones_arr, 2)")),
                            phone_udf("Номер телефона 2"),
                            phone_udf("Номер телефона 3"),
                        )
                    )
                ),
            )
            .drop("phones_arr")
        )

    def _add_patient_emails_column(self, df):
        return (
            df.withColumn("emails_arr", split(col("Почта"), ",|;|/"))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(expr("get(emails_arr, 0)")),
                            email_udf(expr("get(emails_arr, 1)")),
                            email_udf(expr("get(emails_arr, 2)")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails", expr("filter(emails, x -> NOT x like '%@clinicnacpp.ru')")
            )
            .drop("emails_arr")
        )

    def _read_incoming_calls(self):
        return self.read(path="Входящие звонки.csv", sep=";", header=False)

    def _read_sent_sms(self):
        return self.read(path="Отправленные SMS.csv", sep=";", header=False)

    def _read_calls(self):
        return self.read(path="Звонки.csv", sep=";", header=False)

    def _prepare_schedule(self):
        return self.read(path="Расписание.csv", sep=";", header=False)

    def _prepare_records(self):
        sex_regex = r"\((\W)\)\s*Дата"
        sex_second_regex = r"Пол\:\s*(\W)"
        birth_regex = r"Дата рождения:\s*(\d{2}\.\d{2}\.\d{4})"

        df = (
            self.read(path="Записи.csv", sep=";", header=True)
            .select(col("patient_id").alias("id"), "date1", "date2", "comment")
            .withColumn("sex", regexp_extract(col("comment"), sex_regex, 1))
            .withColumn(
                "sex",
                when(
                    col("sex") == "",
                    regexp_extract(col("comment"), sex_second_regex, 1),
                ).otherwise(col("sex")),
            )
            .withColumn("sex", sex_udf("sex"))
            .withColumn("birth", regexp_extract(col("comment"), birth_regex, 1))
            .withColumn(
                "actuality2",
                greatest(
                    actuality_date_udf(col("date1"), lit(self.raw_date_time_pattern)),
                    actuality_date_udf(col("date2"), lit(self.raw_date_time_pattern)),
                ),
            )
            .select("id", "sex", "birth", "actuality2")
        )

        return df

    def _prepare_patients(self):
        df = (
            self.read(path="Пациенты.csv", sep=";", header=True)
            .select(
                col("ID").alias("id"),
                "Фамилия",
                "Имя",
                "Отчество",
                "Дата рождения",
                "Почта",
                "Адрес",
                "Адрес 2",
                "СНИЛС",
                "Тип документа",
                "Серия документа",
                "Номер документа",
                "Дата выдачи документа",
                "Оделение выдачи документа",
                "Номер телефона",
                "Номер телефона 2",
                "Номер телефона 3",
                "Дата и время",
                "Дата и время 2",
                "Дата и время 3",
                col("_c26").alias("uuid"),
            )
            .filter(lower(col("Фамилия")) != "тестова")
            .withColumn(
                "Фамилия",
                when(lower(col("Фамилия")) == "нет", lit(None)).otherwise(
                    col("Фамилия")
                ),
            )
            .withColumn(
                "Имя",
                when(lower(col("Имя")) == "нет", lit(None)).otherwise(col("Имя")),
            )
            .withColumn(
                "Отчество",
                when(lower(col("Отчество")) == "нет", lit(None)).otherwise(
                    col("Отчество")
                ),
            )
            .withColumn(
                "Фамилия",
                regexp_replace("Фамилия", self.name_ignore_pattern, ""),
            )
            .withColumn(
                "Имя",
                regexp_replace("Имя", self.name_ignore_pattern, ""),
            )
            .withColumn(
                "Отчество",
                regexp_replace("Отчество", self.name_ignore_pattern, ""),
            )
            .withColumn(
                "names",
                name_parts_udf("Фамилия", "Имя", "Отчество"),
            )
            .filter(col("names").isNotNull())
            .withColumn("names", array(col("names")))
        )
        df = self._add_patient_emails_column(df)
        df = (
            self._add_patient_phones_column(df)
            .withColumn(
                "address",
                array_compact(
                    array_distinct(array(address_udf("Адрес"), address_udf("Адрес 2")))
                ),
            )
            .withColumn(
                "address",
                expr(
                    f"filter(address, x -> NOT lower(x) IN ({self.excluded_addresses_pattern}))"
                ),
            )
            .withColumn("birth_date", birth_date_udf("Дата рождения", lit("%Y-%m-%d")))
            .withColumn(
                "actuality",
                greatest(
                    actuality_date_udf(
                        col("Дата и время"), lit(self.raw_date_time_pattern)
                    ),
                    actuality_date_udf(
                        col("Дата и время 2"), lit(self.raw_date_time_pattern)
                    ),
                    actuality_date_udf(
                        col("Дата и время 3"), lit(self.raw_date_time_pattern)
                    ),
                ),
            )
            .withColumn(
                "Тип документа",
                when(
                    col("Тип документа").isNotNull(),
                    when(
                        col("Тип документа").isin(
                            ["3", "8", "18", "19", "20", "21", "27"]
                        ),
                        lit("паспорт гражданина рф"),
                    )
                    .when(
                        col("Тип документа") == "20",
                        when(
                            regexp_replace("Серия документа", " ", "").rlike(
                                "^[0-9]{4}$"
                            ),
                            lit("паспорт гражданина рф"),
                        ).when(
                            col("Серия документа").isin(["82", "83"]),
                            lit("вид на жительство"),
                        ),
                    )
                    .when(
                        col("Тип документа").isin(["9", "22"]),
                        lit("заграничный паспорт гражданина рф"),
                    )
                    .when(
                        col("Тип документа") == "10",
                        when(
                            regexp_replace("Серия документа", " ", "").rlike(
                                "^[0-9]{4}$"
                            )
                            & (col("Серия документа") != "1111"),
                            lit("паспорт гражданина рф"),
                        ).otherwise(lit("свидетельство о рождении")),
                    )
                    .when(
                        col("Тип документа") == "14",
                        lit("удостоверение личности военнослужащего"),
                    )
                    .when(
                        col("Тип документа").isin(["17", "29"]),
                        lit("свидетельство о рождении"),
                    )
                    .when(
                        col("Тип документа") == "18",
                        when(
                            regexp_replace("Серия документа", " ", "").rlike(
                                "^[0-9]{4}$"
                            ),
                            lit("паспорт гражданина рф"),
                        ).otherwise(lit("вид на жительство")),
                    )
                    .when(
                        col("Тип документа").isin(["1", "33"]),
                        lit("водительское удостоверение"),
                    )
                    .when(
                        col("Тип документа") == "25",
                        when(
                            col("Серия документа").isin(["82", "83"]),
                            lit("вид на жительство"),
                        )
                        .when(
                            regexp_replace("Серия документа", " ", "").rlike(
                                "^[0-9]{4}$"
                            ),
                            lit("паспорт гражданина рф"),
                        )
                        .when(
                            regexp_replace("Серия документа", " ", "").rlike(
                                "^[5-9][0-9]$"
                            ),
                            lit("заграничный паспорт гражданина рф"),
                        ),
                    ),
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("СНИЛС").isNotNull(),
                                document_udf(lit("снилс"), col("СНИЛС")),
                            ),
                            when(
                                col("Тип документа").isNotNull(),
                                document_udf(
                                    col("Тип документа"),
                                    concat_ws(
                                        "",
                                        col("Серия документа"),
                                        col("Номер документа"),
                                    ),
                                    col("Дата выдачи документа"),
                                    lit(None),
                                    col("Оделение выдачи документа"),
                                    lit(None),
                                    lit(self.raw_date_time_pattern),
                                ),
                            ),
                        )
                    )
                ),
            )
            .select(
                "id",
                "names",
                "phones",
                "emails",
                "documents",
                "address",
                "birth_date",
                "actuality",
            )
        )

        return df

    def parser(self):
        # holds only phones and dates that cannot be matched with names
        ignored_incoming_calls = self._read_incoming_calls()
        # holds only phones and dates that cannot be matched with names
        ignored_sent_sms = self._read_sent_sms()
        # quite often phones do not belong to names
        ignored_calls_df = self._read_calls()
        # quite often phones do not belong to names
        ignored_schedule_df = self._prepare_schedule()

        records_df = self._prepare_records()
        patients_df = self._prepare_patients()

        records_df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            patients_df.join(records_df, on="id", how="left")
            .withColumn(
                "birth_date",
                when(
                    col("birth_date").isNull(),
                    birth_date_udf("birth", lit("%d.%m.%Y")),
                ).otherwise(col("birth_date")),
            )
            .withColumn("actuality", coalesce(col("actuality"), col("actuality2")))
            .drop("id", "birth", "actuality2")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        records_df.unpersist()

        null_df = df.filter(size(col("phones")) == 0)
        phones_df = df.filter(size(col("phones")) > 0)

        df = (
            phones_df.groupBy("names", "phones")
            .agg(
                array_distinct(flatten(collect_list("emails"))).alias("emails"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                max(col("actuality")).alias("actuality"),
            )
            .unionByName(null_df, allowMissingColumns=True)
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
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("phones").isNull()
                    & col("documents").isNull()
                    & (size(col("address")) == 1),
                    expr(
                        f"filter(address, x -> NOT lower(x) RLIKE '{self.excluded_address_prefixes_pattern}')"
                    ),
                ).otherwise(col("address")),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (
                    col("phones").isNotNull()
                    | col("emails").isNotNull()
                    | col("address").isNotNull()
                    | col("documents").isNotNull()
                )
            )
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
