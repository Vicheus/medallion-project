from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    struct,
    concat_ws,
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    birth_date_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    sex_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0133"

    def parser(self):
        df_1 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0133/raw/@StormInDataBase/B Users.csv",
            sep=";",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0133/raw/@StormInDataBase/MDL Users.csv",
            sep=";",
            header=True,
        )
        df_3 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0133/raw/@StormInDataBase/users_info_preprocessed.csv",
            sep=";",
            header=True,
        )

        df_1 = (
            df_1.replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("PERSONAL_PROFESSION").isNotNull()
                    | col("WORK_COMPANY").isNotNull(),
                    array(
                        work_udf(
                            when(
                                col("PERSONAL_PROFESSION") != col("WORK_COMPANY"),
                                col("PERSONAL_PROFESSION"),
                            ).otherwise(None),
                            lit(None),
                            lit(None),
                            col("WORK_COMPANY"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Волгоградский медицинский университет").alias("title"),
                            lit("https://www.volgmed.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn("address", lit(None))
            .withColumn("educations", array())
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("LAST_LOGIN"), col("DATE_REGISTER")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "accounts",
                "works",
                "ips",
                "socials",
                "address",
                "educations",
                "documents",
                "birth_date",
                "sex",
                "actuality",
            )
        )

        df_2 = (
            df_2.replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("firstname"), col("lastname"), col("middlename")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(" ", col("country"), col("city"), col("address"))
                ),
            )
            .withColumn("ip_address", ip_address_udf(col("lastip")))
            .withColumn("works", array())
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Волгоградский медицинский университет").alias("title"),
                            lit("https://www.volgmed.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                from_unixtime(col("lastlogin"), "yyyy-MM-dd HH:mm:ss")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("skype").isNotNull() | col("skype").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("skype").isNotNull() | col("skype").isNotNull(),
                                social_udf(
                                    lit("Facebook"), col("skype"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("educations", array())
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        from_unixtime(col("timecreated")),
                        lit("%Y-%m-%d %H:%M:%S"),
                        from_unixtime(col("timemodified")),
                        lit("%Y-%m-%d %H:%M:%S"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "accounts",
                "works",
                "ips",
                "socials",
                "address",
                "educations",
                "documents",
                "birth_date",
                "sex",
                "actuality",
            )
        )

        df_3 = (
            df_3.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("uname"), lit(None), col("uotchestvo"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("date_birth"), lit("%Y-%m-%d"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("main_phone")),
                            phone_udf(col("add_phone")),
                            phone_udf(col("addition_phone")),
                            phone_udf(col("home_phone")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("address2")))
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn(
                "educations",
                when(
                    col("education_place_name").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                col("education_place_name"),
                                lit(None),
                                lit(None),
                                lit(None),
                                col("education_end_date"),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                array(
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
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "accounts",
                "works",
                "ips",
                "socials",
                "address",
                "educations",
                "documents",
                "birth_date",
                "sex",
                "actuality",
            )
        )

        df = df_1.unionAll(df_2).unionAll(df_3)

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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
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
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
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
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
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

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "accounts",
            "works",
            "ips",
            "socials",
            "address",
            "educations",
            "documents",
            "birth_date",
            "sex",
            "actuality",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
