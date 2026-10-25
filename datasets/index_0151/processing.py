from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat,
    struct,
    collect_set,
    split,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    name_udf,
    phones_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0151"

    def parser(self):
        df_platex = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0151/raw/platex_preprocessed.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("C_NAME")))))
            )
            .withColumn("phones", phones_udf(split(col("W_PHONE"), ";")))
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("emails", lit(None))
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("address", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "documents",
                "accounts",
                "address",
                "ips",
                "actuality",
            )
        )

        df_forum_members = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0151/raw/obltelecom_forum_members_preprocessed.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                array_compact(array_distinct(array(name_udf(col("real_name"))))),
            )
            .withColumn("emails", email_udf(col("email_address")))
            .withColumn(
                "date_registered",
                from_unixtime(col("date_registered"), "yyyy-MM-dd HH:mm:ss"),
            )
            .withColumn(
                "accounts",
                when(
                    col("member_name").isNotNull() & col("passwd").isNotNull(),
                    array(
                        struct(
                            lit("Облтелеком").alias("title"),
                            lit("https://obltelecom.ru").alias("link"),
                            col("member_name").alias("login"),
                            col("passwd").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("member_ip").isNotNull() | col("member_ip2").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(ip_address_udf(col("member_ip")).alias("ip")),
                                struct(ip_address_udf(col("member_ip2")).alias("ip")),
                            )
                        )
                    ),
                ),
            )
            .withColumn("phones", array())
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("address", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_registered"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "documents",
                "accounts",
                "address",
                "ips",
                "actuality",
            )
        )

        df_billing_accounts = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0151/raw/billing_accounts_preprocessed.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("name")),
                            name_parts_udf(
                                col("abonent_surname"),
                                col("abonent_name"),
                                col("abonent_patronymic"),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("fax")),
                            phone_udf(col("mobile")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthdate")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("passport_series").isNotNull()
                                & (col("passport_series") != "")
                                & col("passport_number").isNotNull()
                                & (col("passport_number") != ""),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("passport_series"), col("passport_number")
                                    ).alias("serial"),
                                    col("passport_issuedate").alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    concat(
                                        col("passport_issuedepartment"),
                                        col("passport_issueplace"),
                                    ).alias("authority"),
                                    lit(None).alias("authority_code"),
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
                            lit("Облтелеком").alias("title"),
                            lit("https://obltelecom.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn("ips", array())
            .withColumn("actuality", lit(None))
            .select(
                "account_id",
                "names",
                "phones",
                "emails",
                "birth_date",
                "documents",
                "accounts",
                "ips",
                "actuality",
            )
        )

        df_billing_accounts_addr = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0151/raw/billing_accounts_addr_preprocessed.csv",
                sep=",",
                header=True,
            )
            .groupBy("account_id")
            .agg(collect_set("address").alias("address"))
        )

        df_accounts = df_billing_accounts.join(
            df_billing_accounts_addr, "account_id", "left"
        ).select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "documents",
            "accounts",
            "address",
            "ips",
            "actuality",
        )

        df = df_accounts.unionAll(df_platex).unionAll(df_forum_members)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
