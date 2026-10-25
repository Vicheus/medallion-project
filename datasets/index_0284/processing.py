from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    max,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    flatten,
    collect_set,
    coalesce,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0284"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0284/raw/chipik.by/result.csv",
            sep=",",
            header=True,
        ).repartition(20)

        df = (
            df.replace("\\N", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("EMAIL")), email_udf(col("LOGIN")))
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_REGISTER"), col("LAST_LOGIN")),
                    lit("%d.%m.%Y %H:%M:%S"),
                ),
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
                            phone_udf(
                                col("WORK_PHONE"), lit(self.dataset_country_code.value)
                            ),
                            phone_udf(
                                col("LOGIN"), lit(self.dataset_country_code.value)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("chipik.by").alias("title"),
                            lit("https://chipik.by/").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("PERSONAL_CITY").isNotNull(),
                                    concat_ws(
                                        " ",
                                        col("PERSONAL_STATE"),
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_ZIP"),
                                        when(
                                            col("PERSONAL_STREET").isNotNull(),
                                            col("PERSONAL_STREET"),
                                        ).otherwise(None),
                                    ),
                                )
                            )
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "actuality")
        )

        df = (
            df.filter(size(col("phones")) > 0)
            .groupBy(["names", "emails"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_set(col("accounts"))))
                ).alias("accounts"),
                max("actuality").alias("actuality"),
            )
            .select("names", "emails", "phones", "address", "accounts", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
