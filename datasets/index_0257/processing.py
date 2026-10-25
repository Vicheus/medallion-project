from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    split,
    expr,
    array_append,
)
from pyspark.sql.types import StructType, StructField, StringType


from parsetron import Parsetron
from parsetron.sections.financials.udfs import (
    financial_cards_numbers_udf,
    financial_card_number_udf,
)
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0257"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,financials,address"

    def parser(self):
        schema = StructType(
            [
                StructField("phone", StringType(), True),
                StructField("operator", StringType(), True),
                StructField("region", StringType(), True),
                StructField("timezone", StringType(), True),
                StructField("fullname", StringType(), True),
                StructField("birthdate", StringType(), True),
                StructField("date", StringType(), True),
                StructField("main_card", StringType(), True),
                StructField("additional_cards", StringType(), True),
            ]
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0257/raw/sberspasibo/sberspasibo.txt",
                sep="\t",
                header=False,
                schema=schema,
            )
            .withColumn("names", name_udf(col("fullname")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("address", address_udf(col("region")))
            .withColumn("main_card", financial_card_number_udf(col("main_card")))
            .withColumn(
                "additional_cards",
                financial_cards_numbers_udf(split(col("additional_cards"), ",")),
            )
            .withColumn(
                "additional_cards",
                expr(
                    "TRANSFORM(additional_cards, x -> STRUCT('ПАО Сбербанк' as title, x AS card_number))"
                ),
            )
            .withColumn(
                "main_card",
                when(
                    col("main_card").isNotNull(),
                    struct(
                        lit("ПАО Сбербанк").alias("title"),
                        col("main_card").alias("card_number"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                array_compact(
                    array_distinct(
                        array_append(col("additional_cards"), col("main_card"))
                    )
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("operator"), col("operator"))
            )
            .select(
                "names", "phones", "birth_date", "address", "financials", "raw_metadata"
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
