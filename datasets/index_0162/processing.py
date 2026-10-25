from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    concat,
    regexp_replace,
    concat_ws,
    size,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0162"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0162/raw/finist-preprod.csv",
            sep="|",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                regexp_replace(
                    name_parts_udf(col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")),
                    " Y Imconnector",
                    "",
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDATE"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_FAX")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("PERSONAL_PAGER")),
                            phone_udf(col("WORK_PHONE")),
                            phone_udf(col("WORK_FAX")),
                            phone_udf(col("WORK_PAGER")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "address",
                address_udf(
                    when(
                        col("PERSONAL_CITY").isNotNull(),
                        concat_ws(
                            ", ",
                            col("PERSONAL_CITY"),
                            col("PERSONAL_ZIP"),
                            when(
                                col("PERSONAL_STREET").isNotNull(),
                                concat(lit("ул. "), col("PERSONAL_STREET")),
                            ).otherwise(None),
                        ),
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("FINIST").alias("title"),
                            lit("https://finist.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            col("ID").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_POSITION").isNotNull() | col("WORK_COMPANY").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("WORK_POSITION"),
                                    lit(None),
                                    lit(None),
                                    col("WORK_COMPANY"),
                                    address_udf(
                                        when(
                                            col("WORK_CITY").isNotNull(),
                                            concat_ws(
                                                ", ",
                                                col("WORK_CITY"),
                                                col("WORK_ZIP"),
                                                when(
                                                    col("WORK_STREET").isNotNull(),
                                                    concat(
                                                        lit("ул. "), col("WORK_STREET")
                                                    ),
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
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("LAST_LOGIN"),
                        col("DATE_REGISTER"),
                        col("LAST_ACTIVITY_DATE"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "accounts",
            "works",
            "actuality",
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = df.drop_duplicates()

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
