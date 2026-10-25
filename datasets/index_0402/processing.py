from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0402"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0402/raw/spiritfit.ru - @StormBaseAdapter.txt",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("emails", email_udf(col("Email")))
            .select("names", "phones", "emails")
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
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
