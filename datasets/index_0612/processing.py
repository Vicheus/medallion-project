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
    concat,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0612"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0612/raw/abonents.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("Абонент")))
            .withColumn(
                "address", address_udf(concat_ws(" ", lit("г. Кинешма"), col("Адрес")))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Телефон 1")),
                            phone_udf(col("Телефон 2")),
                            phone_udf(col("Телефон 3")),
                            phone_udf(col("Телефон 4")),
                        )
                    )
                ),
            )
            .withColumn("series", regexp_extract("Документ абонента", r"^(\d{4})", 1))
            .withColumn(
                "number", regexp_extract("Документ абонента", r"^\d{4}\s+(\d{6})", 1)
            )
            .withColumn(
                "issued_at",
                regexp_extract("Документ абонента", r"(\d{2}\.\d{2}\.\d{4})$", 1),
            )
            .withColumn(
                "issued_by",
                regexp_extract(
                    "Документ абонента",
                    r"^\d{4}\s+\d{6}\s+(.*)\s+\d{2}\.\d{2}\.\d{4}$",
                    1,
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("series").isNotNull() & col("number").isNotNull(),
                            document_udf(
                                lit(None),
                                concat(col("series"), col("number")).alias("serial"),
                                col("issued_at").alias("date_issue"),
                                lit(None).alias("date_expire"),
                                col("issued_by").alias("authority"),
                                lit(None).alias("authority_code"),
                                lit("%d.%m.%Y"),
                            ),
                        ),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата подключения"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "address", "phones", "documents", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
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
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
