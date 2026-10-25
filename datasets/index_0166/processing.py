from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0166"

    def parser(self):
        df_mailing = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0166/raw/art-talant.org/art_acymailing_subscriberhomadb.csv",
                sep=",",
                header=True,
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", lit(None))
            .withColumn("ip", ip_address_udf(col("lastopen_ip")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                from_unixtime(
                                    col("lastopen_date"), "yyyy-MM-dd HH:mm:ss"
                                )
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn("educations", array())
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn("address", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "confirmed_date",
                from_unixtime(col("confirmed_date"), "yyyy-MM-dd HH:mm:ss"),
            )
            .withColumn(
                "lastopen_date",
                from_unixtime(col("lastopen_date"), "yyyy-MM-dd HH:mm:ss"),
            )
            .withColumn(
                "lastclick_date",
                from_unixtime(col("lastclick_date"), "yyyy-MM-dd HH:mm:ss"),
            )
            .withColumn(
                "lastsent_date",
                from_unixtime(col("lastsent_date"), "yyyy-MM-dd HH:mm:ss"),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("confirmed_date"),
                        col("lastopen_date"),
                        col("lastclick_date"),
                        col("lastsent_date"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "educations",
                "works",
                "sex",
                "accounts",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_comments = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0166/raw/art-talant.org/art_jcommentshomadb.csv",
                sep=",",
                header=True,
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", lit(None))
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(struct(col("ip").alias("ip"), lit(None).alias("date"))),
                ),
            )
            .withColumn("educations", array())
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn("address", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "educations",
                "works",
                "sex",
                "accounts",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_guestbook = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0166/raw/art-talant.org/art_phocaguestbook_itemshomadb.csv",
                sep=",",
                header=True,
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("names", name_udf(col("username")))
            .withColumn("phones", lit(None))
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(struct(col("ip").alias("ip"), lit(None).alias("date"))),
                ),
            )
            .withColumn("educations", array())
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn("address", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("title"), col("title"), lit("content"), col("content")
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "educations",
                "works",
                "sex",
                "accounts",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_works = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0166/raw/art-talant.org/art_publish_workshomadb.csv",
                sep=",",
                header=True,
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("names", name_udf(col("pupil")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("ips", array())
            .withColumn(
                "educations",
                when(
                    col("school").isNotNull() & (col("school") != ""),
                    array_compact(
                        array(
                            education_udf(
                                col("school"),
                                lit("Среднее"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn("sex", lit(None))
            .withColumn("address", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("name"), col("name"), lit("description"), col("description")
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "educations",
                "works",
                "sex",
                "accounts",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0166/raw/art-talant.org/art_usershomadb.csv",
                sep=",",
                header=True,
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", lit(None))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("address", address_udf(col("city")))
            .withColumn("ips", array())
            .withColumn("educations", array())
            .withColumn(
                "works",
                when(
                    col("workplace").isNotNull() & (col("workplace") != ""),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("workplace").alias("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("арт-талант").alias("title"),
                            lit("https://art-talant.org/").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "educations",
                "works",
                "sex",
                "accounts",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df = (
            df_comments.unionAll(df_guestbook)
            .unionAll(df_mailing)
            .unionAll(df_works)
            .unionAll(df_users)
        )
        df = df.drop_duplicates(["names", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
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
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "ips",
            "educations",
            "works",
            "sex",
            "accounts",
            "address",
            "actuality",
            "raw_metadata",
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
