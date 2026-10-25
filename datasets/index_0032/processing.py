from pyspark.sql.functions import col, when, array, regexp_extract, lit
from pyspark.sql.types import StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import phone_udf, name_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0032"
    important_columns_for_filtering: str = "phones"
    write_filtered_rows: bool = True

    def parser(self):

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0032/raw/Red.csv",
            sep=";",
            header=True,
        )

        DEFAULT_DATE = "01.01.1953"
        NAME_KEYWORDS = ["Заблокирован", "Утеряна"]
        name_pattern = "|".join(NAME_KEYWORDS)

        df = (
            df.filter(col("Phone").isNotNull())
            .withColumn(
                "Fio",
                when(
                    col("Fio").rlike(name_pattern),
                    regexp_extract("Fio", r"\(([^)]+)\)", 1),
                ).otherwise(col("Fio")),
            )
            .withColumn(
                "Birthday",
                when(col("Birthday") == DEFAULT_DATE, None).otherwise(col("Birthday")),
            )
        )

        df.show(n=100, truncate=False)

        df = (
            df.withColumn(
                "birth_date", birth_date_udf(col("Birthday"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phone_udf(col("Phone").cast(StringType())))
            .withColumn("names", name_udf(col("Fio")))
        )

        df = df.drop_duplicates(["names", "phones"])
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.select("names", "birth_date", "phones")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
