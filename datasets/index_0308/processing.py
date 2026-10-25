from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    regexp_replace,
    regexp_extract,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0308"

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0308/raw/dtgroup.ru/customer base.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("Название")))
            .withColumn(
                "phones", phone_udf(regexp_replace(col("Телефоны"), "комментарий", ""))
            )
            .withColumn("emails", array_compact(array(email_udf(col("Почта")))))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "telegram_url",
                regexp_extract(col("Ссылки"), r"https?://t\.me/([A-Za-z0-9_]+)", 1),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Активность"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "works",
                array_compact(
                    array(
                        when(
                            col("Должность").isNotNull() | col("Компания").isNotNull(),
                            work_udf(
                                col("Должность"),
                                lit(None),
                                lit(None),
                                col("Компания"),
                                lit(None),
                                lit(None),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("telegram_url").isNotNull(),
                            social_udf(
                                lit("Telegram"),
                                lit(None),
                                col("telegram_url"),
                                lit(None),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .select("names", "phones", "emails", "sex", "actuality", "works", "socials")
        )

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0308/raw/dtgroup.ru/customers_*.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("Название")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(
                        array(email_udf(col("Почта")), email_udf(col("megaMail")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("actuality", lit(None))
            .withColumn(
                "birth_date",
                birth_date_udf(col("День рождения/Основания"), lit("%Y-%m-%d")),
            )
            .withColumn(
                "works",
                array_compact(
                    array(
                        when(
                            col("Должность").isNotNull()
                            | col("department").isNotNull(),
                            work_udf(
                                col("Должность"),
                                lit(None),
                                lit(None),
                                concat_ws(" ", lit("dtgroup"), col("department")),
                                lit(None),
                                lit(None),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("skype").isNotNull(),
                            social_udf(
                                lit("Skype"), col("skype"), lit(None), lit(None)
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .select("names", "phones", "emails", "sex", "actuality", "works", "socials")
        )

        df = df_1.unionAll(df_2).drop_duplicates()
        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
