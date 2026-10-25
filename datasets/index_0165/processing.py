from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0165"

    def parser(self):
        df_call_client = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0165/raw/call_client_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "emails",
                email_udf(
                    regexp_extract(
                        col("email"),
                        r"^[a-zA-Z0-9._%+-]+@(mail\.ru|yandex\.ru|gmail\.com)$",
                        0,
                    )
                ),
            )
            .withColumn("address", array())
            .select("names", "emails", "phones", "address")
        )

        df_phonebook = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0165/raw/phonebook_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", lit(None))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("city"))))),
            )
            .select("names", "emails", "phones", "address")
        )

        df_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0165/raw/customers_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("addphone")),
                            phone_udf(col("mobilephone")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .select("names", "emails", "phones", "address")
        )

        df = (
            df_call_client.unionAll(df_phonebook)
            .unionAll(df_customers)
            .drop_duplicates()
        )

        df = df.select("names", "emails", "phones", "address")

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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
