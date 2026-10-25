from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_set,
    udf,
)
from pyspark.sql.types import StringType
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


def extract_valid_name(full_name):
    import re

    if full_name is None:
        return None
    parts = full_name.strip().split()
    # Keep only valid Cyrillic name parts
    valid_parts = [p for p in parts if re.match(r"^[А-ЯЁ][а-яё]+$", p)]
    return " ".join(valid_parts) if len(valid_parts) >= 2 else None


extract_valid_name_udf = udf(extract_valid_name, StringType())


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0343"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0343/raw/персональные_данные_fast_anime_ru_02_2021.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("Почтовый индекс"),
                        col("Область"),
                        col("Город"),
                        col("Улица"),
                        col("Дом"),
                        col("Квартира"),
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(array(name_udf(extract_valid_name_udf(col("ФИО")))))
                ),
            )
            .select("names", "emails", "phones", "address")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(collect_set("address")).alias("address"),
                array_compact(collect_set("emails")).alias("emails"),
            )
            .select("names", "emails", "phones", "address")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
