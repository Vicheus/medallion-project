from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    collect_set,
    flatten,
    array_compact,
    greatest,
    regexp_extract,
    size,
    concat_ws,
    concat,
    struct,
    split,
    explode,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    birth_date_udf,
    sex_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0174"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"
        twitter_pattern = r"https://twitter.com/([a-zA-Z0-9_]+)"
        ok_pattern = r"http://odnoklassniki.ru/profile/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"

        df_emails = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0174/raw/fitomarket.ru_DB/email_ip_248k.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .replace("\t", None)
            .replace("``", "`")
            .withColumn("USER_ID", col("USER_ID").cast("int"))
            .withColumn("EMAIL2", email_udf(col("EMAIL")))
            .withColumn("IP_SPLIT", split(col("IP"), ","))
            .withColumn("EXPLODED_IP", explode(col("IP_SPLIT")))
            .withColumn("IP", ip_address_udf(col("EXPLODED_IP")))
            .groupBy("USER_ID")
            .agg(
                collect_set("EMAIL2").alias("EMAIL2"),
                array_compact(
                    array_distinct(
                        collect_set(
                            when(
                                col("IP").isNotNull(),
                                array(
                                    struct(
                                        col("IP").alias("ip"), lit(None).alias("date")
                                    )
                                ),
                            )
                        )
                    )
                ).alias("ips"),
            )
            .select("USER_ID", "EMAIL2", "ips")
            .drop_duplicates(["USER_ID", "EMAIL2", "ips"])
        )

        df_emails.show(n=20, truncate=False)

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0174/raw/fitomarket.ru_DB/fitomarket_users_281k.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .replace("\tNULL", None)
            .replace("``", "`")
        )

        df = (
            df.join(df_emails, df_emails["USER_ID"] == df["ID"], "left")
            .withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 0))
            .withColumn(
                "facebook_link", regexp_extract("PERSONAL_WWW", facebook_pattern, 0)
            )
            .withColumn("ok_link", regexp_extract("PERSONAL_WWW", ok_pattern, 0))
            .withColumn(
                "twitter_link", regexp_extract("PERSONAL_WWW", twitter_pattern, 0)
            )
            .withColumn(
                "instagram_link", regexp_extract("PERSONAL_WWW", instagram_pattern, 0)
            )
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
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        concat(array(email_udf(col("EMAIL"))), col("EMAIL2"))
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
                                        ", ",
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
                            lit("Фитомаркет").alias("title"),
                            lit("https://fitomarket.ru").alias("link"),
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
                "socials",
                when(
                    col("vk_link").isNotNull()
                    | col("facebook_link").isNotNull()
                    | col("ok_link").isNotNull()
                    | col("twitter_link").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_link").isNotNull(),
                                social_udf(
                                    lit("Vk"), lit(None), col("vk_link"), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_link").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    lit(None),
                                    col("facebook_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("ok_link").isNotNull(),
                                social_udf(
                                    lit("Ok"), lit(None), col("ok_link"), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_link").isNotNull(),
                                social_udf(
                                    lit("Twitter"),
                                    lit(None),
                                    col("twitter_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_link").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    lit(None),
                                    col("instagram_link"),
                                    lit(None),
                                ),
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
            "ips",
            "socials",
            "actuality",
        )

        df = df.drop_duplicates()

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
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(col("ips")) > 0,
                    array_compact(array_distinct(flatten(col("ips")))),
                ).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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
