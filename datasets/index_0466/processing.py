from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0466"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,address"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0466/raw/mail.ru.txt",
            sep=";",
            header=False,
            encoding="windows-1251",
        ).filter(~col("_c3").contains("Украина"))

        df = (
            df.withColumn("names", name_udf(col("_c1")))
            .withColumn("emails", email_udf(col("_c0")))
            .withColumn("address", address_udf(col("_c3")))
            .withColumn("actuality", actuality_date_udf(col("_c4"), lit("%d.%m.%Y")))
            .select("names", "emails", "address", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("address").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
