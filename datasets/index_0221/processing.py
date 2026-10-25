from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import name_udf, email_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0221"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0221/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("username")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%m-%d-%Y")))
            .withColumn("ip_address", ip_address_udf(col("ipaddress")))
            .withColumn(
                "socials",
                when(
                    col("fbuserid").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("fbuserid").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("fbuserid"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array_compact(array(struct(col("ip_address").alias("ip")))),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("email").isNotNull(),
                    array(
                        struct(
                            lit("Клерк.ру").alias("title"),
                            lit("https://www.klerk.ru").alias("link"),
                            email_udf(col("email")).alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "ips", "birth_date", "accounts", "socials")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "names"]).agg(
            flatten(collect_set(col("ips"))).alias("ips"),
            flatten(collect_set(col("accounts"))).alias("accounts"),
            flatten(collect_set(col("socials"))).alias("socials"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
