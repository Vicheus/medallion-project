from pyspark.sql.functions import when, col, array

from parsetron import Parsetron

from parsetron.sections.main.udfs import email_udf, phone_udf, address_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0051"

    def parser(self):
        df = (
            self.read(path="Grastin (2021-2022).csv", sep=",", header=True)
            .withColumn("names", name_udf(col("buyer")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "phones", "address", "emails")
        )

        df = df.select("names", "phones", "address", "emails")
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        df.show(truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
