from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    array_distinct,
    from_json,
    transform,
    regexp_replace,
    size,
)
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    phones_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0084"

    def parser(self):
        df_b_users = self.read(
            path="ock/osk_b_users_preprocessed.csv", sep=";", header=True
        )
        df_b_users = (
            df_b_users.drop_duplicates(["name", "email", "login"])
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", array(email_udf(col("email"))))
            .withColumn("phones", array(phone_udf(col("mobile_phone"))))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Объединённая страховая компания (ОСК)").alias("title"),
                            lit("https://www.osk-ins.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("address", array())
            .withColumn("documents", array())
            .withColumn("works", array())
            .withColumn("ips", array())
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "works",
                "accounts",
                "ips",
            )
        )

        telephone_schema = ArrayType(
            StructType(
                [
                    StructField("TelephoneType", StringType(), True),
                    StructField("TelephonePresentation", StringType(), True),
                    StructField("Number", StringType(), True),
                ]
            )
        )
        df_drafts = self.read(
            path="ock/osk_drafts_preprocessed.csv", sep=";", header=True
        )
        df_drafts = (
            df_drafts.withColumn("names", name_udf(col("full_name")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("fact_address")),
                            address_udf(col("juridical_address")),
                        )
                    )
                ),
            )
            .withColumn(
                "telephones",
                from_json(
                    regexp_replace(col("telephones"), '""', '"'), telephone_schema
                ),
            )
            .withColumn(
                "telephones",
                transform(col("telephones"), lambda x: x["TelephonePresentation"]),
            )
            .withColumn("phones", phones_udf(col("telephones")))
            .withColumn("emails", array(email_udf("email")))
            .withColumn(
                "documents",
                when(
                    col("passport_number").isNotNull() | col("inn").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_number").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("passport_number"),
                                    col("passport_date_of_issue"),
                                    lit(None),
                                    col("passport_gived_out"),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("work_place").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                lit(None),
                                lit(None),
                                col("work_place"),
                                lit(None),
                            ),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "works",
                "accounts",
                "ips",
            )
        )

        df_zay_base = self.read(
            path="ock/osk_zay_base_preprocessed.csv", sep=";", header=True
        )
        df_zay_base = (
            df_zay_base.drop_duplicates(["full_name", "email", "phone"])
            .withColumn("names", name_udf(col("full_name")))
            .withColumn("emails", array(email_udf(col("email"))))
            .withColumn("phones", array(phone_udf(col("phone"))))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("region"))))),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            ip_date_udf(col("date")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("documents", array())
            .withColumn("works", array())
            .withColumn("accounts", array())
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "works",
                "accounts",
                "ips",
            )
        )

        df_zay_users = self.read(
            path="ock/osk_zay_users_preprocessed.csv", sep=";", header=True
        )
        df_zay_users = (
            df_zay_users.drop_duplicates(["email", "password", "name", "phone"])
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", array(email_udf(col("email"))))
            .withColumn("phones", array(phone_udf(col("phone"))))
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Объединённая страховая компания (ОСК)").alias("title"),
                            lit("https://www.osk-ins.ru").alias("link"),
                            col("email").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("address", array())
            .withColumn("documents", array())
            .withColumn("works", array())
            .withColumn("ips", array())
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "works",
                "accounts",
                "ips",
            )
        )

        df = (
            df_zay_users.unionAll(df_b_users)
            .unionAll(df_drafts)
            .unionAll(df_zay_base)
            .withColumn("phones", array_distinct(array_compact(col("phones"))))
            .withColumn("emails", array_distinct(array_compact(col("emails"))))
            .withColumn("documents", array_distinct(array_compact(col("documents"))))
            .withColumn("works", array_distinct(array_compact(col("works"))))
            .withColumn("accounts", array_distinct(array_compact(col("accounts"))))
            .withColumn("ips", array_distinct(array_compact(col("ips"))))
            .withColumn("address", array_distinct(array_compact(col("address"))))
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
