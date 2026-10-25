from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, regexp_replace, lower

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0587"

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0587/raw/grnhs.ru.csv",
            sep=";",
            header=True,
        )

        df = df.withColumn("Name", regexp_replace(lower(col("Name")), r"не задано", ""))

        df = (
            df.withColumn("names", name_udf(col("Name")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("PhoneNumber")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("MagnetCards"), col("MagnetCards")),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("WhenCreated"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .select("names", "emails", "phones", "actuality", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
