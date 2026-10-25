from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
    to_date,
    date_format,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0472"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0472/raw/vdov_mob_svo.csv",
                sep="\t",
                header=True,
            )
            .withColumn(
                "series",
                regexp_extract("Паспортные данные", r"Серия и номер: (\d+)", 1),
            )
            .withColumn(
                "issued_by",
                regexp_extract("Паспортные данные", r"Кем выдан: (.+?)\.", 1),
            )
            .withColumn(
                "issued_at",
                date_format(
                    to_date(
                        regexp_extract(
                            "Паспортные данные",
                            r"Дата выдачи: (\d{2}\.\d{2}\.\d{4})",
                            1,
                        ),
                        "dd.MM.yyyy",
                    ),
                    "yyyy-MM-dd",
                ),
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date_formatted",
                date_format(to_date(col("Дата рождения"), "M/d/yyyy"), "yyyy-MM-dd"),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("birth_date_formatted"), lit("%Y-%m-%d")),
            )
            .withColumn("address", address_udf(col("Адрес регистрации")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "documents",
                when(
                    col("series").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("series").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("series"),
                                    col("issued_at"),
                                    lit(None),
                                    col("issued_by"),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "birth_date", "address", "phones", "documents")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
