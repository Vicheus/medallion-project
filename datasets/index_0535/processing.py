from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    email_udf,
    phone_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0535"
    calc_completeness: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0434/raw/pm.ru - @StormBaseAdapter/pm.ru/clients_organizations.csv",
            sep=";",
        )

        df = (
            df.withColumn(
                "names",
                name_udf(col("name")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf((col("phone"))))
            .withColumn("address", address_udf((col("real_address"))))
            .withColumn(
                "documents",
                when(
                    (col("kpp").isNotNull() | col("inn").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("kpp").isNotNull()),
                                document_udf(
                                    lit("кпп"),
                                    col("kpp"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("inn").isNotNull()),
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
                "financials",
                when(
                    col("bank_name").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("bank_name").isNotNull(),
                                struct(col("bank_name").alias("title")),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("head_full_name"),
                    col("head_full_name"),
                    lit("head_position"),
                    col("head_position"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "documents",
                "financials",
                "raw_metadata",
            )
        )

        df = df.drop_duplicates(["names"])

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(), array_compact(array(col("address")))
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
