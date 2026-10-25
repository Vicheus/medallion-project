from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_distinct, array_compact, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0234"

    def parser(self):
        df_buyers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0234/raw/buyers_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("adress"))))),
            )
            .select("names", "emails", "phones", "address")
        )

        df_predzakaz = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0234/raw/predzakaz_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("delivery_adress")),
                            address_udf(col("pickup_point")),
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "address")
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0234/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("FIO")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Tel")),
                            phone_udf(col("Tel2")),
                            phone_udf(col("Tel3")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address", array_compact(array_distinct(array(address_udf(col("Adr")))))
            )
            .select("names", "emails", "phones", "address")
        )

        df = df_buyers.unionAll(df_predzakaz).unionAll(df_users)

        df = df.drop_duplicates(["names", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
