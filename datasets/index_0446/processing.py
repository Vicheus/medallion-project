from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0446"

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/new/pleer.ru_3.7m/pleer_ru.csv",
            sep="\t",
            header=True,
        )

        df = df.filter(
            (~col("phone").startswith("38")) & (~col("city").isin("Киев", "Ровно"))
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("city")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "phones", "emails", "address")
        )

        df = df.drop_duplicates(["names", "phones"])

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
