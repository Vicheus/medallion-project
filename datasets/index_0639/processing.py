from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    size,
    collect_set,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0639"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0639/raw/russkoe-slovo.ru.txt",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("address1"), col("address2")))
            )
            .select("names", "emails", "phones", "address")
        )

        df = df.groupBy(["names", "phones"]).agg(
            array_compact(collect_set(col("emails"))).alias("emails"),
            array_compact(collect_set(col("address"))).alias("address"),
        )

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
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() & col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
