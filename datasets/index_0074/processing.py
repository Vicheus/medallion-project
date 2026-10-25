from pyspark import StorageLevel
from pyspark.sql.functions import col, when, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0074"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0074/raw/100realt.txt",
            sep="\t",
            encoding="windows-1251",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Заголовок"), df["Заголовок"], lit("Описание"), df["Описание"]
                ),
            )
        )

        df = df.select("names", "phones", "address", "raw_metadata")

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
