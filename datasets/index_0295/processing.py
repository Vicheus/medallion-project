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
    coalesce,
    concat_ws,
    flatten,
    collect_set,
    max,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0295"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0295/raw/stroydvor.su_15.csv",
            sep="|",
            header=True,
        ).replace("NULL", None)

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_REGISTER"), col("LAST_LOGIN")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("WORK_PHONE")),
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
                            lit("СтройДвор").alias("title"),
                            lit("https://stroydvor.su/").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_COMPANY").isNotNull()
                    | col("WORK_DEPARTMENT").isNotNull()
                    | col("WORK_POSITION").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    concat_ws(
                                        " ",
                                        col("WORK_DEPARTMENT"),
                                        col("WORK_POSITION"),
                                    ),
                                    lit(None),
                                    lit(None),
                                    col("WORK_COMPANY"),
                                    lit(None),
                                    lit(None),
                                )
                            )
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
                                concat_ws(
                                    " ",
                                    col("PERSONAL_STATE"),
                                    col("PERSONAL_CITY"),
                                    col("PERSONAL_ZIP"),
                                    col("PERSONAL_STREET"),
                                )
                            )
                        )
                    )
                ),
            )
            .select(
                "names", "emails", "phones", "address", "accounts", "works", "actuality"
            )
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_set(col("accounts"))))
                ).alias("accounts"),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names", "emails", "phones", "actuality", "address", "accounts", "works"
            )
        )

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
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
