from pyspark.sql.functions import when, col, lit, array, array_compact, lower

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0071"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,phones,address"

    def parser(self):
        incorrect_name_parts = ["-", "--", "---", "----", "-----", ".", "...", "....."]
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0071/raw/skyeng.ru.txt",
            sep=",",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .filter(
                ~(lower(col("Имя")).like("test%"))
                & ~(lower(col("Фамилия")).like("test%"))
                & ~((col("Имя") == "-") & (col("Фамилия") == "-"))
            )
            .withColumn(
                "Имя",
                when(col("Имя").isin(incorrect_name_parts), None).otherwise(col("Имя")),
            )
            .withColumn(
                "Фамилия",
                when(col("Фамилия").isin(incorrect_name_parts), None).otherwise(
                    col("Фамилия")
                ),
            )
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), lit(None))
            )
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%.m.%d"))
            )
            .withColumn("address", email_udf(col("Адрес")))
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
        )
        df = df.select("names", "emails", "phones", "birth_date", "address", "socials")
        df = df.dropDuplicates(["names", "emails", "phones"])

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
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
