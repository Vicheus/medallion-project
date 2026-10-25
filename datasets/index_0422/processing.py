from pyspark import StorageLevel

from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    phone_udf,
    address_udf,
    name_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0422"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0422/raw/KZ Билайн (2018) 5Kk строк.csv",
                sep="|",
            )
            .withColumn("names", name_udf(col("фио")))
            .withColumn(
                "phones",
                phone_udf(col("телефон"), lit(self.dataset_country_code.value)),
            )
            .withColumn("address", address_udf(col("адрес")))
            .select("names", "phones", "address")
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("address").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
