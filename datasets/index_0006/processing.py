from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, from_json, size, lit
from pyspark.sql.types import ArrayType, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import names_udf, emails_udf, phones_udf, address_udf, address_with_type_udf, normalize_address_batch_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0006"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0006/raw/ru_cdek_contragent_30m_2022.csv",
            sep=";",
            header=True,
        )

        df = df.dropDuplicates(["names", "address", "phones", "emails"])
        df = (
            df.withColumn(
                "names", names_udf(from_json(col("names"), ArrayType(StringType())))
            )
            .withColumn(
                "phones", phones_udf(from_json(col("phones"), ArrayType(StringType())))
            )
            .withColumn(
                "emails", emails_udf(from_json(col("emails"), ArrayType(StringType())))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("address_with_type", address_with_type_udf(col("address"), lit(1)))
            .withColumn('addresses', normalize_address_batch_udf(array(col('address_with_type'))))
        )

        df = df.select("names", "address", "addresses", "emails", "phones")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "addresses", when(size(col("addresses")) > 0, col("addresses")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
