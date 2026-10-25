from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array_compact,
    array_distinct,
    array,
    concat_ws,
    lit,
    trim,
    array_size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    relations_udf,
    address_udf,
    raw_metadata_udf,
    addresses_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0510"
    calc_completeness: bool = False
    output_files_count: int = 5

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/ozon_staff_22.csv",
            sep=";",
        )
        df = df.drop_duplicates(["ФИО"])

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(
                                concat_ws(" ", col("Город"), col("Фактический адрес"))
                            ),
                            address_udf(col("Адрес оформления")),
                        )
                    )
                ),
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    addresses_with_type_udf(col("address"), lit(3))
                ),
            )
            .withColumn(
                "relations",
                relations_udf(
                    concat_ws(" ", name_udf("Руководитель"), lit("Руководитель"))
                ),
            )
            .withColumn(
                "works",
                when(
                    col("Уровень 1").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("Должность"),
                                    lit(None),
                                    lit(None),
                                    trim(
                                        concat_ws(
                                            " ",
                                            col("Уровень 1"),
                                            col("Уровень 2"),
                                            col("Уровень 3"),
                                            col("Уровень 4"),
                                            col("Уровень 5"),
                                            col("Уровень 6"),
                                            col("Уровень 7"),
                                            col("Уровень 8"),
                                            col("Уровень 9"),
                                            col("Уровень 10"),
                                        )
                                    ),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Рабочий телефон"),
                    col("Рабочий телефон"),
                    lit("Slack"),
                    col("Slack"),
                    lit("HR Бизнес-партнер"),
                    col("HR Бизнес-партнер"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "relations",
                "address",
                "addresses",
                "works",
                "raw_metadata",
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    col("relations").isNotNull(), array_compact(array(col("relations")))
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(array_size(col("works")) > 0, col("works")).otherwise(None),
            )
            .withColumn(
                "address",
                when(array_size(col("address")) > 0, col("address")).otherwise(None),
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
                | col("works").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
