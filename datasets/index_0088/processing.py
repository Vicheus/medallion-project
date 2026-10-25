from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0088"

    def parser(self):
        df = self.read(
            path="SuperJob_2016-2017_5,8M.csv",
            sep=";",
            encoding="windows-1251",
            header=True,
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "sex",
                sex_udf(
                    when(col("Пол: 2-М 3-Ж") == 2, lit("male")).otherwise(lit("female"))
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(
                    concat_ws(
                        "-",
                        col("Год рождения"),
                        col("Месяц рождения"),
                        col("День рождения"),
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Телефон1")), phone_udf(col("Телефон2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("город")))
            .withColumn("emails", email_udf(col("e-mail")))
        )

        df = df.select("names", "address", "emails", "phones", "sex", "birth_date")

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
