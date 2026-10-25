from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, coalesce, concat_ws

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0303"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0303/raw/rusgym33_reg.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date",
                coalesce(
                    birth_date_udf(col("date_bd"), lit("%Y-%m-%d")),
                    birth_date_udf(col("date_bd"), lit("%d.%m.%Y")),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date_reg"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "address", address_udf(concat_ws(" ", col("region"), col("city")))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("weight"),
                    col("weight"),
                    lit("trainer"),
                    col("trainer"),
                    lit("nomination"),
                    col("nomination"),
                ),
            )
            .select(
                "names",
                "phones",
                "sex",
                "birth_date",
                "actuality",
                "address",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.drop_duplicates(["phones"])

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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
