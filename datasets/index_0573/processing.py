import re
from typing import Optional

from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    array,
    array_compact,
    lit,
    when,
    udf,
    size,
    max,
    lower,
    try_element_at,
    split,
    expr,
    concat_ws,
    array_distinct,
    flatten,
    collect_list,
    trim,
)
from pyspark.sql.types import StringType, ArrayType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    name_udf,
    actuality_date_udf,
    address_udf,
    email_udf,
)
from parsetron.sections.work.udfs import work_udf

months = {
    "января": "01",
    "февраля": "02",
    "марта": "03",
    "апреля": "04",
    "мая": "05",
    "июня": "06",
    "июля": "07",
    "августа": "08",
    "сентября": "09",
    "октября": "10",
    "ноября": "11",
    "декабря": "12",
}


def date(value: str) -> Optional[str]:
    if value and re.match(r"^\d{1,2}", value):
        day, month, year, _ = value.split()
        parsed = f"{year}-{months[month]}-{day}"
        return parsed
    return None


cyrillic_date_udf = udf(date, StringType())


def filter_relations(names, phones, relations):
    filtered_results = []

    if not names or not phones or not relations:
        return None

    for relation in relations:
        match_found = False

        for name in names:
            for phone in phones:
                if relation.startswith(f"{name} {phone} "):
                    match_found = True
                    break
            if match_found:
                break
        if not match_found:
            filtered_results.append(relation)

    return filtered_results


