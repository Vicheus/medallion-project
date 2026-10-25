from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf

from parsetron.sections.main.udfs import (
    birth_date_udf,
    phone_udf,
    address_udf,
    name_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0043"

    def parser(self):

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0043/raw/DengiSrazy.ru_@BDdump/dengisrazy.ru_nbki.ru_03.2024_(46.230.018).csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%d.%m.%Y")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("document").isNotNull(),
                            document_udf(
                                lit("паспорт гражданина рф"),
                                col("document"),
                                col("passport_date"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("%Y-%m-%d"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .select("names", "phones", "address", "birth_date", "documents")
        )

        df = df.select("names", "phones", "address", "birth_date", "documents")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

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

        df.show(truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
