from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    normalize_address_batch_udf,
    address_with_type_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0527"

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7 Shield/database_candidates/candidates/rustirka.ru./rustirka.ru/RUSTIRKA CLEAN.txt",
                sep="|",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "address_with_type", address_with_type_udf(col("address"), lit(1))
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(array(col("address_with_type"))),
            )
            .select("names", "phones", "address", "addresses")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
