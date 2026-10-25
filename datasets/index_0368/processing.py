from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_compact, collect_set, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0368"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0368/raw/заказы_Буффет24.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Имя клиента")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Адрес доставки")))
            .select("names", "phones", "address")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(array_compact(collect_set(col("address"))).alias("address"))
            .select("names", "phones", "address")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
