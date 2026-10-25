from pyspark import StorageLevel

from pyspark.sql.functions import when, col, lit, array, size, array_compact

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE

from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    birth_date_udf,
    phone_udf,
    sex_udf,
    address_udf,
    name_parts_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0419"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0419/raw/Damumed.kz - @BDump/*.csv"
        )
        df = df.filter(col("ИНН").isNotNull() | col("Телефон").isNotNull())

        df.show(n=20, truncate=False)

        df = (
            df.withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "phones",
                phone_udf(col("Телефон"), lit(self.dataset_country_code.value)),
            )
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("ИНН").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("ИНН"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Дата смерти"),
                    col("Дата смерти"),
                    lit("Граждантсво"),
                    col("Граждантсво"),
                    lit("Национальность"),
                    col("Национальность"),
                ),
            )
        )

        df.cache()

        df = df.select(
            "names",
            "birth_date",
            "phones",
            "address",
            "sex",
            "documents",
            "raw_metadata",
        )

        df = (
            df.withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "birth_date",
            "phones",
            "address",
            "sex",
            "documents",
            "raw_metadata",
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
