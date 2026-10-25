from pyspark.sql.functions import when, col, array
from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0409"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0409/raw/contacts_cmexpert_ru_40k_2025.csv",
                sep=",",
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("phones", phone_udf(col("Phone")))
            .select("names", "phones")
        )

        df = df.drop_duplicates(["names", "phones"])

        df = df.repartition(self.output_file_count)

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
