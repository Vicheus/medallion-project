from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    struct,
    array_distinct,
    array_compact,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf
from pyspark import StorageLevel


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0507"
    output_file_count: int = 3

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0507/raw/dikidi.ru.txt",
                header=True,
                sep="\t",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "ip_address",
                when(
                    ((col("ip") != "127.0.0.1") & (col("ip") != "null")),
                    ip_address_udf(col("ip")),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("insert"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .select("names", "phones", "emails", "ips", "actuality")
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(),
                    array_compact(array_distinct(array(col("emails")))),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ips").isNotNull(),
                    array_compact(array_distinct(array(col("ips")))),
                ).otherwise(None),
            )
        )
        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )
        df = df.select("names", "phones", "emails", "ips", "actuality")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
