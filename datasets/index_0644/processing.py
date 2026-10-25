from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, address_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0644"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0644/raw/zacks_com.txt",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("Name")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("address", address_udf(col("City")))
            .withColumn("phones", phone_udf(col("Phone")))
            .select("names", "emails", "phones", "address")
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
