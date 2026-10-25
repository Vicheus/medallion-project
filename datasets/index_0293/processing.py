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
    trim,
    regexp_replace,
    regexp_extract,
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
    dataset_code_name: str = "index_0293"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0293/raw/holzmebel.ru_5_2024.csv",
            sep="|",
            header=True,
        )

        vk_pattern = r"https?://vk\.com/([^/]+)"
        instagram_pattern = r"https?://instagram\.com/([^/]+)"

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_REGISTER"), col("LAST_LOGIN")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("vk_id", regexp_extract(col("PERSONAL_WWW"), vk_pattern, 1))
            .withColumn(
                "instagram_id",
                regexp_extract(col("PERSONAL_WWW"), instagram_pattern, 1),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
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
                            lit("HOLZmebel").alias("title"),
                            lit("https://holzmebel.ru/").alias("link"),
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
                                    regexp_replace(
                                        trim(
                                            concat_ws(
                                                " ",
                                                col("WORK_DEPARTMENT"),
                                                col("WORK_POSITION"),
                                            )
                                        ),
                                        "-",
                                        "",
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
                                when(
                                    col("PERSONAL_CITY").isNotNull(),
                                    concat_ws(
                                        " ",
                                        col("PERSONAL_STATE"),
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_ZIP"),
                                        col("PERSONAL_STREET"),
                                    ),
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull() | col("instagram_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                struct(
                                    lit("ВКонтакте").alias("title"),
                                    col("vk_id").alias("id"),
                                    col("PERSONAL_WWW").alias("link"),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_id").isNotNull(),
                                struct(
                                    lit("Instagram").alias("title"),
                                    col("instagram_id").alias("id"),
                                    col("PERSONAL_WWW").alias("link"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "emails",
                "birth_date",
                "sex",
                "phones",
                "address",
                "accounts",
                "works",
                "socials",
                "actuality",
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
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
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
