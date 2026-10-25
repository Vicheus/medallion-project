from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    regexp_replace,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0518"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Downloads/bases_new/ru_business_persons.csv",
                sep=",",
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_udf(regexp_replace(col("name"), "Mr|Ms", "")),
            )
            .withColumn("emails", email_udf(col("b_email")))
            .withColumn("phones", phone_udf(col("b_phone")))
            .withColumn(
                "works",
                when(
                    (col("company").isNotNull() | col("title").isNotNull()),
                    array(
                        work_udf(
                            col("title"),
                            lit(None),
                            lit(None),
                            col("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "emails", "works")
        )

        df = (
            df.withColumn(
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
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
