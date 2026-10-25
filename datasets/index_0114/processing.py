from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    udf,
    size,
)
from pyspark.sql.types import StringType
import locale
from datetime import datetime

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    children_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


def parse_ru_date(date_str):
    try:
        try:
            if not date_str:
                return None
            locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
            return datetime.strptime(date_str, "%d %B %Y").date()
        except ValueError:
            # fallback
            return datetime.strptime(date_str, "%d/%m/%Y").date()
    except:  # noqa: E722
        return None


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0114"

    def parser(self):
        parse_ru_date_udf = udf(parse_ru_date, StringType())

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0114/raw/hh 2018.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("Имя")))
            .withColumn(
                "birth_date",
                birth_date_udf(
                    parse_ru_date_udf(col("ДатаРожд")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("relationship", col("СемПолож"))
            .withColumn("children", children_udf(col("Дети")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Телефон")), phone_udf(col("Телефон2")))
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("Страна"),
                        col("Область"),
                        col("Город"),
                        col("Район"),
                        col("Адрес"),
                        col("Метро"),
                    )
                ),
            )
            .withColumn(
                "educations",
                when(
                    col("Образование").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                when(col("ВУЗ").isNotNull(), col("ВУЗ")).otherwise(
                                    lit(None)
                                ),
                                col("Образование"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            ),
                            education_udf(
                                lit(None),
                                col("ДопОбраз"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            ),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("Профессия").isNotNull() | col("МестоРаботы").isNotNull()),
                    array(
                        work_udf(
                            col("Профессия"),
                            lit(None),
                            lit(None),
                            col("МестоРаботы"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("Права").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Права").isNotNull(),
                                document_udf(
                                    lit("водительское удостоверение"),
                                    col("Права"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    col("Skype").isNotNull() & (col("Skype").isNotNull() != ""),
                    array_compact(
                        array(
                            when(
                                col("skype").isNotNull()
                                & (col("Skype").isNotNull() != ""),
                                social_udf(
                                    lit("Skype"), col("Skype"), lit(None), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("ДатаРег"), lit("%d/%m/%Y %H:%M"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Зарплата"),
                    df["Зарплата"],
                    lit("Опыт"),
                    df["Опыт"],
                    lit("Осебе"),
                    df["Осебе"],
                    lit("СфераД"),
                    df["СфераД"],
                    lit("РежимРаботы"),
                    df["РежимРаботы"],
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "sex",
                "relationship",
                "children",
                "address",
                "works",
                "documents",
                "educations",
                "socials",
                "actuality",
                "raw_metadata",
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("socials").isNotNull()
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
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
        )
        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
