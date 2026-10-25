from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    array_sort,
    coalesce,
    col,
    collect_set,
    filter,
    flatten,
    length,
    lit,
    lower,
    max,
    regexp_replace,
    size,
    split,
    transform,
    trim,
    udf,
    when,
)
from pyspark.sql.types import StringType

from parsetron import Parsetron
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    address_udf,
    birth_date_udf,
    email_udf,
    name_parts_udf,
    phones_udf,
    raw_metadata_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


def _preprocess_phones(df: DataFrame, res_col: str, input_col: str) -> DataFrame:
    return df.withColumn(res_col, split(col(input_col), lit(";"))).withColumn(
        res_col,
        transform(
            res_col,
            lambda x: when(
                ~trim(x).rlike(r"\s"),
                regexp_replace(trim(x), r"\D+$", ""),
            ).otherwise(x),
        ),
    )


def parse_date(date_str: str):
    if not date_str:
        return None

    months = {
        "января": 1,
        "февраля": 2,
        "марта": 3,
        "апреля": 4,
        "мая": 5,
        "июня": 6,
        "июля": 7,
        "августа": 8,
        "сентября": 9,
        "октября": 10,
        "ноября": 11,
        "декабря": 12,
    }

    try:
        parts = date_str.split()
        day = int(parts[0])
        month_name = parts[1].lower()
        year = int(parts[2])
        month = months[month_name]
        return f"{day}.{month}.{year}"
    except:
        return None


