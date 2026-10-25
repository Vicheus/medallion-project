from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_distinct,
    array_compact,
    size,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    phone_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf
from pyspark import StorageLevel


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0503"
    output_file_count: int = 3

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0503/raw/driver_info_results.csv",
                header=True,
                sep=",",
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("middlename"))
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("date_of_birth"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("experience"), col("experience")),
            )
            .withColumn(
                "documents",
                when(
                    col("license_number").isNotNull()
                    | col("passport_number").isNotNull()
                    | col("tax_number").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                when(
                                    col("license_number").isNotNull(),
                                    document_udf(
                                        lit("водительское удостоверение"),
                                        col("license_number"),
                                        col("license_date"),
                                        col("expiration_date"),
                                        lit(None),
                                        lit(None),
                                        lit("%Y-%m-%d"),
                                    ),
                                ).otherwise(None),
                                when(
                                    col("passport_number").isNotNull(),
                                    document_udf(
                                        lit("паспорт гражданина рф"),
                                        col("passport_number"),
                                        col("passport_date"),
                                        lit(None),
                                        col("passport_author"),
                                        col("department_code"),
                                        lit("%Y-%m-%d"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None),
                                when(
                                    col("tax_number").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("tax_number"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("%Y-%m-%d"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality", birth_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array_distinct(array(col("raw_metadata")))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )
        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )
        df = df.select(
            "names", "birth_date", "phones", "documents", "raw_metadata", "actuality"
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
