from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    from_unixtime,
    split,
    array,
    array_distinct,
    array_compact,
    concat,
    coalesce,
    concat_ws,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    name_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0171"

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("ip", ip_address_udf(col("reg_ip")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("phone_2")))
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("forum_email")))
                    )
                ),
            )
            .withColumn(
                "birth_date",
                when(
                    col("birth_day") > 0,
                    birth_date_udf(
                        from_unixtime(col("birth_day"), "yyyy-MM-dd HH:mm:ss"),
                        lit("%Y-%m-%d %H:%M:%S"),
                    ),
                ).otherwise(lit(None)),
            )
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(col("adress")),
                            address_udf(
                                when(
                                    (col("street").isNotNull()) & (col("street") != ""),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("city_index") != "", col("city_index")
                                        ).otherwise(None),
                                        when(col("city") != "", col("city")).otherwise(
                                            None
                                        ),
                                        col("street"),
                                        when(
                                            col("house") != "",
                                            concat(lit("б. "), col("house")),
                                        ).otherwise(None),
                                        when(
                                            col("appartment") != "",
                                            concat(lit("кв. "), col("appartment")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("UltraTrade").alias("title"),
                            lit("https://ultratrade.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("reg_ip").isNotNull(), array(struct(col("reg_ip").alias("ip")))
                ),
            )
            .withColumn("socials", array())
            .withColumn("coordinates", array())
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
        )
        df_users_1.cache()

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/users2.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("address", array())
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn(
                "socials",
                when(
                    col("telegram").isNotNull() & (col("telegram") != ""),
                    array_compact(
                        array(
                            when(
                                col("telegram").isNotNull() & (col("telegram") != ""),
                                social_udf(
                                    lit("Telegram"),
                                    col("telegram"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("coordinates", array())
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
        )
        df_users_2.cache()

        df_users_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/users3.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("city"))))),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn("coordinates", array())
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
        )
        df_users_3.cache()

        df_users_4 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/users4.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", array())
            .withColumn("birth_date", lit(None))
            .withColumn("address", array())
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn("coordinates", array())
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
            .drop_duplicates()
        )
        df_users_4.cache()

        df_users_5 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/users5.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone_2")),
                            phone_udf(col("phone_3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email_2")))
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(
                                when(
                                    (col("adress").isNotNull()) & (col("adress") != ""),
                                    concat_ws(
                                        ", ",
                                        when(
                                            coalesce(
                                                col("city_index"), col("post_code")
                                            )
                                            != "",
                                            coalesce(
                                                col("city_index"), col("post_code")
                                            ),
                                        ).otherwise(None),
                                        when(col("city") != "", col("city")).otherwise(
                                            None
                                        ),
                                        col("adress"),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    )
                ),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn("lat", split(col("coord"), " ")[1])
            .withColumn("long", split(col("coord"), " ")[0])
            .withColumn(
                "coordinates",
                when(
                    (
                        col("long").isNotNull()
                        & (col("long") != 0.0)
                        & col("lat").isNotNull()
                        & (col("lat") != 0.0)
                    ),
                    array(array(col("long").cast("float"), col("lat").cast("float"))),
                ).otherwise(None),
            )
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
            .drop_duplicates()
        )
        df_users_5.cache()

        df_companies = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0171/raw/preprocessed/companies_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("company_name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(array(address_udf(col("company_ur_adress"))))
                ),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn("coordinates", array())
            .withColumn(
                "documents",
                when(
                    col("company_inn").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("company_inn").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("company_inn"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("company_bank"), col("company_bank")),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "ips",
                "socials",
                "coordinates",
                "documents",
                "raw_metadata",
            )
            .drop_duplicates()
        )
        df_companies.cache()

        df = (
            df_users_1.unionAll(df_users_2)
            .unionAll(df_users_3)
            .unionAll(df_users_4)
            .unionAll(df_users_5)
            .unionAll(df_companies)
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "coordinates",
                when(size(col("coordinates")) > 0, col("coordinates")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
