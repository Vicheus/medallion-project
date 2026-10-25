from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.educations.udfs import education_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0555"

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0555/raw/declarant_org/persons.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "education", regexp_replace(col("education"), "Место учебы:", "")
            )
            .withColumn("ownership", regexp_replace(col("ownership"), r"\r?\n", ";"))
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "educations",
                when(
                    col("education").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                lit(None),
                                col("education"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("inn").isNotNull(),
                    array_compact(
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
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("sanctions"),
                    col("sanctions"),
                    lit("declr_info"),
                    col("declr_info"),
                    lit("ownership"),
                    col("ownership"),
                ),
            )
            .select("names", "birth_date", "educations", "documents", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
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
            & (col("documents").isNotNull() | col("raw_metadata").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
