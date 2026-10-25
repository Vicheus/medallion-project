from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    greatest,
    lit,
    struct,
    array_compact,
    array,
    max,
    array_distinct,
    flatten,
    collect_list,
    size,
    when,
    regexp_replace,
    length,
    lower,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    name_parts_udf,
    actuality_date_udf,
    sex_udf,
    birth_date_udf,
    raw_metadata_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0607"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    raw_date_time_pattern = "%Y-%m-%d %H:%M:%S"

    ignore_names_stops = [
        "from site",
        "name",
        "none",
        "null",
        "user",
        "whatsapp",
        "xxx",
        "имя",
        "ип",
        "клиент",
        "купон",
        "не важно",
        "не указано",
        "неважно",
        "нет отчества",
        "нет отчество",
        "нет по паспорту",
        "нет",
        "нету",
        "отчество",
        "покупатель",
        "получатель",
        "сертификат",
        "телефон",
        "фамилия",
    ]
    ignore_names_stops_pattern = "|".join(ignore_names_stops)
    ignore_names = [
        "' -- whatsapp",
        "cafe",
        "couponnadibordo с сайта nadibordo.ru",
        "from site",
        "instagram",
        "pscoin",
        "sbs подарочный сертификат pro makeup руб",
        "telegram",
        "uabpo",
        "user",
        "whatsapp",
        "без имени",
        "входящий успешный",
        "входящий",
        "заказ в клик",
        "имени без",
        "инстаграм",
        "карта подарочная",
        "кк подарочный сертификат",
        "контакт контакт",
        "м подарочный сертификат",
        "неизвестен",
        "номинал подарочный сертификат",
        "отказ",
        "партнёра сертификат",
        "по заказу",
        "подарок",
        "подарочная",
        "подарочный . тг",
        "подарочный сертификат pro makeup руб",
        "подарочный сертификат pro makeup",
        "подарочный сертификат на руб",
        "подарочный сертификат р",
        "подарочный сертификат с",
        "подарочный сертификат ю",
        "подарочный сертификат",
        "подарочный",
        "пользовательс а",
        "с сайта сайта",
        "с сайта",
        "сертификат c",
        "сертификат в",
        "сертификат н",
        "сертификат нв",
        "сертификат партнёра",
        "сертификат подарочный",
        "сертификат р",
        "сертификат рублей",
        "сертификат",
        "сертификаты",
        "соси хуй",
        "телеграм",
        "уважаемый",
        "частное лицо",
        "частноелицо",
        "юридическое лицо",
    ]
    ignore_names_pattern = "|".join(ignore_names)
    ignore_metadata_values = [
        "created_by_bonuplus",
        "created_by_bonusplus",
        "без рассылки",
        "без уведомлений",
        "без уведомления",
        "для себя",
        "импорт",
        "интернет - поисковая строка",
        "лохушка",
        "мимо проходила",
        "мимо проходили",
        "мимо шла",
        "мимо",
        "обычная",
        "одежда",
        "покупатель",
        "просто",
        "профсоюз",
        "регистрация на сайте",
        "с уведомлением",
        "свет",
        "случайно",
        "хорошо  ( не доступен)",
    ]
    ignore_metadata_values_pattern = "|".join(ignore_metadata_values)

    def _prepare_data(self):
        return (
            self.read(
                path="bоnusрІus.prо - @StormBaseAdapter.csv", sep="\t", header=False
            )
            .select(
                col("_c0").alias("id"),
                col("_c2").alias("date1"),
                col("_c4").alias("phone"),
                col("_c5").alias("card"),
                col("_c9").alias("firstname"),
                col("_c10").alias("lastname"),
                col("_c11").alias("middlename"),
                col("_c12").alias("sex"),
                col("_c13").alias("birth"),
                col("_c14").alias("email"),
                col("_c15").alias("metadata"),
                col("_c30").alias("date2"),
                col("_c31").alias("date3"),
            )
            .replace("\\N", None)
            .filter(
                col("phone").rlike("^\\s*77\\d{9}\\s*$")
                | col("phone").rlike("^\\s*70\\d{8}\\s*$")
            )
            .withColumn(
                "firstname",
                regexp_replace(
                    lower(col("firstname")),
                    f"\\b({self.ignore_names_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn(
                "lastname",
                regexp_replace(
                    lower(col("lastname")),
                    f"\\b({self.ignore_names_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn(
                "middlename",
                regexp_replace(
                    lower(col("middlename")),
                    f"\\b({self.ignore_names_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn("firstname", regexp_replace("firstname", "\\d", ""))
            .withColumn("lastname", regexp_replace("lastname", "\\d", ""))
            .withColumn("middlename", regexp_replace("middlename", "\\d", ""))
            .withColumn("names", name_parts_udf("firstname", "lastname", "middlename"))
            .withColumn(
                "names",
                when(
                    lower(col("names")).rlike(f"^({self.ignore_names_pattern})$"),
                    lit(None),
                ).otherwise(col("names")),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array_compact(array(col("names")))),
            )
        )

    def _process_data(self, df):
        return (
            df.withColumn(
                "phones",
                array_compact(
                    array(phone_udf("phone", lit(self.dataset_country_code.value)))
                ),
            )
            .withColumn("emails", array_compact(array(email_udf("email"))))
            .withColumn("sex", sex_udf("sex"))
            .withColumn(
                "birth_date", birth_date_udf("birth", lit("%Y-%m-%d %H:%M:%S.%f"))
            )
            .withColumn(
                "actuality",
                greatest(
                    actuality_date_udf(col("date1"), lit(self.raw_date_time_pattern)),
                    actuality_date_udf(col("date2"), lit(self.raw_date_time_pattern)),
                    actuality_date_udf(col("date3"), lit(self.raw_date_time_pattern)),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("card").rlike("^\\d{4,}$"),
                    array_compact(
                        array(
                            struct(
                                lit("БонусПлюс").alias("title"),
                                lit("https://bonusplus.pro").alias("link"),
                                col("card").alias("client_card_number"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("metadata").isNotNull()
                    & (length(col("metadata")) > 3)
                    & (length(col("metadata")) < 151)
                    & ~lower(col("metadata")).rlike(
                        f"^\\s*({self.ignore_metadata_values_pattern})\\s*$"
                    ),
                    array_compact(
                        array(raw_metadata_udf(lit("_c15"), col("metadata")))
                    ),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "accounts",
                "actuality",
                "raw_metadata",
            )
        )

    def _group_data(self, df):
        null_df = df.filter(
            ~(
                col("sex").isNotNull()
                & col("birth_date").isNotNull()
                & (size(col("phones")) > 0)
            )
        )
        group_df = df.filter(
            (
                col("sex").isNotNull()
                & col("birth_date").isNotNull()
                & (size(col("phones")) > 0)
            )
        )

        df = (
            group_df.groupBy(["phones", "sex", "birth_date"])
            .agg(
                array_distinct(flatten(collect_list("names"))).alias("names"),
                array_distinct(flatten(collect_list("emails"))).alias("emails"),
                array_distinct(flatten(collect_list("accounts"))).alias("accounts"),
                array_distinct(flatten(collect_list("raw_metadata"))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .unionByName(null_df)
            .distinct()
        )

        return df

    def parser(self):
        prepared_df = self._prepare_data()
        prepared_df.persist(StorageLevel.DISK_ONLY).count()

        enriched_df = self._process_data(prepared_df)
        enriched_df.persist(StorageLevel.DISK_ONLY).count()
        prepared_df.unpersist()

        df = (
            self._group_data(enriched_df)
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
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .filter(col("names").isNotNull() & col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        enriched_df.unpersist()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
