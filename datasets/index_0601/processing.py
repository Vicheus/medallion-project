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
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    raw_metadata_udf,
    address_udf,
    normalize_kz_letters_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0601"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0601/raw/apiba.prgapp.kz_2026.csv",
                sep=",",
                header=True,
            )
            .withColumn("address", normalize_kz_letters_udf(col("address")))
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("patronymic"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "documents",
                when(
                    col("iin").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("iin").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("iin"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code),
                                    ),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("extra"), col("extra")))
            .select("names", "address", "documents", "raw_metadata")
        )

        df.show(n=20, truncate=False)

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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("documents").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
