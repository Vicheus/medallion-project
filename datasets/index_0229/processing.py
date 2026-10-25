from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat,
    array_compact,
    array_distinct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0229"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0229/raw/preprocessed/labquest_*.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО Пациента")))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Адрес эл_почты")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Паспорт_серия").isNotNull()
                                & col("Паспорт_номер").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(col("Паспорт_серия"), col("Паспорт_номер")),
                                    lit(None),
                                    lit(None),
                                    col("Паспорт_кем выдан"),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("Заказчик"), col("Заказчик"))
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "documents",
                "raw_metadata",
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
