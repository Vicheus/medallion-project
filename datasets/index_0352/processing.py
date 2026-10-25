from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0352"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0352/raw/клиенты_sdmed_ru_2024.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Номер паспорта").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Номер паспорта").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("Кем выдан паспорт").alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            )
                        )
                    )
                ),
            )
            .select("names", "birth_date", "emails", "phones", "address", "documents")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
