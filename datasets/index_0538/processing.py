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
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    TimestampType,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_with_type_udf,
    address_udf,
    normalize_address_batch_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0538"

    def parser(self):
        schema = StructType(
            [
                StructField("id", IntegerType(), True),
                StructField("fio", StringType(), True),
                StructField("summa", IntegerType(), True),
                StructField("date", StringType(), True),
                StructField("time", StringType(), True),
                StructField("sdacha", StringType(), True),
                StructField("address", StringType(), True),
                StructField("comment", StringType(), True),
                StructField("created", TimestampType(), True),
                StructField("is_time", IntegerType(), True),
                StructField("phone", StringType(), True),
                StructField("is_maslo", IntegerType(), True),
                StructField("pay_type", IntegerType(), True),
                StructField("pay_state", IntegerType(), True),
            ]
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0538/raw/pirogidomoy.ru.csv",
                sep=",",
                header=True,
                schema=schema,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn(
                "address_with_type",
                address_with_type_udf(col("address"), lit(1)),
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(array(col("address_with_type"))),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "phones", "address", "addresses", "actuality")
        )

        df.show(n=20, truncate=False)

        df = df.dropDuplicates(["phones", "names"])

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
