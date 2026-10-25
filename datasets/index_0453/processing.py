from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, size
from parsetron import Parsetron

from parsetron.sections.main.udfs import name_parts_udf, email_udf, raw_metadata_udf
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0453"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0453/raw/digital.gov.ru - @StormInDataBase.csv",
            sep="|",
            header=True,
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("login_name"),
                    col("login_name"),
                    lit("display_name"),
                    col("display_name"),
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("company").isNotNull()),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "emails", "works", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
