from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, split, forall, length, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    dataset_code_name: str = "index_0004"
    test_mode: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0004/raw/winelab_raw.csv",
            sep="|",
            header=True,
        )

        df = df.dropDuplicates(["tel", "fio", "email"])

        # filter out rows with short name parts
        df = df.filter(forall(split(df.fio, " "), lambda e: length(e) > 2))

        df = (
            df.withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("actuality", actuality_date_udf(col("data"), lit("%Y-%m-%d")))
        )

        df = df.select("names", "emails", "phones", "actuality")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
