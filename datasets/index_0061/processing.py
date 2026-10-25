from pyspark.sql.functions import when, col, lit, array, coalesce

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
    sex_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0061"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0061/raw/Tele2_2022_7.5M.txt",
            sep="\t",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("NAME")))
            .withColumn("phones", phone_udf(col("MSISDN")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("sex", sex_udf(col("SEX")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("CREATED"), col("LAST_UPD")),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
        )
        df = df.select("names", "emails", "phones", "sex", "actuality")
        df = df.dropDuplicates(["names", "emails", "phones"])

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
