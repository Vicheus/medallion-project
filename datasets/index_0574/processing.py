from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0574"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0574/raw/*_output.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fullname_ru")))
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones")
        )

        df = df.drop_duplicates(["names", "phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
