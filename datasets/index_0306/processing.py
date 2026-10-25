from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0306"

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0306/raw/kreditovka.ru/finotdel.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .filter(~col("email").like("%google.com"))
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("city")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("raw_metadata", raw_metadata_udf(lit("summa"), col("summa")))
            .select("names", "address", "emails", "raw_metadata")
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0306/raw/kreditovka.ru/users.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .filter(~col("email").like("%google.com"))
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("city")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select("names", "address", "emails", "raw_metadata")
        )

        df = df_users_1.unionAll(df_users_2).drop_duplicates(["emails"])
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
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
