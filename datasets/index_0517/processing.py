from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_compact

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0517"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Downloads/bases_new/vbh24.ru - @bereza_bd/users.csv",
                sep=";",
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_udf(col("name")),
            )
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        ).drop_duplicates(["names", "emails"])

        df = df.withColumn(
            "names",
            when(
                col("names").isNotNull(), array_compact(array(col("names")))
            ).otherwise(None),
        ).withColumn(
            "emails",
            when(
                col("emails").isNotNull(), array_compact(array(col("emails")))
            ).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
