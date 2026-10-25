from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, size, split

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phones_udf, email_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0236"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0236/raw/celfin.ru.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("emails")))
            .withColumn("phones", phones_udf(split(col("phones"), ";")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%m/%d/%Y"))
            )
            .select("names", "emails", "phones", "birth_date")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
