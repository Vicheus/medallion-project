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
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0194"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0194/raw/*.csv",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("PERSONAL_PHONE"),
                                lit(self.dataset_country_code.value),
                            ),
                            phone_udf(
                                col("PERSONAL_MOBILE"),
                                lit(self.dataset_country_code.value),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("EMAIL")))))
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Соседи").alias("title"),
                            lit("https://sosedi.by").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("PERSONAL_CITY"))))),
            )
            .select("names", "emails", "phones", "birth_date", "accounts", "address")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            flatten(collect_set(col("names"))).alias("names"),
            flatten(collect_set(col("address"))).alias("address"),
            flatten(collect_set(col("accounts"))).alias("accounts"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
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
