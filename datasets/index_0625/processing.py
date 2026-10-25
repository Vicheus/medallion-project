from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array
from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import name_parts_udf, phone_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0625"
    calc_completeness: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0625/raw/users_by.csv",
                sep=";",
                header=True,
            )
            .replace("<blank>", "NULL")
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones", phone_udf(col("mobile"), lit(self.dataset_country_code.value))
            )
            .withColumn("ip_address", ip_address_udf(col("ipadd")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    struct(col("ip_address").alias("ip")),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    struct(
                        lit("Trident Crypto Fund").alias("title"),
                        col("emails").alias("login"),
                        col("password").alias("password_hash"),
                    ),
                ),
            )
            .select("names", "emails", "phones", "ips", "accounts")
        )

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
                "ips", when(col("ips").isNotNull(), array(col("ips"))).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
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
