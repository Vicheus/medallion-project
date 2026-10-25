from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
    collect_set,
    size,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0437"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0437/raw/cian_ru.csv",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Адрес")))
        )
        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                )
            )
            .select("names", "phones", "address")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.withColumn("address", expr("slice(address, 1, 15)"))

        df = df.filter(col("names").isNotNull() & ((col("phones").isNotNull())))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
