from pyspark.sql.functions import when, col, lit, array
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron

from parsetron.sections.main.udfs import birth_date_udf, phone_udf, email_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0045"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails"

    def parser(self):
        schema = (
            StructType()
            .add("names", StringType(), True)
            .add("phone", StringType(), True)
            .add("birthday", StringType(), True)
            .add("email", StringType(), True)
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0045/raw/sber.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df = (
            df.replace("null", None)
            .withColumn("names", name_udf(col("names")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%m.%Y")))
        )

        df = df.select("names", "phones", "emails", "birth_date")

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
