from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
    array_compact,
    collect_set,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import name_parts_udf, phone_udf, email_udf
from parsetron.sections.ips.udfs import ip_address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0641"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/T7/datasets/index_0641/raw/users_kz_members.csv",
                sep=";",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip", ip_address_udf(col("ipadd")))
            .withColumn(
                "phones", phone_udf(col("mobile"), lit(self.dataset_country_code.value))
            )
            .withColumn(
                "ips",
                when(col("ip").isNotNull(), struct(col("ip").alias("ip"))),
            )
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("email").isNotNull(),
                    struct(
                        lit("123RF").alias("title"),
                        lit("https://www.123rf.com/").alias("link"),
                        col("email").alias("login"),
                        col("password").alias("password_hash"),
                    ),
                ),
            )
            .select("names", "phones", "emails", "ips", "accounts")
        )

        df = (
            df.groupBy(["names", "ips"])
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(collect_set(col("accounts"))).alias("accounts"),
            )
            .select("names", "phones", "emails", "ips", "accounts")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "ips", when(col("ips").isNotNull(), array(col("ips"))).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
