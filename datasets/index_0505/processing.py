from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, array_size

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0505"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 5
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/marwin_kz_meloman_kz.csv",
            sep=";",
        ).filter(col("Магазин") == "Meloman.kz")

        df = (
            df.withColumn("names", name_udf(col("Покупатель")))
            .withColumn(
                "phones",
                phone_udf(
                    col("Контактный телефон"), lit(self.dataset_country_code.value)
                ),
            )
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("address", address_udf(col("Адрес доставки")))
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array(address_with_type_udf(col("address"), lit(2)))
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Дата доставки"),
                    col("Дата доставки"),
                    lit("Состав"),
                    col("Состав"),
                    lit("Сумма"),
                    col("Сумма"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата и время"), lit("%d.%m.%Y %H:%M")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "addresses",
                "raw_metadata",
                "actuality",
            )
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
                "addresses",
                when(array_size(col("addresses")) > 0, col("addresses")).otherwise(
                    None
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
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
