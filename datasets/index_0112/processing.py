from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    concat,
    size,
    initcap,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0112"

    def parser(self):
        df_clients = self.read(
            path="/media/user/SAMSUNG/Databases/index_0112/raw/Dump_public_level.travel_14.12.2022_bcrypt/clients.csv",
            sep="\t",
            header=True,
        )
        df_tourists = self.read(
            path="/media/user/SAMSUNG/Databases/index_0112/raw/Dump_public_level.travel_14.12.2022_bcrypt/tourists.csv",
            sep="\t",
            header=True,
        )

        df_clients = (
            df_clients.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("middle_name"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "documents",
                array(
                    when(
                        col("passport").isNotNull(),
                        document_udf(
                            lit(None),
                            col("passport"),
                            col("passport_issued_at"),
                            lit(None),
                            col("passport_issued_by"),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() | col("encrypted_password").isNotNull(),
                    array(
                        struct(
                            lit("Level Travel").alias("title"),
                            lit("https://level.travel").alias("link"),
                            col("email").alias("login"),
                            col("encrypted_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("last_sign_in_ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("last_sign_in_ip")).alias("ip"),
                            ip_date_udf(col("last_sign_in_at")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("provider").isNotNull()
                            & (col("provider") != "")
                            & col("uid").isNotNull()
                            & (col("uid") != ""),
                            struct(
                                initcap(col("provider")).alias("title"),
                                col("uid").alias("id"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("last_sign_in_at"),
                        col("created_at"),
                        col("updated_at"),
                        col("confirmed_at"),
                    ),
                    lit("%Y-%m-%dT%H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "socials",
                "ips",
                "accounts",
                "phones",
                "documents",
                "sex",
                "actuality",
            )
        )

        df_clients.show(n=20, truncate=False)

        df_tourists = (
            df_tourists.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("patronymic"))
            )
            .withColumn(
                "sex", sex_udf(when(col("female") == 1, "female").otherwise("male"))
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("passport_number").isNotNull(),
                        document_udf(
                            lit(None),
                            concat(col("passport_prefix"), col("passport_number")),
                            col("passport_issued_on"),
                            col("passport_expires_on"),
                            col("passport_issuer"),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("socials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created_at"), col("updated_at")),
                    lit("%Y-%m-%dT%H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "socials",
                "ips",
                "accounts",
                "phones",
                "documents",
                "sex",
                "actuality",
            )
        )

        df = df_clients.unionAll(df_tourists)

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
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
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
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df = df.select(
            "names",
            "emails",
            "socials",
            "ips",
            "accounts",
            "phones",
            "documents",
            "sex",
            "actuality",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
