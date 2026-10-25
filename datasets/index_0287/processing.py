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
    trim,
    concat_ws,
    max,
    coalesce,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
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
    dataset_code_name: str = "index_0287"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0287/raw/экабуд.бел/b_user.csv",
            sep=",",
            header=True,
        ).repartition(20)

        df = (
            df.filter(~col("NAME").contains("blogspot"))
            .replace("\\N", None)
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
                            lit("Магазин ЭКАБУД.БЕЛ").alias("title"),
                            lit("https://экабуд.бел").alias("link"),
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
                                    trim(
                                        concat_ws(
                                            " ",
                                            col("WORK_DEPARTMENT"),
                                            col("WORK_POSITION"),
                                        )
                                    ),
                                    lit(None),
                                    lit(None),
                                    col("WORK_COMPANY"),
                                    address_udf(
                                        when(
                                            col("WORK_CITY").isNotNull(),
                                            concat_ws(
                                                " ",
                                                col("WORK_CITY"),
                                                col("WORK_STREET"),
                                            ),
                                        )
                                    ),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "accounts", "works", "actuality")
        )

        df = df.groupBy(["names", "emails"]).agg(
            array_distinct(array_compact(flatten(collect_set(col("phones"))))).alias(
                "phones"
            ),
            array_distinct(array_compact(flatten(collect_set(col("accounts"))))).alias(
                "accounts"
            ),
            array_distinct(array_compact(flatten(collect_set(col("works"))))).alias(
                "works"
            ),
            max(col("actuality")).alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
