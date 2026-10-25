from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, split, size
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    emails_udf,
    phone_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0457"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0457/raw/Магазин_одежды_Nice-one_26_02_2025.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("emails", emails_udf(split(col("Почта"), ",")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("Никнейм"), col("Никнейм"))
            )
            .select("names", "emails", "phones", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

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
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
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
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
