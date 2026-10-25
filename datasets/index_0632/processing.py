from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0632"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_contacts = (
            self.read(
                path="/home/user/Documents/data/index_0632/raw/deppul.ru - @bd_bereza/contact.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("C_FIRSTNAME"), col("C_LASTNAME"), col("C_MIDDLENAME")
                ),
            )
            .withColumn("emails", email_udf(col("C_EMAILADDRESS")))
            .withColumn("accounts", lit(None))
            .select("names", "emails", "accounts")
        )

        df_customers = (
            self.read(
                path="/home/user/Documents/data/index_0632/raw/deppul.ru - @bd_bereza/sc_customers.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "accounts",
                when(
                    col("Login").isNotNull() & col("cust_password").isNotNull(),
                    struct(
                        lit("DePPul.ru").alias("title"),
                        lit("http://deppul.ru").alias("link"),
                        col("Login").alias("login"),
                        col("cust_password").alias("password"),
                    ),
                ),
            )
            .select("names", "emails", "accounts")
        )

        df = df_contacts.unionAll(df_customers)

        df = (
            df.groupBy(["emails"])
            .agg(
                array_compact(array_distinct(collect_list(col("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(collect_list(col("accounts")))).alias(
                    "accounts"
                ),
            )
            .select("names", "emails", "accounts")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
