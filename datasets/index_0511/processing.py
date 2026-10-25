from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array_compact,
    array,
    concat_ws,
    lit,
    array_size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0511"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/wikkeo.com/wikkeo.com (2022).txt",
            sep=",",
        )
        df = df.drop_duplicates(["ФИО"])

        df = (
            (
                df.withColumn("names", name_udf(coalesce(col("ФИО"), col("Никнейм"))))
                .withColumn("phones", phone_udf(col("Номер телефона")))
                .withColumn("emails", email_udf(col("Почта")))
                .withColumn(
                    "address", address_udf(concat_ws(" ", col("Город"), col("Адрес")))
                )
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array_compact(array(address_with_type_udf(col("address"), lit(3))))
                ),
            )
            .withColumn(
                "socials",
                when(
                    (
                        (col("Телеграм ID").isNotNull() & (col("Телеграм ID") != ""))
                        | (
                            col("Телеграм тег").isNotNull()
                            & (col("Телеграм тег") != "")
                        )
                    ),
                    array_compact(
                        array(
                            social_udf(
                                lit("Telegram"),
                                col("Телеграм ID"),
                                col("Телеграм тег"),
                                lit(None),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "emails", "address", "addresses", "socials")
        )

        df.cache()

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(), array_compact(array(col("address")))
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(array_size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(array_size(col("addresses")) > 0, col("addresses")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("socials").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
