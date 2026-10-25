from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat,
    array_compact,
    struct,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    name_parts_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0108"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0108/raw/@StormInDataBase/Sessions.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("FirstName"), col("LastName"), col("Patronymic")),
            )
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "documents",
                when(
                    col("Inn").isNotNull()
                    | col("Snils").isNotNull()
                    | col("PassportNumber").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("Snils"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                            when(
                                col("Inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("Inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                            when(
                                col("PassportNumber").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat(
                                        col("PassportSeries"), col("PassportNumber")
                                    ),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("ClientId").isNotNull(),
                    array(
                        struct(
                            lit("Мандарин").alias("title"),
                            lit("http://mandarin.io.ru").alias("link"),
                            col("ClientId").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("ChangeDate"), col("CreateDate")),
                    lit("%Y-%m-%d %H:%M:%S.%f %z"),
                ),
            )
            .select("names", "phones", "documents", "accounts", "actuality")
        )

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
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("phones").isNotNull())
        )
        df = df.select("names", "phones", "documents", "accounts", "actuality")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
