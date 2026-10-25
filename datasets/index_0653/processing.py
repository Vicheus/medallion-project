from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    array_sort,
    col,
    filter,
    flatten,
    lit,
    regexp_replace,
    size,
    split,
    transform,
    trim,
    when,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    address_udf,
    birth_date_udf,
    name_parts_udf,
    normalize_kz_letters_udf,
    phones_udf,
    sex_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


def _preprocess_phones(df: DataFrame, res_col: str, input_col: str) -> DataFrame:
    return df.withColumn(res_col, split(col(input_col), lit(","))).withColumn(
        res_col,
        transform(
            res_col,
            lambda x: when(
                ~trim(x).rlike(r"\s"),
                regexp_replace(trim(x), r"\D+$", ""),
            ).otherwise(x),
        ),
    )


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0653"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    stop_words = [
        "УЛИЦА: Не указано",
        "ДОМ: Не указано",
        "УЛИЦА: НЕ УКАЗАНО",
        "ДОМ: НЕ УКАЗАНО",
        "УЛИЦА: Неопределен",
        "УЛИЦА: НЕОПРЕДЕЛЕН",
        "УЛИЦА: неопределенная",
        "ОБЛ.ЗНАЧ\\.:",
        "РЕСП.ЗНАЧ\\.:",
        "РАЙ.ЗНАЧ\\.:",
        "ВНУТРИ ГОРОДА",
        "ДОМ: ¦/¦",
        "ДОМ: \\*",
        "ДОМ: б/н",
        "ДОМ: Б/Н",
        "ДОМ: бн",
        "ДОМ: БН",
        "КВАРТИРА: ####",
    ]
    stop_words_regex = "|".join(stop_words)
    stop_phones = [
        "77072844793",
        "77072844792",
        "77020519546",
        "77143145896",
        "77029140919",
        "77143334545",
        "77145399147",
        "77263243400",
        "77272902206",
        "77252771552",
        "77213145417",
        "77252533072",
        "77292401202",
        "77277573209",
        "77132991587",
        "77172300483",
        "77164421919",
        "77213140083",
        "77232789107",
        "77263622825",
        "77277573208",
        "77232206892",
        "77114121942",
        "77143500000",
        "77143159487",
        "77143158963",
        "77152505707",
        "77292511225",
        "77143197452",
        "77277425051",
        "77145394335",
        "77143179236",
        "77122306185",
        "77273605702",
        "77143152487",
        "77252956500",
        "77273721036",
        "77234742432",
        "77277534128",
        "77262348352",
        "77134500000",
        "77213143466",
        "77164549429",
        "77272999759",
        "77162300009",
        "77277031739",
        "77277551032",
        "77232609268",
        "77263624265",
        "77233235728",
        "77143321717",
        "77277550219",
        "77143144585",
        "77475982263",
        "77019120914",
        "77078462293",
        "77023984006",
        "77716987228",
        "77081756182",
        "77054561084",
        "77475107106",
        "77474815926",
        "77758709493",
        "77262460203",
        "77751611360",
        "77772091262",
        "77054852702",
        "77052405761",
        "77752206599",
        "77786750568",
        "77751481091",
        "77774564512",
        "77014152536",
        "77072772281",
        "77053955088",
        "77262348542",
        "77078462293",
        "77059687179",
        "77018350396",
        "77051281570",
        "77019140912",
        "77082116058",
        "77779859252",
        "77054816640",
        "77016680883",
        "77770945257",
        "77478461344",
        "77053572262",
        "77072772281",
        "77053709356",
        "77782991271",
        "77028121773",
        "77783834902",
        "77716699976",
        "77081956373",
        "77076266813",
        "77056977375",
        "77779635013",
        "77078240497",
        "77163127568",
        "77768713285",
        "77779868410",
        "77058708226",
        "77029727723",
        "77476576751",
        "77782932982",
        "77028692795",
        "77782843410",
        "77761296554",
        "77272642277",
        "77262521413",
        "77122324242",
        "77242275403",
        "77182606864",
        "77143524164",
        "77182606889",
        "77215379990",
        "77252448855",
        "77215331540",
        "77145391145",
        "77273056400",
        "77242200573",
        "77272323869",
        "77172399999",
        "77215658208",
        "77215658226",
        "77222360485",
        "77277456010",
        "77164631501",
        "77145328130",
        "77263779089",
        "77215644573",
        "77232553292",
        "77277926546",
        "77263522441",
        "77145421510",
        "77262460312",
        "77172728149",
        "77132976153",
        "77112264582",
        "77182393473",
        "77273056400",
    ]

    def parser(self):
        df = (
            self.read(path="Жители Казахстан 16kk_cleaned.csv", sep=";", header=True)
            .repartition(50)
            .withColumn(
                "names",
                name_parts_udf(
                    normalize_kz_letters_udf(col("Имя")),
                    normalize_kz_letters_udf(col("Фамилия")),
                    normalize_kz_letters_udf(col("Отчество")),
                ),
            )
            .filter(col("names").isNotNull())
            .withColumn("names", array_compact(array(col("names"))))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
        )
        df = _preprocess_phones(df, "phones1", "Мобильный")
        df = _preprocess_phones(df, "phones2", "Рабочий")
        df = _preprocess_phones(df, "phones3", "Домашний")
        df = (
            df.withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        flatten(
                            filter(
                                array(
                                    when(
                                        col("phones1").isNotNull(),
                                        phones_udf(
                                            col("phones1"),
                                            lit(self.dataset_country_code.value),
                                        ),
                                    ),
                                    when(
                                        col("phones2").isNotNull(),
                                        phones_udf(
                                            col("phones2"),
                                            lit(self.dataset_country_code.value),
                                        ),
                                    ),
                                    when(
                                        col("phones3").isNotNull(),
                                        phones_udf(
                                            col("phones3"),
                                            lit(self.dataset_country_code.value),
                                        ),
                                    ),
                                ),
                                lambda x: x.isNotNull(),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "phones", filter(col("phones"), lambda x: ~x.isin(self.stop_phones))
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        document_udf(
                            lit("инн"),
                            col("ИНН"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(self.dataset_country_code.value),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array(
                        when(
                            col("Адрес").isNotNull(),
                            address_udf(
                                regexp_replace(
                                    regexp_replace(
                                        regexp_replace(
                                            normalize_kz_letters_udf(col("Адрес")),
                                            self.stop_words_regex,
                                            "",
                                        ),
                                        "ПОСЕЛОК: ТАУКЕНТ, ПОСЕЛОК: ТАУКЕНТ",
                                        "ПОСЕЛОК: ТАУКЕНТ",
                                    ),
                                    r"АУЛ\(СЕЛО\):",
                                    "СЕЛО",
                                )
                            ),
                        )
                    )
                ),
            )
            .select("names", "birth_date", "sex", "phones", "documents", "address")
            .withColumn("names", when(size(col("names")) > 0, col("names")))
            .withColumn(
                "phones",
                when(size(col("phones")).between(1, 10), array_sort(col("phones"))),
            )
            .withColumn("documents", when(size(col("documents")) > 0, col("documents")))
            .withColumn("address", when(size(col("address")) > 0, col("address")))
            .filter(
                col("names").isNotNull()
                & (col("phones").isNotNull() | col("documents").isNotNull())
            )
            .persist()
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
