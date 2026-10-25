from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    concat,
    struct,
    concat_ws,
    regexp_extract,
    size,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
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
    relations_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0169"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0169/raw/users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("firstname"), col("lastname"), col("patronymic")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_date", birth_date_udf(col("birth"), lit("%d.%M.%Y")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone_mobile")), phone_udf(col("workphone"))
                        )
                    )
                ),
            )
            .withColumn("ip", ip_address_udf(col("last_ip")))
            .withColumn(
                "VK",
                when(
                    col("social").rlike(r"https://(m\.)?vk\.com/([a-zA-Z0-9_]+)"),
                    regexp_extract(
                        "social", r"https://(m\.)?vk\.com/([a-zA-Z0-9_]+)", 2
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "OK",
                when(
                    col("social").rlike(r"https://ok\.ru/profile/(\d+)"),
                    regexp_extract("social", r"https://ok\.ru/profile/(\d+)", 1),
                ).otherwise(None),
            )
            .withColumn(
                "Mailru",
                when(
                    col("social").rlike(r"https://my\.mail\.ru/mail/([a-zA-Z0-9_]+)"),
                    regexp_extract(
                        "social", r"https://my\.mail\.ru/mail/([a-zA-Z0-9_]+)", 1
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "Facebook",
                when(
                    col("social").rlike(
                        r"https://www\.facebook\.com/profile\.php\?id=(\d+)"
                    ),
                    regexp_extract(
                        "social",
                        r"https://www\.facebook\.com/profile\.php\?id=(\d+)",
                        1,
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "Telegram",
                when(
                    col("social").rlike(r"@([a-zA-Z0-9_]+)"),
                    regexp_extract("social", r"@([a-zA-Z0-9_]+)", 1),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("passport_serial").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport_serial").alias("serial"),
                                    col("passport_date").alias("date_issue"),
                                    col("passport_issued").alias("date_expire"),
                                    lit(None).alias("authority"),
                                    regexp_replace(
                                        col("passport_issued_by"), r"[^0-9]", ""
                                    ).alias("authority_code"),
                                ),
                            ),
                            when(
                                col("inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
                            when(
                                col("snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("snils").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
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
                                concat_ws(
                                    ", ",
                                    when(
                                        col("regindex").isNotNull(), col("regindex")
                                    ).otherwise(None),
                                    when(
                                        col("regregion").isNotNull(), col("regregion")
                                    ).otherwise(None),
                                    when(
                                        col("regdistrict").isNotNull(),
                                        col("regdistrict"),
                                    ).otherwise(None),
                                    when(
                                        col("regcity").isNotNull(), col("regcity")
                                    ).otherwise(None),
                                    when(
                                        col("reglocality").isNotNull(),
                                        col("reglocality"),
                                    ).otherwise(None),
                                    when(
                                        col("regstreet").isNotNull(), col("regstreet")
                                    ).otherwise(None),
                                    when(
                                        col("reghouse").isNotNull(),
                                        concat(lit("д. "), col("reghouse")),
                                    ).otherwise(None),
                                    when(
                                        col("regflat").isNotNull(),
                                        concat(lit("кв. "), col("regflat")),
                                    ).otherwise(None),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    ", ",
                                    when(
                                        col("faktindex").isNotNull(), col("faktindex")
                                    ).otherwise(None),
                                    when(
                                        col("faktregion").isNotNull(), col("faktregion")
                                    ).otherwise(None),
                                    when(
                                        col("faktdistrict").isNotNull(),
                                        col("faktdistrict"),
                                    ).otherwise(None),
                                    when(
                                        col("faktcity").isNotNull(), col("faktcity")
                                    ).otherwise(None),
                                    when(
                                        col("faktlocality").isNotNull(),
                                        col("faktlocality"),
                                    ).otherwise(None),
                                    when(
                                        col("faktstreet").isNotNull(), col("faktstreet")
                                    ).otherwise(None),
                                    when(
                                        col("fakthouse").isNotNull(),
                                        concat(lit("д. "), col("fakthouse")),
                                    ).otherwise(None),
                                    when(
                                        col("faktflat").isNotNull(),
                                        concat(lit("кв. "), col("faktflat")),
                                    ).otherwise(None),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            ip_date_udf(col("last_activity")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("workplace").isNotNull() | col("profession").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                col("profession"),
                                lit(None),
                                lit(None),
                                col("workplace"),
                                address_udf(
                                    when(
                                        col("workaddress").isNotNull(),
                                        col("workaddress"),
                                    ).otherwise(None)
                                ),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("VK").isNotNull() & (col("VK").isNotNull() != ""),
                    array_compact(
                        array(
                            when(
                                col("VK").isNotNull() & (col("VK").isNotNull() != ""),
                                social_udf(lit("Vk"), col("VK"), lit(None), lit(None)),
                            ).otherwise(None),
                            when(
                                col("OK").isNotNull() & (col("OK").isNotNull() != ""),
                                social_udf(lit("Ok"), col("OK"), lit(None), lit(None)),
                            ).otherwise(None),
                            when(
                                col("Mailru").isNotNull()
                                & (col("Mailru").isNotNull() != ""),
                                social_udf(
                                    lit("Мой мир Mail.ru"),
                                    col("Mailru"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("Facebook").isNotNull()
                                & (col("Facebook").isNotNull() != ""),
                                social_udf(
                                    lit("Facebook"),
                                    col("Facebook"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("Telegram").isNotNull()
                                & (col("Telegram").isNotNull() != ""),
                                social_udf(
                                    lit("Telegram"),
                                    col("Telegram"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    col("contact_person_name").isNotNull()
                    | col("contact_person2_name").isNotNull()
                    | col("contact_person3_name").isNotNull()
                    | col("chief_name").isNotNull(),
                    array(
                        when(
                            col("contact_person_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("contact_person_name")),
                                    phone_udf(col("contact_person_phone")),
                                    col("contact_person_relation"),
                                )
                            ),
                        ).otherwise(None),
                        when(
                            col("contact_person2_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("contact_person2_name")),
                                    phone_udf(col("contact_person2_phone")),
                                    col("contact_person2_relation"),
                                )
                            ),
                        ).otherwise(None),
                        when(
                            col("contact_person3_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("contact_person3_name")),
                                    phone_udf(col("contact_person3_phone")),
                                    col("contact_person3_relation"),
                                )
                            ),
                        ).otherwise(None),
                        when(
                            col("chief_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("chief_name")),
                                    phone_udf(col("chief_phone")),
                                    lit("директор"),
                                )
                            ),
                        ).otherwise(None),
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "socials",
                "ips",
                "relations",
                "sex",
                "birth_date",
                "documents",
            )
        )

        df_users.persist(StorageLevel.DISK_ONLY).count()

        df_relations = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0169/raw/relations_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("ips", array())
            .withColumn("works", array())
            .withColumn("socials", array())
            .withColumn(
                "relations",
                when(
                    col("related_user").isNotNull(),
                    array(
                        when(
                            col("related_user").isNotNull(),
                            relations_udf(
                                concat_ws(" ", col("related_user"), col("relation"))
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "socials",
                "ips",
                "relations",
                "sex",
                "birth_date",
                "documents",
            )
        )

        df_relations.persist(StorageLevel.DISK_ONLY).count()

        df_chiefs = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0169/raw/chiefs_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("chief_name")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("chief_phone"))))),
            )
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("ips", array())
            .withColumn("works", array())
            .withColumn("socials", array())
            .withColumn(
                "relations",
                when(
                    col("related_user").isNotNull(),
                    array(
                        when(
                            col("related_user").isNotNull(),
                            relations_udf(
                                concat_ws(" ", col("related_user"), col("relation"))
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "socials",
                "ips",
                "relations",
                "sex",
                "birth_date",
                "documents",
            )
        )

        df_chiefs.persist(StorageLevel.DISK_ONLY).count()

        df = df_users.unionAll(df_chiefs).unionAll(df_relations)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    size(array_compact(col("relations"))) > 0,
                    array_compact(col("relations")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
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
