from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    date_format,
    regexp_replace,
    coalesce,
    to_date,
    lit,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0532"
    calc_completeness: bool = True
    output_file_count: int = 10

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0532/raw/onlineskills_ru.csv",
                sep=",",
            ).replace("-", None)
        ).filter(
            ~(
                col("Страна").isin(
                    [
                        "Казахстар",
                        "Казахстан-Беларусь",
                        "Республика Казахстан",
                        "казахстан",
                        "Республика Кказахстан",
                        "Белорусь",
                        "БЕЛАРУСЬ",
                        "Белларусь",
                        "Республика Белорусь",
                        "Белоруссия",
                        "беларусия",
                    ]
                )
            )
        )

        replacements = [
            ("янв\\.", "01"),
            ("фев\\.", "02"),
            ("февр\\.", "02"),
            ("мар\\.", "03"),
            ("апр\\.", "04"),
            ("мая", "05"),
            ("июн\\.", "06"),
            ("июл\\.", "07"),
            ("авг\\.", "08"),
            ("сен\\.", "09"),
            ("сент\\.", "09"),
            ("окт\\.", "10"),
            ("ноя\\.", "11"),
            ("нояб\\.", "11"),
            ("дек\\.", "12"),
        ]

        df = df.withColumn(
            "normalized_activity_date", col("Клиент дата последней активности")
        )

        for ru, num in replacements:
            df = df.withColumn(
                "normalized_activity_date",
                regexp_replace(
                    coalesce(
                        col("normalized_activity_date"),
                        col("Клиент дата последней активности"),
                    ),
                    ru,
                    num,
                ),
            )

        df = (
            df.withColumn(
                "names",
                name_udf(col("Имя клиента")),
            )
            .withColumn("address", address_udf(col("Клиент адрес")))
            .withColumn("emails", email_udf(col("Email клиента")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    date_format(
                        to_date(col("normalized_activity_date"), "dd MM yyyy HH:mm"),
                        "yyyy-MM-dd",
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "actuality",
            )
        )

        df = df.drop_duplicates(["phones", "emails"])

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
