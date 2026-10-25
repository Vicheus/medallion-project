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
from parsetron.settings import DATASET_COUNTRY_CODE


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0600"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    raw_date_time_pattern = "%Y-%m-%d %H:%M:%S"

    def _add_patient_phones_column(self, df):
        return (
            df.withColumn("phones_arr", split(col("Номер телефона"), ",|;|/"))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                expr("get(phones_arr, 0)").isNotNull()
                                & phone_udf(expr("get(phones_arr, 0)")).isNull(),
                                phone_udf(
                                    expr("get(phones_arr, 0)"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                expr("get(phones_arr, 1)").isNotNull()
                                & phone_udf(expr("get(phones_arr, 1)")).isNull(),
                                phone_udf(
                                    expr("get(phones_arr, 1)"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                expr("get(phones_arr, 2)").isNotNull()
                                & phone_udf(expr("get(phones_arr, 2)")).isNull(),
                                phone_udf(
                                    expr("get(phones_arr, 2)"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                col("Номер телефона 2").isNotNull()
                                & phone_udf(col("Номер телефона 2")).isNull(),
                                phone_udf(
                                    col("Номер телефона 2"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                col("Номер телефона 3").isNotNull()
                                & phone_udf(col("Номер телефона 3")).isNull(),
                                phone_udf(
                                    col("Номер телефона 3"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
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
                    f"filter(address, x -> NOT lower(x) IN ('д. корп. стр. кв. п. эт.'))"
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
                "documents",
                when(
                    col("Тип документа").isNotNull()
                    & col("Тип документа").isin(["16", "26"]),
                    array_compact(
                        array(
                            document_udf(
                                lit("паспорт гражданина рк"),
                                concat_ws(
                                    "",
                                    col("Серия документа"),
                                    col("Номер документа"),
                                ),
                                col("Дата выдачи документа"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(self.raw_date_time_pattern),
                                lit(self.dataset_country_code.value),
                            ),
                        )
                    ),
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
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("phones").isNotNull() | col("documents").isNotNull())
            )
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
