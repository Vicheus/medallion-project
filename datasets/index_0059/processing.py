from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    address_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0059"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0059/raw/burgerkingrus.ru_08.2024_(5.627.676)_orders.csv.csv",
            sep="\t",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%d.%m.%Y")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("datetime"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("favcategory"), df["favcategory"], lit("favdish"), df["favdish"]
                ),
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "actuality",
            "raw_metadata",
        )
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
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
