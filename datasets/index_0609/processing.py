from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    size,
    split,
    array_compact,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phones_udf, emails_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0609"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0609/raw/amocrm_contacts_202509261845.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_distinct(array_compact(phones_udf(split(col("phone"), ",")))),
            )
            .withColumn(
                "emails",
                array_distinct(array_compact(emails_udf(split(col("email"), ",")))),
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
