from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, greatest

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0094"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0094/raw/Rostelecom_2021_700k.csv",
            sep=",",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("fullname")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("last_sign_in_at"), col("updated_at"), col("created_at")
                    ),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
            .select("names", "phones", "emails", "actuality")
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
