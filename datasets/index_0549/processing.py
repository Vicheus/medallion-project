from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array_compact,
    size,
    array,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0549"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0549/raw/росhtа.ru - @StormBaseAdapter.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", array_compact(array(name_udf("name"))))
            .withColumn(
                "address",
                array(
                    address_udf(col("display_address")),
                    address_udf(concat_ws(" ", col("index"), col("address"))),
                ),
            )
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .select("names", "address", "phones")
        )

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
