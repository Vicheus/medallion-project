from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_parts_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0391"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0391/raw/iglobe.ru/iglobe_clean.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("FirstName"), col("LastName"), lit(None))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("Email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("Phone")))))
            )
            .select("names", "emails", "phones")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