parse_date_udf = udf(parse_date, StringType())


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0665"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY
    languages_list = [
        "arabic",
        "english",
        "finnish",
        "french",
        "japanies",
        "korean",
        "tureckiy",
        "аварский",
        "адыгейский",
        "азербайджанский",
        "английский",
        "арабский",
        "армянский",
        "белорусский",
        "болгарский",
        "бурятский",
        "голландский",
        "греческий",
        "грузинский",
        "иврит",
        "ингушский",
        "индийский",
        "иранский",
        "испанский",
        "итальянский",
        "кабардинский",
        "казахский",
        "китайский",
        "корейский",
        "кыргызский",
        "латинский",
        "латынь",
        "латышский",
        "литовский",
        "молдавский",
        "монгольский",
        "мордовский",
        "немецкий",
        "норвежский",
        "осетинский",
        "персидский",
        "польский",
        "португальский",
        "румынский",
        "русский",
        "сербский",
        "словацкий",
        "таджикский",
        "татарский",
        "тувинский",
        "турецкий",
        "туркменский",
        "удмуртский",
        "узбекский",
        "укранский",
        "фарси",
        "финский",
        "французский",
        "хакасский",
        "чеченский",
        "чешский",
        "чувашский",
        "шведский",
        "эстонский",
        "язык жестов",
        "якутский",
        "японский",
    ]
    languages_regex = "(" + "|".join(languages_list) + ")"

    def parser(self):
        df1 = self.read(path="resume.csv", sep="|", header=True).select(
            "Имя",
            "Фамилия",
            "Отчество",
            "Дата рождения",
            "Телефон 1",
            "Телефон 2",
            "Телефон 3",
            "E-mail",
            "Город",
            "Образование",
            "Иностранный язык",
            "Дата резюме",
            "Гражданство",
        )
        df2 = self.read(path="resume_2.csv", sep="|", header=True).select(
            "Имя",
            "Фамилия",
            "Отчество",
            "Дата рождения",
            col("Телефон").alias("Телефон 1"),
            "E-mail",
            "Город",
            "Образование",
            "Иностранный язык",
            "Дата резюме",
            "Гражданство",
        )
        df = (
            df1.unionByName(df2, allowMissingColumns=True)
            .replace(["", " ", ".", "-", ";", "нет", "Нет", "НЕТ"], None)
            .filter(
                lower(regexp_replace(trim(col("Гражданство")), r"\.$", "")).isin(
                    [
                        "belarus",
                        "беларусь",
                        "белорусь",
                        "белоруска",
                        "рб",
                        "республика беларусь",
                        "республика белорусь",
                        "берарус",
                        "белорус",
                        "беларусское",
                        "беларусия",
                        "р. беларусь",
                    ]
                )
                | lower(
                    regexp_replace(trim(col("Гражданство")), r"\.$", "")
                ).startswith("беларусь")
                | (
                    lower(trim(col("E-mail"))).endswith(".by")
                    & ~(
                        lower(trim(col("Гражданство"))).isin(
                            [
                                "спб",
                                "санкт-петербург",
                                "москва",
                                "рф",
                                "российское",
                                "руский",
                                "руская",
                                "русский",
                                "русская",
                                "россия",
                                "русское",
                            ]
                        )
                        | lower(col("Гражданство")).contains("рф")
                        | lower(col("Гражданство")).contains("российское")
                        | lower(col("Гражданство")).contains("русское")
                        | lower(trim(col("Город"))).isin(
                            [
                                "москва",
                                "moscow",
                                "волгоград",
                                "смоленск",
                                "московская область",
                                "санкт-петербург",
                                "спб",
                                "новосибирск",
                                "г. москва",
                                "ростов-на-дону",
                                "казань",
                            ]
                        )
                    )
                )
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("Имя"),
                    when(
                        (length(col("Фамилия")) > 2)
                        & (size(array_distinct(split(col("Фамилия"), ""))) == 1),
                        lit(None),
                    ).otherwise(col("Фамилия")),
                    col("Отчество"),
                ),
            )
            .filter(col("names").isNotNull())
            .withColumn("names", array_compact(array(col("names"))))
            .withColumn(
                "birth_date",
                coalesce(
                    birth_date_udf("Дата рождения", lit("%d.%m.%Y")),
                    birth_date_udf("Дата рождения", lit("%d %m %Y")),
                    birth_date_udf("Дата рождения", lit("%B %d, %Y")),
                    birth_date_udf("Дата рождения", lit("%Y.%m.%d")),
                    birth_date_udf("Дата рождения", lit("%d%m%Y")),
                    birth_date_udf("Дата рождения", lit("%d,%m,%Y")),
                    birth_date_udf("Дата рождения", lit("%d.%m.%Y.")),
                    # Standard Python lib converts %y 0-68 to 2000-2068, 69-99 to 1969-1999
                    when(
                        trim(col("Дата рождения")).rlike(r"\d{1,2}\.\d{1,2}\.\d{2}\D*")
                        | trim(col("Дата рождения")).rlike(r"\d{6}\D*"),
                        birth_date_udf(
                            regexp_replace(
                                regexp_replace(
                                    trim(col("Дата рождения")),
                                    r"^(\d{1,2})\.(\d{1,2})\.(\d{2})",
                                    r"$1.$2.19$3",
                                ),
                                r"\D+$",
                                "",
                            ),
                            lit("%d.%m.%Y"),
                        ),
                    ),
                    birth_date_udf(parse_date_udf("Дата рождения"), lit("%d.%m.%Y")),
                ),
            )
        )
        df = _preprocess_phones(df, "phones1", "Телефон 1")
        df = _preprocess_phones(df, "phones2", "Телефон 2")
        df = _preprocess_phones(df, "phones3", "Телефон 3")

        df = (
            df.withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        flatten(
                            filter(
                                array(
                                    phones_udf(
                                        col("phones1"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                    phones_udf(
                                        col("phones2"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                    phones_udf(
                                        col("phones3"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ),
                                lambda x: x.isNotNull(),
                            )
                        )
                    )
                ),
            )
            .withColumn("emails", array_compact(array(email_udf("E-mail"))))
            .withColumn(
                "education", regexp_replace(trim(col("Образование")), r"\.$", "")
            )
            .withColumn(
                "educations",
                array_compact(array(education_udf(lit(None), lower(col("education"))))),
            )
            .withColumn("address", array_compact(array(address_udf("Город"))))
            .withColumn(
                "actuality", actuality_date_udf(col("Дата резюме"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "raw_metadata",
                array_compact(
                    array(
                        raw_metadata_udf(
                            lit("Образование"),
                            when(
                                (size(col("educations")) == 0)
                                & (length(trim(col("Образование"))) > 2)
                                & (
                                    ~lower(
                                        regexp_replace(
                                            trim(col("Образование")), r":$", ""
                                        )
                                    ).isin(
                                        ["&61607", "учебное заведение", "образование"]
                                    )
                                )
                                & (~col("Образование").contains("</")),
                                col("Образование"),
                            ),
                            lit("Иностранный язык"),
                            when(
                                lower(col("Иностранный язык")).rlike(
                                    self.languages_regex
                                ),
                                col("Иностранный язык"),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "educations",
                when(
                    (size(col("educations")) == 0),
                    when(
                        lower(col("education")).endswith("диплом")
                        | lower(col("education")).endswith("диплом с отличием")
                        | lower(col("education")).endswith("diploma with honour"),
                        array_compact(array(education_udf(lit(None), lit("диплом")))),
                    )
                    .when(
                        lower(col("education")).endswith("бакалавр"),
                        array_compact(array(education_udf(lit(None), lit("бакалавр")))),
                    )
                    .when(
                        lower(col("education")).endswith("магистр"),
                        array_compact(array(education_udf(lit(None), lit("магистр")))),
                    )
                    .when(
                        lower(col("education")).isin(
                            [
                                "высшее экономическое",
                                "высшее техническое",
                                "высшее юридическое",
                                "высшее педагогическое",
                                "высшее медицинское",
                                "высшее гуманитарное",
                                "высшее-техническое",
                                "высшее филологическое",
                                "высшее художественное",
                                "высшее (гуманитарное)",
                                "высшее торговое",
                            ]
                        )
                        | lower(col("education")).endswith("высшее"),
                        array_compact(array(education_udf(lit(None), lit("высшее")))),
                    )
                    .otherwise(col("educations")),
                ).otherwise(col("educations")),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "educations",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        columns = [
            column
            for column in df.columns
            if column not in {"educations", "actuality", "raw_metadata"}
        ]

        df = (
            df.groupBy(columns)
            .agg(
                array_compact(flatten(collect_set("educations"))).alias("educations"),
                max(col("actuality")).alias("actuality"),
                array_compact(flatten(collect_set("raw_metadata"))).alias(
                    "raw_metadata"
                ),
            )
            .withColumn("names", when(size(col("names")) > 0, array_sort(col("names"))))
            .withColumn(
                "phones", when(size(col("phones")) > 0, array_sort(col("phones")))
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, array_sort(col("emails")))
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, array_sort(col("educations"))),
            )
            .withColumn(
                "address", when(size(col("address")) > 0, array_sort(col("address")))
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, array_sort(col("raw_metadata"))),
            )
            .filter(
                col("names").isNotNull()
                & (col("phones").isNotNull() | col("emails").isNotNull())
            )
            .persist()
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
