from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    phone_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0153"
    calc_completeness: bool = False
    important_columns_for_filtering: str = "phones,documents,address"
    write_filtered_rows: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0153/raw/pochta.ru24.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "address",
                when(
                    col("Индекс").isNotNull() & col("Адрес").isNotNull(),
                    address_udf(concat_ws(" ", col("Индекс"), col("Адрес"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата активности"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Вес посылки"),
                    col("Вес посылки"),
                    lit("Объявл_ценность"),
                    col("Объявл_ценность"),
                    lit("Валюта"),
                    col("Валюта"),
                    lit("Вид отправления"),
                    col("Вид отправления"),
                    lit("Категория отправления"),
                    col("Категория отправления"),
                    lit("Размер упаковки"),
                    col("Размер упаковки"),
                    lit("Вид упаковки"),
                    col("Вид упаковки"),
                ),
            )
            .select(
                "names", "phones", "address", "documents", "actuality", "raw_metadata"
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
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
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.drop_duplicates()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
