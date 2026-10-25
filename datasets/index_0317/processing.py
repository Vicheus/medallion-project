from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0317"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0317/raw/orders_info_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("city"), col("address")))
            )
            .withColumn(
                "actuality", actuality_date_udf(col("order_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("company"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "address", "works", "actuality")
        )

        df = df.drop_duplicates(["names", "phones", "emails"])
        df = df.filter(col("names") != "Bam")

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
