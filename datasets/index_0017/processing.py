from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 40
    dataset_code_name: str = "index_0017"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0017/raw/Lukoil.ru_2022_13,8M.csv",
            sep=",",
            header=True,
            encoding="windows-1251",
        )

        # cleanup incorrect card numbers
        df = df.withColumn(
            "Номер Карты",
            when(col("Номер Карты") == "0", None).otherwise(col("Номер Карты")),
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "accounts",
                when(
                    col("Номер Карты").isNotNull(),
                    array(
                        struct(
                            lit("Карта лояльности Лукойл").alias("title"),
                            col("Номер Карты").alias("client_card_number"),
                        )
                    ),
                ).otherwise(None),
            )
        )

        df = df.select("names", "phones", "birth_date", "accounts")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("accounts").isNotNull())
        )

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df.show(n=100, truncate=False)

        df.printSchema()

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
