from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    collect_set,
    first,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    sex_udf,
    address_udf,
    address_from_parts_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0502"
    output_file_count: int = 50
    validate_invalid_groupping: bool = True
    important_columns_for_filtering: str = "phones,addresses"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0502/raw/max.ru - @StormBaseAdapter.csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Регион")))
            .withColumn(
                "addresses",
                address_from_parts_udf(
                    lit(1),
                    lit(None),
                    lit(None),
                    col("Регион"),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Оператор"),
                    col("Оператор"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "address",
                "addresses",
                "raw_metadata",
            )
        )

        df_with_bdate = (
            df.filter(col("birth_date").isNotNull() & col("names").isNotNull())
            .groupBy(["names", "birth_date"])
            .agg(
                array_distinct(array_compact(collect_set(col("phones")))).alias(
                    "phones"
                ),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_distinct(array_compact(collect_set(col("address")))).alias(
                    "address"
                ),
                array_distinct(array_compact(collect_set(col("addresses")))).alias(
                    "addresses"
                ),
                first(col("sex"), ignorenulls=True).alias("sex"),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "address",
                "addresses",
                "raw_metadata",
            )
        )

        df_without_bdate = (
            df.filter(col("birth_date").isNull())
            .drop_duplicates(["names"])
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .withColumn(
                "addresses", array_compact(array_distinct(array(col("addresses"))))
            )
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "address",
                "addresses",
                "raw_metadata",
            )
        )

        df = df_with_bdate.unionAll(df_without_bdate).select(
            "names",
            "birth_date",
            "sex",
            "phones",
            "address",
            "addresses",
            "raw_metadata",
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(size(col("addresses")) > 0, col("addresses")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
