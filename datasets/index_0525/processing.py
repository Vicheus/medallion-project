from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    struct,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0525"
    calc_completeness: bool = False
    output_file_count: int = 5
    validate_invalid_groupping: bool = True

    def parser(self):
        df_1 = (
            self.read(
                path="/home/user/Documents/data/bosco/users_b_form_result.csv",
                sep=";",
                header=True,
            )
            .drop_duplicates(["email_1"])
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("emails", array_compact(array(email_udf(col("email_1")))))
            .withColumn("phones", lit(None))
            .withColumn("address", lit(None))
            .withColumn("addresses", array())
            .withColumn("socials", array())
            .withColumn("accounts", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "address",
                "addresses",
                "socials",
                "accounts",
                "actuality",
            )
        )

        df_2 = (
            self.read(
                path="/home/user/Documents/data/bosco/users_b_sale_order_props.csv",
                sep=";",
                header=True,
            )
            .drop_duplicates(["email"])
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "addresses_with_type",
                array_compact(
                    array_distinct(array(address_with_type_udf(col("address"), lit(1))))
                ),
            )
            .withColumn(
                "addresses",
                array_compact(
                    array_distinct(
                        normalize_address_batch_udf(col("addresses_with_type"))
                    )
                ),
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("lastname"), lit(None))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("socials", array())
            .withColumn("accounts", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "address",
                "addresses",
                "socials",
                "accounts",
                "actuality",
            )
        )

        df_2.cache()

        df_3 = self.read(
            path="/home/user/Documents/data/bosco/users_b_user.csv",
            sep=";",
            header=True,
        )
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"

        df_3 = (
            df_3.withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("LOGIN")), email_udf(col("EMAIL")))
                    )
                ),
            )
            .withColumn(
                "phones",
                phone_udf(col("PERSONAL_PHONE")),
            )
            .withColumn("social_link", col("PERSONAL_WWW"))
            .withColumn("vk_id", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "facebook_id", regexp_extract("PERSONAL_WWW", facebook_pattern, 1)
            )
            .withColumn("address", lit(None))
            .withColumn("addresses", array())
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Bosco.ru – группа компаний Bosco di Ciliegi").alias(
                                "title"
                            ),
                            lit("https://bosco.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull() | col("facebook_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull() & (col("vk_id") != ""),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull()
                                & (col("facebook_id") != ""),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "address",
                "addresses",
                "socials",
                "accounts",
                "actuality",
            )
        )

        df_4 = (
            self.read(
                path="/home/user/Documents/data/bosco/users_b_uts_fuser.csv",
                sep=";",
                header=True,
            )
            .filter(col("UF_USER_ID").isNull())
            .drop_duplicates(["UF_EMAIL"])
            .withColumn("address", lit(None))
            .withColumn("addresses", array())
            .withColumn("names", name_udf(col("UF_NAME")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("emails", array_compact(array(email_udf(col("UF_EMAIL")))))
            .withColumn("phones", phone_udf(col("UF_PHONE")))
            .withColumn("socials", array())
            .withColumn("accounts", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "address",
                "addresses",
                "socials",
                "accounts",
                "actuality",
            )
        )

        df = df_1.unionAll(df_2).unionAll(df_3).unionAll(df_4)

        df = df.drop_duplicates(["emails"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df.cache()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(
                    size(array_compact(col("addresses"))) > 0,
                    array_compact(col("addresses")),
                ).otherwise(None),
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
