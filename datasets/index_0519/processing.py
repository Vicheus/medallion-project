from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0519"
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0519/raw/jivo.ru (2022).txt",
                sep="\t",
            )
            .withColumn(
                "names",
                name_udf(col("ФИО")),
            )
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .select("names", "phones", "emails")
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

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
