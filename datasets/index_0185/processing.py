from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    flatten,
    collect_set,
    max,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0185"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("date", StringType(), True),
                StructField("unknown_field_1", StringType(), True),
                StructField("email", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("email2", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("address1", StringType(), True),
                StructField("email3", StringType(), True),
                StructField("address2", StringType(), True),
                StructField("unknown_field_2", StringType(), True),
            ]
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0185/raw/ostrov_chistoty.csv",
                sep=";",
                header=False,
                schema=schema,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("phone"), lit(self.dataset_country_code.value)
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address1")), address_udf(col("address2"))
                        )
                    )
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            flatten(collect_set(col("names"))).alias("names"),
            flatten(collect_set(col("address"))).alias("address"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