filter_relations_udf = udf(filter_relations, ArrayType(StringType()))


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0573"
    validate_invalid_groupping: bool = True

    filter_company_words = ("ип", "и.п.", "индивидуальный предприниматель")
    ignore_company_words = (
        "плательщик",
        "никончук василий андреевич",
        "стасевич евгений алерьевич",
    )
    ignore_fio_words = [
        "afdsf",
        "aliaksandr karliuk",
        "bdfy",
        "cnhf nfvfhf fktrcttdyf",
        "cnhf nfvfhf",
        "dkfl",
        "fghfdgsdfsd",
        "gtnh",
        "gtnhjd",
        "hrjttjgyf",
        "lazurit.com",
        "tktyf",
        "xdgh",
        "без имени",
        "дежурный работник склада",
        "жщошзлжщ",
        "зав складом",
        "запрос",
        "исполнитель",
        "кладовщик",
        "консультант",
        "контакт менеджер",
        "контакт",
        "контакт.центр",
        "контактное лицо",
        "контактное лицо заказчика",
        "контактное лицо на загрузке",
        "кто ответит",
        "кто поднимет трубку",
        "кто поднимет",
        "кто-нибудь",
        "кто-то",
        "лпшщгр",
        "любой работник склада",
        "любой специалист",
        "менеджер",
        "менежджер",
        "не известно",
        "неив.",
        "неизв.",
        "неизвест.",
        "неизвестно.",
        "неизвестны",
        "оао коминтерн",
        "общий",
        "ответственное лицо",
        "отдел закупок",
        "отдел комплектации",
        "отдел логистики",
        "отдел око",
        "отдел омтс",
        "отдел продаж",
        "отдел работы с клиентами",
        "отдел сбыта",
        "приемка",
        "работник склада",
        "работника склада",
        "русдюбель",
        "сервис без определенного лица",
        "сервис наколесах",
        "склад",
        "сортировочный центр wildberries",
        "сотрудник склада",
        "сотрудник",
        "сотрудники деловых линий",
        "спрлрпл",
        "тат - склад",
        "тел.склада",
        "телеграм",
        "телефон магазина любой менеджер",
        "телефон офиса",
        "тк деловые линии",
        "тот кто поднимет. у них передают телефон.",
        "тпг северо-западный союз",
        "цукп",
        "частное предприятие высокий потенциал",
        "чвмпчвчв",
        "ыфвфыв фывф фыв",
        "яты чвтыо вто",
    ]
    ignore_fio_parts = (
        "общий забрать товар",
        "общество с ограниченной ответственностью",
        "ооо",
        "телефон склада",
        "спа-салон элеганс",
    )

    def _add_relations_column(self, df):
        return df.withColumn(
            "relations",
            array_compact(
                array(
                    when(
                        col("payer_names").isNotNull()
                        & col("payer_phones").isNotNull(),
                        concat_ws(
                            " ",
                            try_element_at(col("payer_names"), lit(1)),
                            try_element_at(col("payer_phones"), lit(1)),
                            lit("Плательщик"),
                        ),
                    ),
                    when(
                        col("sender_names").isNotNull()
                        & col("sender_phones").isNotNull(),
                        concat_ws(
                            " ",
                            try_element_at(col("sender_names"), lit(1)),
                            try_element_at(col("sender_phones"), lit(1)),
                            lit("Отправитель"),
                        ),
                    ),
                    when(
                        col("recipient_names").isNotNull()
                        & col("recipient_phones").isNotNull(),
                        concat_ws(
                            " ",
                            try_element_at(col("recipient_names"), lit(1)),
                            try_element_at(col("recipient_phones"), lit(1)),
                            lit("Получатель"),
                        ),
                    ),
                )
            ),
        )

    def _add_documents_column(self, df):
        return (
            df.withColumn(
                "inns",
                split(col("payer_inn"), "/"),
            )
            .withColumn(
                "payer_documents",
                array_compact(
                    array(
                        document_udf(lit("инн"), expr("get(inns, 0)")),
                        document_udf(lit("инн"), expr("get(inns, 1)")),
                    )
                ),
            )
            .withColumn(
                "payer_documents",
                when(
                    size(col("payer_documents")) > 0, col("payer_documents")
                ).otherwise(None),
            )
        )

    def _add_phones_column(self, df, phone_col_title, res_col_title):
        return df.withColumn(
            "phones_arr", split(col(phone_col_title), "\\+")
        ).withColumn(
            res_col_title,
            array_compact(
                array(
                    phone_udf(expr("get(phones_arr, 0)")),
                    phone_udf(expr("get(phones_arr, 1)")),
                    phone_udf(expr("get(phones_arr, 2)")),
                )
            ),
        )

    def _add_works_column(self, df, org_col_title, fio_col_title, res_col_title):
        return df.withColumn(
            res_col_title,
            when(
                col(org_col_title).isNotNull()
                & ~lower(col(org_col_title)).rlike(
                    f"^\\s*({"|".join(self.ignore_company_words)})\\s*$"
                )
                & (
                    lower(col(org_col_title))
                    != lower(try_element_at(col(fio_col_title), lit(1)))
                ),
                array_compact(
                    array(
                        when(
                            lower(col(org_col_title)).rlike(
                                f"^\\s*({"|".join(self.filter_company_words)})\\b"
                            ),
                            work_udf(post=col(org_col_title)),
                        ).otherwise(work_udf(company=col(org_col_title)))
                    )
                ),
            ).otherwise(None),
        ).withColumn(
            res_col_title,
            when(size(col(res_col_title)) > 0, col(res_col_title)).otherwise(None),
        )

    def _add_fio(self, df, fio_col_title, res_col_title):
        return df.withColumn(res_col_title, name_udf(col(fio_col_title))).withColumn(
            res_col_title,
            when(
                col(res_col_title).isNotNull()
                & ~lower(trim(col(res_col_title))).isin(self.ignore_fio_words)
                & ~lower(col(res_col_title)).rlike(
                    f"^\\s*({"|".join(self.ignore_fio_parts)})\\b"
                ),
                array_compact(array(col(res_col_title))),
            ).otherwise(None),
        )

    def _prepare_raw_data(self, df):
        df = self._add_fio(df, "payer_contact_person", "payer_names")
        df = self._add_fio(df, "sender_contact_person", "sender_names")
        df = self._add_fio(df, "recipient_contact_person", "recipient_names")
        df = (
            df.withColumn(
                "payer_emails",
                array_compact(array(email_udf(col("payer_contact_person_email")))),
            )
            .withColumn(
                "recipient_addresses",
                array_compact(array(address_udf(col("delivery_address")))),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    cyrillic_date_udf(col("pickup_date")), lit("%Y-%m-%d")
                ),
            )
        )

        df = self._add_phones_column(df, "payer_contact_person_phone", "payer_phones")
        df = self._add_phones_column(df, "sender_contact_phone", "sender_phones")
        df = self._add_phones_column(df, "recipient_contact_phone", "recipient_phones")
        df = self._add_documents_column(df)
        df = (
            df.withColumn(
                "payer_names",
                when(size(col("payer_names")) > 0, col("payer_names")).otherwise(None),
            )
            .withColumn(
                "sender_names",
                when(size(col("sender_names")) > 0, col("sender_names")).otherwise(
                    None
                ),
            )
            .withColumn(
                "recipient_names",
                when(
                    size(col("recipient_names")) > 0, col("recipient_names")
                ).otherwise(None),
            )
            .withColumn(
                "payer_emails",
                when(size(col("payer_emails")) > 0, col("payer_emails")).otherwise(
                    None
                ),
            )
            .withColumn(
                "payer_phones",
                when(size(col("payer_phones")) > 0, col("payer_phones")).otherwise(
                    None
                ),
            )
            .withColumn(
                "sender_phones",
                when(size(col("sender_phones")) > 0, col("sender_phones")).otherwise(
                    None
                ),
            )
            .withColumn(
                "recipient_phones",
                when(
                    size(col("recipient_phones")) > 0, col("recipient_phones")
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = self._add_works_column(df, "payer", "payer_names", "payer_works")
        df = self._add_works_column(df, "sender", "sender_names", "sender_works")
        df = self._add_works_column(
            df, "recipient", "recipient_names", "recipient_works"
        )
        df = self._add_documents_column(df)
        df = self._add_relations_column(df).select(
            "payer_names",
            "payer_documents",
            "payer_emails",
            "payer_phones",
            "payer_works",
            "sender_names",
            "sender_phones",
            "sender_works",
            "recipient_names",
            "recipient_phones",
            "recipient_addresses",
            "recipient_works",
            "actuality",
            "relations",
        )

        return df

    def _read_df(self, filename):
        return self.read(path=filename, sep=";", header=True).drop(
            "cargo_description",
            "volume",
            "total_weight",
            "number_of_packages",
            "delivery_type",
            "additional_info",
            "source_file",
        )

    def _form_data(self, df):
        payer_df = df.select(
            col("payer_names").alias("names"),
            col("payer_emails").alias("emails"),
            col("payer_phones").alias("phones"),
            col("payer_works").alias("works"),
            col("payer_documents").alias("documents"),
            col("actuality"),
            col("relations"),
        )
        sender_df = df.select(
            col("sender_names").alias("names"),
            col("sender_phones").alias("phones"),
            col("sender_works").alias("works"),
            col("actuality"),
            col("relations"),
        )
        recipient_df = df.select(
            col("recipient_names").alias("names"),
            col("recipient_phones").alias("phones"),
            col("recipient_addresses").alias("address"),
            col("recipient_works").alias("works"),
            col("actuality"),
            col("relations"),
        )

        joined_df = (
            payer_df.unionByName(sender_df, allowMissingColumns=True)
            .unionByName(recipient_df, allowMissingColumns=True)
            .filter(col("names").isNotNull() & col("phones").isNotNull())
        )

        return joined_df

    def _group_data(self, df):
        null_df = df.filter(col("phones").isNull())
        phone_df = df.filter(col("phones").isNotNull())

        df = (
            phone_df.groupBy("names", "phones")
            .agg(
                array_distinct(flatten(collect_list("emails"))).alias("emails"),
                array_distinct(flatten(collect_list("works"))).alias("works"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("relations"))).alias("relations"),
                max(col("actuality")).alias("actuality"),
            )
            .unionByName(null_df, allowMissingColumns=True)
        )

        null_df = df.filter(~(col("emails").isNotNull() & col("phones").isNull()))
        emails_df = df.filter(col("emails").isNotNull() & col("phones").isNull())

        df = (
            emails_df.groupBy("names", "emails")
            .agg(
                array_distinct(flatten(collect_list("works"))).alias("works"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("relations"))).alias("relations"),
                max(col("actuality")).alias("actuality"),
            )
            .unionByName(null_df, allowMissingColumns=True)
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "works",
                when(size(col("works")) > 0, col("works")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "relations",
                filter_relations_udf("names", "phones", "relations"),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("phones").isNotNull() | col("documents").isNotNull())
            )
        )

        return df

    def parser(self):
        first_df = self._read_df("pdfs1.csv")
        second_df = self._read_df("pdfs2.csv")
        third_df = self._read_df("pdfs3.csv")

        joined_df = first_df.unionByName(
            second_df, allowMissingColumns=True
        ).unionByName(third_df, allowMissingColumns=True)

        prepared_df = self._prepare_raw_data(joined_df)

        prepared_df.persist(StorageLevel.DISK_ONLY).count()

        formed_df = self._form_data(prepared_df)

        formed_df.persist(StorageLevel.DISK_ONLY).count()
        prepared_df.unpersist()

        grouped_df = self._group_data(formed_df)

        grouped_df.persist(StorageLevel.DISK_ONLY).count()
        formed_df.unpersist()

        return grouped_df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
