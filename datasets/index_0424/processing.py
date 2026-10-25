from pyspark import StorageLevel

from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import phone_udf, name_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0424"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0424/raw/bkstroy.kz - @StormBaseAdapter/Телефон*.csv",
                sep=";",
                encoding="windows-1251",
            )
            .withColumn("names", name_udf(col("NAME")))
            .withColumn(
                "phones", phone_udf(col("DEVICE"), lit(self.dataset_country_code.value))
            )
            .withColumn("address", address_udf(col("NAME_1")))
            .select("names", "address", "phones")
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

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
