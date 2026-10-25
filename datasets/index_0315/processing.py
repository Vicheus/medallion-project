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
from parsetron.sections.document.udfs import identify_document_features_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):

    test_mode: bool = False
    dataset_code_name: str = "index_0315"

    def parser(self):
        work_stop_words = [
            "Школа",
            "школа",
            "Учащийся",
            "учащийся",
            "школьник",
            "Школьник",
            "учеба",
            "студент",
            "Не работаю",
        ]
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0315/raw/turniketov.net.csv",
            sep=",",
            header=True,
        ).cache()

        df.show()

        df = (
            df.replace("None", None)
            .limit(20)
            .withColumn("names", name_udf(col("fio")))
            .withColumn("birth_date", birth_date_udf(col("birth"), lit("%Y-%m-%d")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("joined"), lit('"%Y-%m-%dT%H:%M:%S.%f"')),
            )
            .withColumn(
                "document",
                when(
                    col("passport").isNotNull(),
                    identify_document_features_udf(col("passport")),
                ).otherwise(None),
            )
            .withColumn("document_series", col("document")["document_series"])
            .withColumn("document_issued_at", col("document")["document_issued_at"])
            .withColumn("document_issued_by", col("document")["document_issued_by"])
            .withColumn(
                "document_issued_by_code", col("document")["document_issued_by_code"]
            )
            .withColumn(
                "work_company",
                when(
                    ~col("work").rlike("|".join(work_stop_words)), col("work")
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("work_company").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("work_company"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                array(
                    when(
                        col("passport").isNotNull(),
                        document_udf(
                            lit(None),
                            col("document_series"),
                            col("document_issued_at"),
                            lit(None),
                            col("document_issued_by"),
                            col("document_issued_by_code"),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None)
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "sex",
                "documents",
                "works",
                "actuality",
                "document",
                "document_series",
                "document_issued_at",
                "document_issued_by",
                "document_issued_by_code",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
