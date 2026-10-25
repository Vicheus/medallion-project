from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    to_date,
    date_format,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0196"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0196/raw/customers*.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("First Name"), col("Last Name"), lit(None))
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "address", address_udf(regexp_replace(col("Address"), "Кладр \d+", ""))
            )
            .withColumn(
                "birth_date",
                birth_date_udf(
                    date_format(to_date(col("Birthday"), "MMMM d, yyyy"), "yyyy-MM-dd"),
                    lit("%Y-%m-%d"),
                ),
            )
            .select("names", "emails", "phones", "address", "birth_date")
        )

        df.show(n=30, truncate=False)

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
