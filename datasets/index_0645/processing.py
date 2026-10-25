from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0645"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0645/raw/pskb.com - @bereza_bd.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("names", "emails", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.withColumn(
            "names",
            when(col("names").isNotNull(), array(col("names"))).otherwise(None),
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
