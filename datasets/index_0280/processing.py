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
    coalesce,
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
    dataset_code_name: str = "index_0280"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0280/raw/autospace/Clients.csv",
            sep=";",
            header=True,
        ).repartition(20)

        df = (
            df.replace("NULL", None)
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
                    lit("%m/%d/%Y %H:%M"),
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
                            lit("ООО Автоспейс").alias("title"),
                            lit("https://autospace.by/").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "work_position",
                trim(concat_ws(" ", col("WORK_DEPARTMENT"), col("WORK_POSITION"))),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_COMPANY").isNotNull()
                    | (col("work_position").isNotNull() & (col("work_position") != "")),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    when(
                                        col("work_position").isNotNull()
                                        & (col("work_position") != ""),
                                        col("work_position"),
                                    ).otherwise(lit(None)),
                                    lit(None),
                                    lit(None),
                                    col("WORK_COMPANY"),
                                    address_udf(
                                        when(
                                            col("WORK_CITY").isNotNull(),
                                            concat_ws(
                                                " ",
                                                col("WORK_CITY"),
                                                when(
                                                    col("WORK_STREET").isNotNull(),
                                                    col("WORK_STREET"),
                                                ).otherwise(None),
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
