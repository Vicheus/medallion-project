from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, regexp_replace, length, lower

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
    extract_name_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0354"

    def parser(self):
        name_replace_pattern = r"(?i)\b(отказ|покупка|работа|некорректный|супруга)\b"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0354/raw/клиенты_xfit_ru.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                when(
                    length(col("ФИО")) > 45,
                    name_udf(
                        extract_name_udf(
                            regexp_replace(lower("ФИО"), name_replace_pattern, "")
                        )
                    ),
                ).otherwise(
                    name_udf(regexp_replace(lower("ФИО"), name_replace_pattern, ""))
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%M.%Y"))
            )
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "actuality", actuality_date_udf(col("Последний визит"), lit("%Y-%M-d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .select("names", "birth_date", "sex", "phones", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
