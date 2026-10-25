from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, size

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0292"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0292/raw/opendata_fssp_gov_ru/data.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("phones", phone_udf(col("Number")))
            .withColumn(
                "works",
                when(
                    col("Agency name").isNotNull() | col("Post").isNotNull(),
                    array(
                        work_udf(
                            col("Post"),
                            lit(None),
                            lit(None),
                            col("Agency name"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "works")
        )

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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
