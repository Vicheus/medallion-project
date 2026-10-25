from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0258"
    output_file_count: int = 20

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0258/raw/pochta_kartoteka.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("OriginalFIO")))
            .withColumn("sex", sex_udf(col("Sex")))
            .withColumn(
                "birth_date", birth_date_udf(col("Birthday"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("address", address_udf(col("OriginalAddress")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("PassportSeriya").isNotNull()
                                & col("PassportNumber").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("PassportSeriya"), col("PassportNumber")
                                    ),
                                    col("PassportIssueWhen"),
                                    lit(None),
                                    col("PassportIssueWho"),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("SNILS").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("SNILS"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("INN"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .select("names", "sex", "birth_date", "phones", "address", "documents")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
