from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, size, array_compact

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0337"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0337/raw/мойбизнес.рф.txt",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "address", "emails", "phones", "documents")
        )

        df = df.drop_duplicates()

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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
