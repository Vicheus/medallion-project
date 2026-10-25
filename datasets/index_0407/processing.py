from pyspark.sql.functions import when, col, lit, array
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    raw_metadata_udf,
    email_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0407"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0407/raw/clients_aspro_mobi_10k.csv",
                sep=",",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("edrpou"), col("edrpou"), lit("manager"), col("manager")
                ),
            )
            .select("names", "phones", "emails", "raw_metadata")
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

        df = df.repartition(self.output_file_count)

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

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
