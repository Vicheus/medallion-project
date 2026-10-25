from pyspark import StorageLevel
from pyspark.sql.functions import when, col, struct, array, size

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import name_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0262"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0262/raw/users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("author_name")))
            .withColumn("emails", email_udf(col("author_email")))
            .withColumn("ip_address", ip_address_udf(col("author_ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ).otherwise(array()),
            )
            .select("names", "emails", "ips")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
