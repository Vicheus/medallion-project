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
    coalesce,
    array_distinct,
    concat_ws,
    length,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.financials.udfs import financial_invoice_number_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    birth_date_udf,
    name_udf,
    address_udf,
    name_parts_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0148"

    def parser(self):
        df_admins = (
            self.read(
                path="/home/user/Documents/data/index_0148/raw/admins_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf("cell_phone"))
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("financials", array())
            .withColumn(
                "socials",
                when(
                    col("telegram_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("telegram_id").isNotNull(),
                                social_udf(
                                    lit("Telegram"),
                                    col("telegram_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "documents",
                "address",
                "financials",
                "socials",
            )
        )

        df_users = (
            self.read(
                path="/home/user/Documents/data/index_0148/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf("phone2"),
                            phone_udf("cell_phone"),
                        )
                    )
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("telegram_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("telegram_id").isNotNull(),
                                social_udf(
                                    lit("Telegram"),
                                    col("telegram_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    col("pasport_num").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("pasport_num").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("pasport_num"),
                                    col("pasport_date"),
                                    lit(None),
                                    col("pasport_grant"),
                                    lit(None),
                                    lit("%Y-%M-%d"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("city").isNotNull()
                                    & (length(col("address_street")) > 3),
                                    concat_ws(
                                        ", ",
                                        col("zip"),
                                        col("city"),
                                        when(
                                            col("address_street").isNotNull(),
                                            concat(lit("ул. "), col("address_street")),
                                        ).otherwise(None),
                                        when(
                                            col("address_build").isNotNull(),
                                            concat(lit("д. "), col("address_build")),
                                        ).otherwise(None),
                                        when(
                                            col("address_flat").isNotNull(),
                                            concat(lit("кв. "), col("address_flat")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            address_udf(col("reg_address")),
                        )
                    )
                ),
            )
            .withColumn("financials", array())
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "documents",
                "address",
                "financials",
                "socials",
            )
        )

        df_users.cache()

        df_companies = (
            self.read(
                path="/home/user/Documents/data/index_0148/raw/companies_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", lit(None))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("relations", array())
            .withColumn("birth_date", lit(None))
            .withColumn(
                "invoice_number", financial_invoice_number_udf(col("bank_account"))
            )
            .withColumn("socials", array())
            .withColumn(
                "documents",
                when(
                    col("tax_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("tax_number").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("tax_number"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%M-%d"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("address", array(address_udf(col("address"))))
            .withColumn(
                "financials",
                when(
                    col("invoice_number").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                coalesce(
                                    col("bank_name"), lit("Неопределенный банк")
                                ).alias("title"),
                                col("invoice_number").alias("invoice_number"),
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "documents",
                "address",
                "financials",
                "socials",
            )
        )
        df_companies.cache()

        df = df_admins.unionAll(df_users).unionAll(df_companies).drop_duplicates()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
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
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
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
            "phones",
            "birth_date",
            "documents",
            "address",
            "financials",
            "socials",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
