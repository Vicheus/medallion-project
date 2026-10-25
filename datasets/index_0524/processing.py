from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_compact

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0524"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/shared/medicenter_2024.csv",
                sep=";",
            )
            .replace("<blank>", None)
            .withColumn(
                "names",
                name_udf(col("med_users_name")),
            )
            .withColumn("phones", phone_udf(col("med_users_phone")))
            .withColumn("emails", email_udf(col("med_users_email")))
            .select("names", "emails", "phones")
        ).drop_duplicates(["names", "emails", "phones"])

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
