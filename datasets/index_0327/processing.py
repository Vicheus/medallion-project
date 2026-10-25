from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    sex_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0327"
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0327/raw/EGRUL_2022_2024.txt",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("name"), col("last_name"), col("patronymic")),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("end_date"), col("reg_date")), lit("%Y-%m-%d")
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("ogrnip").isNotNull(),
                                document_udf(
                                    lit("огрн"),
                                    col("ogrnip"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("reg_date"),
                    col("reg_date"),
                    lit("status"),
                    col("status"),
                    lit("end_date"),
                    col("end_date"),
                    lit("okved_id"),
                    col("okved_id"),
                    lit("tax_office_id"),
                    col("tax_office_id"),
                    lit("pfr"),
                    col("pfr"),
                    lit("fss"),
                    col("fss"),
                    lit("citizenship_type"),
                    col("citizenship_type"),
                ),
            )
            .select("names", "sex", "emails", "documents", "actuality", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
