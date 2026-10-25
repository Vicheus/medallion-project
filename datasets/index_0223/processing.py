from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    regexp_extract,
    coalesce,
    flatten,
    collect_set,
    greatest,
    max,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0223"

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0223/raw/gazprom.ru - @bereza_bd/20к_phones_FIO_emails.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col(("client_name"))))
            .withColumn(
                "emails",
                array_compact(array_distinct(array(email_udf(col(("client_email")))))),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col(("client_phone")))))),
            )
            .withColumn("works", array())
            .withColumn("actuality", lit(None))
            .select("names", "emails", "phones", "works", "actuality")
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0223/raw/gazprom.ru - @bereza_bd/100к_FIO_emails_positions.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col(("title"))))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("login")), email_udf(col("email")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("city_phone")),
                            phone_udf(col("home_phone")),
                            phone_udf(col("internal_phone")),
                            phone_udf(col("mobile_phone")),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("post").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                col("post"),
                                lit(None),
                                lit(None),
                                coalesce(
                                    regexp_extract(
                                        "dn", r"(?:.*?OU=[^,]+,){1}OU=([^,]+)", 1
                                    ),
                                    lit("ПАО «Газпром»"),
                                ),
                                address_udf(col("room")),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .select("names", "emails", "phones", "works", "actuality")
        )

        df_users_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0223/raw/gazprom.ru - @bereza_bd/100к_FIO_places.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col(("title"))))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("login")), email_udf(col("email")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("city_phone")),
                            phone_udf(col("home_phone")),
                            phone_udf(col("internal_phone")),
                            phone_udf(col("mobile_phone")),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("post").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                col("post"),
                                lit(None),
                                lit(None),
                                coalesce(
                                    regexp_extract(
                                        "dn", r"(?:.*?OU=[^,]+,){1}OU=([^,]+)", 1
                                    ),
                                    lit("ПАО «Газпром»"),
                                ),
                                address_udf(col("room")),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("creation_date"),
                        col("last_modified_date"),
                        col("lastlogindate"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
            .select("names", "emails", "phones", "works", "actuality")
        )

        df = df_users_1.unionAll(df_users_2).unionAll(df_users_3)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["names", "phones"]).agg(
            array_compact(flatten(collect_set(col("emails")))).alias("emails"),
            array_compact(flatten(collect_set(col("works")))).alias("works"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("works").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
