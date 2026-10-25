from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.work.udfs import work_udf

from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0180"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0180/raw/bolshayaperemena/*.csv",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn(
                "educations",
                when(
                    col("Наименование учреждения").isNotNull()
                    & (
                        (col("Роль") == "Студент ССУЗа")
                        | (col("Роль") == "Ученик")
                        | (col("Роль") == "Выпускник")
                        | (col("Роль") == "СО")
                    ),
                    array_compact(
                        array(
                            education_udf(
                                col("Наименование учреждения"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("Наименование учреждения").isNotNull()
                    & (col("Роль") == "Педагог"),
                    array_compact(
                        array(
                            work_udf(
                                col("Роль"),
                                lit(None),
                                lit(None),
                                col("Наименование учреждения"),
                                col("Адрес"),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%Y-%m-%d")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "educations",
                "sex",
                "birth_date",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
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
