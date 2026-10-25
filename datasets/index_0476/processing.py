from parsetron.settings import DATASET_COUNTRY_CODE

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
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0476"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0476/raw/*.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("birth_date", birth_date_udf(col("bdate"), lit("%d.%m.%Y")))
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
                                    lit("%Y-%m-%d %H:%M:%S"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "birth_date", "address", "phones", "documents")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(),
                    array_compact(array_distinct(array(col("address")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("address").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
