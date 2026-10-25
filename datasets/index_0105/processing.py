from pyspark import StorageLevel
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col, lit, when, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    name_parts_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0105"

    def parser(self):
        schema = StructType(
            [
                StructField("last_name", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("sex", StringType(), True),
                StructField("email", StringType(), True),
                StructField("phone", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0105/raw/helix2023.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones", "emails", "birth_date", "sex")
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
