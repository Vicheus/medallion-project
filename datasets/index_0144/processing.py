from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    array_distinct,
    size,
    concat_ws,
    concat,
    regexp_extract,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    name_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0144"

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0144/raw/naftusia_preprocessed_2.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDATE"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn("vk", regexp_extract("PERSONAL_WWW", r"id(\d+)", 1))
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
                            lit("НАФТУСЯ ТУР").alias("title"),
                            lit("https://naftusia.com").alias("link"),
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
                                            concat(lit("ул. "), col("WORK_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("relations", array())
            .withColumn(
                "socials",
                when(
                    col("vk").isNotNull() | col("vk").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk").isNotNull() | col("vk").isNotNull(),
                                social_udf(lit("Vk"), col("vk"), lit(None), lit(None)),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
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
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "relations",
                "socials",
                "actuality",
            )
        )

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0144/raw/naftusia_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("FIO")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("PHONE")))))
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "address",
                when(
                    col("PERSONAL_CITY").isNotNull(), address_udf(col("PERSONAL_CITY"))
                ).otherwise(lit(None)),
            )
            .withColumn("accounts", array())
            .withColumn("works", array())
            .withColumn("socials", array())
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("RELATED_PERSON_1")),
                            name_udf(col("RELATED_PERSON_2")),
                            name_udf(col("RELATED_PERSON_3")),
                            name_udf(col("RELATED_PERSON_4")),
                            name_udf(col("RELATED_PERSON_5")),
                        )
                    )
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "relations",
                "socials",
                "actuality",
            )
        )

        df = df_1.unionAll(df_2).drop_duplicates()

        df = df.select(
            "names",
            "emails",
            "phones",
            "sex",
            "birth_date",
            "address",
            "accounts",
            "works",
            "relations",
            "socials",
            "actuality",
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
