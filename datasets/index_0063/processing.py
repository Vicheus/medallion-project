from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat_ws,
    concat,
    size,
    array_compact,
    struct,
    array_distinct,
    split,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, address_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0063"

    def parser(self):
        df = self.read(
            path="Beeline2019.csv", sep="|", header=True, encoding="windows-1251"
        )

        # split contact phones string and apply validation udf on each value
        df = df.withColumn(
            "split_contact_phones", split(col("Контактный телефон"), ",")
        )
        max_split_values = (
            df.selectExpr("size(split_contact_phones) as size")
            .agg({"size": "max"})
            .collect()[0][0]
        )
        transformed_contcact_phone_columns = []
        for i in range(max_split_values):
            column_name = f"contact_phone_{i+1}"
            transformed_column_name = f"transformed_{column_name}"
            df = df.withColumn(
                f"contact_phone_{i+1}", col("split_contact_phones").getItem(i)
            )
            df = df.withColumn(transformed_column_name, phone_udf(col(column_name)))
            transformed_contcact_phone_columns.append(transformed_column_name)
        df = df.drop("split_contact_phones")

        df = df.withColumn(
            "contact_phones", array(*transformed_contcact_phone_columns)
        ).withColumn("sms_phones", array(phone_udf(col("Телефон для СМС-уведомлений"))))

        df = (
            df.withColumn("names", name_udf(col("Абонент (ФИО/Орг)")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(concat(col("contact_phones"), col("sms_phones")))
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    when(
                        col("Город").isNotNull(),
                        concat_ws(
                            ", ",
                            col("Город"),
                            when(
                                col("Улица") != "", concat(lit("ул. "), col("Улица"))
                            ).otherwise(None),
                            when(
                                col("Дом") != "", concat(lit("д. "), col("Дом"))
                            ).otherwise(None),
                            when(
                                col("Строение") != "",
                                concat(lit("стр. "), col("Строение")),
                            ).otherwise(None),
                            when(
                                col("№ квартиры") != "",
                                concat(lit("кв. "), col("№ квартиры")),
                            ).otherwise(None),
                        ),
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("CTN абонента").isNotNull(),
                    array(
                        struct(
                            lit("Beeline").alias("title"),
                            lit("https://beeline.ru").alias("link"),
                            col("CTN абонента").alias("id"),
                        )
                    ),
                ),
            )
        )

        df = df.select("names", "phones", "address", "accounts")

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
