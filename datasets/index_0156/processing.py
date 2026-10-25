from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    concat,
    size,
    max,
    greatest,
    concat_ws,
    coalesce,
    regexp_extract,
    flatten,
    collect_set,
    first,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
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
    dataset_code_name: str = "index_0156"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0156/raw/zonatelecom_cleaned.csv",
                sep="|",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")),
            )
            .withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 0))
            .withColumn("vk_id", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
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
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("EMAIL")), email_udf(col("PERSONAL_MAILBOX"))
                        )
                    )
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
                                            concat(lit("ул. "), col("PERSONAL_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            )
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
                            lit("Zonatelecom").alias("title"),
                            lit("http://zt.ru").alias("link"),
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
                    col("WORK_POSITION").isNotNull()
                    | col("WORK_DEPARTMENT").isNotNull()
                    | col("WORK_COMPANY").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    coalesce(col("WORK_POSITION"), col("ADMIN_NOTES")),
                                    lit(None),
                                    lit(None),
                                    concat_ws(
                                        " ", col("WORK_COMPANY"), col("WORK_DEPARTMENT")
                                    ),
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
            .withColumn("documents", array())
            .withColumn("relations", array())
            .withColumn(
                "socials",
                when(
                    col("vk_link").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_link").isNotNull(),
                                social_udf(
                                    lit("Vk"), col("vk_id"), col("vk_link"), lit(None)
                                ),
                            ).otherwise(None)
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
            "documents",
            "socials",
            "relations",
            "actuality",
        )

        df_imprisoned = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0156/raw/imprisoned_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("payer_full_name")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("payer_snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("payer_snils").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ).otherwise(None),
                            when(
                                col("payer_passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("payer_passport").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            concat_ws(
                                " ",
                                name_udf(col("imprisoned_full_name")),
                                lit("Год рождения:"),
                                col("imprisoned_yearbirth"),
                                col("imprisoned_colony"),
                                lit("Получатель денежного перевода."),
                            ),
                        )
                    )
                ),
            )
            .withColumn("socials", array())
            .withColumn("works", array())
            .withColumn("address", array())
            .withColumn(
                "emails",
                array_compact(array_distinct(array(email_udf(col("payer_email"))))),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("payer_tel"))))),
            )
            .withColumn("accounts", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
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
                "documents",
                "socials",
                "relations",
                "actuality",
            )
        )

        df_imprisoned = (
            df_imprisoned.filter(
                col("documents")[0]["serial"].isNotNull() & col("names").isNotNull()
            )
            .groupby(
                col("names"), col("documents")[0]["serial"], col("documents")[0]["type"]
            )
            .agg(
                first("birth_date").alias("birth_date"),
                first("sex").alias("sex"),
                array_compact(flatten(collect_set("emails"))).alias("emails"),
                array_compact(flatten(collect_set("phones"))).alias("phones"),
                array_compact(flatten(collect_set("address"))).alias("address"),
                array_compact(flatten(collect_set("accounts"))).alias("accounts"),
                array_compact(flatten(collect_set("works"))).alias("works"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("socials"))).alias("socials"),
                array_compact(flatten(collect_set("relations"))).alias("relations"),
                max("actuality").alias("actuality"),
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
                "documents",
                "socials",
                "relations",
                "actuality",
            )
        )

        df = df.unionAll(df_imprisoned)

        df = df.drop_duplicates()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
            | col("documents").isNotNull()
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
