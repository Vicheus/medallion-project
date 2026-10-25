from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    regexp_extract,
    udf,
)
from pyspark.sql.types import StringType, ArrayType

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import name_udf, phones_udf, address_udf

import re


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0243"

    def parser(self):
        id_pattern = r"^(\d+)"
        name_pattern = r"([А-Яа-яЁё]+?)\s([А-Яа-яЁё]+(?: [А-Яа-яЁё]+)?)"
        car_model_pattern = r"\s([A-Za-z\s]+(?:\w+\s\w+))\s"
        car_number_pattern = (
            r"([A-Za-zА-Яа-я])\s?(\d{3})\s?([A-Za-zА-Яа-я]{2})\s?(\d{3})"
        )
        address_pattern = r"(Фургон|Цельнометаллический|Рефрижератор|Тент|Фермер фургон|Фермер Цельнометаллический|Фермер тент|Изотермический|Бычок)(.*)"

        def extract_phones(text):
            if not text:
                return []
            return re.findall(r"\d{11}", text)

        extract_phones_udf = udf(extract_phones, ArrayType(StringType()))

        def remove_duplicate_words(input_string):
            if not input_string:
                return
            words = input_string.split()
            unique_words = list(dict.fromkeys(words))
            return " ".join(unique_words)

        remove_duplicate_words_udf = udf(remove_duplicate_words, StringType())

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0243/raw/preprocessed/mover24_ru_processed.json",
                sep="\n",
                header=False,
            )
            .withColumn("search_string", col("_source.search_string"))
            .select("search_string")
        )

        split_pattern = r"(.*)(Фургон|Цельнометаллический|Рефрижератор|Тент|Фермер фургон|Фермер Цельнометаллический|Фермер тент|Изотермический|Бычок)(.*)"

        df = df.withColumn(
            "search_string_1", regexp_extract(col("search_string"), split_pattern, 1)
        ).withColumn(
            "search_string_2", regexp_extract(col("search_string"), split_pattern, 3)
        )

        df = (
            df.withColumn("phone_numbers", extract_phones_udf(col("search_string_1")))
            .select(
                regexp_extract(col("search_string_1"), id_pattern, 1).alias("id"),
                regexp_extract(col("search_string_1"), name_pattern, 0).alias("name"),
                regexp_extract(col("search_string_1"), car_model_pattern, 1).alias(
                    "car_model"
                ),
                regexp_extract(col("search_string_1"), car_number_pattern, 0).alias(
                    "car_number"
                ),
                remove_duplicate_words_udf(
                    regexp_extract(col("search_string"), address_pattern, 2)
                ).alias("address"),
                "phone_numbers",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phones_udf(col("phone_numbers")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "vehicles",
                when(
                    (col("car_number").isNotNull() & (col("car_number") != "")),
                    vehicle_udf(
                        lit(1),
                        col("car_model"),
                        lit(None),
                        lit(None),
                        col("car_number"),
                        lit(None),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "vehicles", "address")
        )

        df = df.drop_duplicates(["names"])
        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(col("vehicles").isNotNull(), array(col("vehicles"))).otherwise(
                    None
                ),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
