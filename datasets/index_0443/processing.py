from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    lit,
    greatest,
    split,
    array_compact,
    array_distinct,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phones_udf,
    birth_date_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0443"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0443/raw/cappuccinohotel.ru @nbase_join.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phones_udf(split(col("Телефоны"), ",")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
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
                                    col("Информация о документе").alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("tgid").isNotNull() & (col("tgid").isNotNull() != ""),
                    array_compact(
                        array(
                            when(
                                col("tgid").isNotNull()
                                & (col("tgid").isNotNull() != ""),
                                social_udf(
                                    lit("Telegram"), col("tgid"), lit(None), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("Последняя активность"), col("Дата последней коммуникации")
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "documents",
                "socials",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names", "birth_date"])

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
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
