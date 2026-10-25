from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    length,
    concat,
    size,
    coalesce,
    array_distinct,
    concat_ws,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    birth_date_udf,
    name_udf,
    relations_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0147"

    def parser(self):
        df_admins = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0147/raw/preprocessed/admins_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf("cell_phone"))
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("relations", array())
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("financials", array())
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comments"), col("comments"))
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "relations",
                "documents",
                "address",
                "financials",
                "raw_metadata",
            )
        )

        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0147/raw/preprocessed/users_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_users.cache()

        df_users_1 = (
            df_users.replace("\t", " ")
            .withColumn("names", name_udf(col("fio")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf("_mob_tel"))
                    )
                ),
            )
            .withColumn(
                "authority_code", regexp_extract("pasport_grant", r"\d{3}-\d{3}", 0)
            )
            .withColumn(
                "relations",
                when(
                    col("_kontakt2").isNotNull() & (col("_kontakt2") != col("fio")),
                    array(
                        relations_udf(
                            concat_ws(" ", col("_kontakt2"), col("_mob_tel2"))
                        )
                    ),
                ).otherwise(array()),
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
                                    col("authority_code"),
                                    lit("%Y-%m-%d"),
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
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comments"), col("comments"), lit("_obzvon"), col("_obzvon")
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "relations",
                "documents",
                "address",
                "financials",
                "raw_metadata",
            )
        )

        df_users_2 = (
            df_users.where(
                col("_kontakt2").isNotNull()
                & (col("_kontakt2") != col("fio"))
                & (col("_mob_tel2").isNotNull())
            )
            .withColumn("names", name_udf(col("_kontakt2")))
            .withColumn("emails", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("_mob_tel2"))))),
            )
            .withColumn(
                "relations",
                when(
                    col("fio").isNotNull() & (col("_mob_tel").isNotNull()),
                    array(relations_udf(concat_ws(" ", col("fio"), col("_mob_tel")))),
                ).otherwise(array()),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("relations", array())
            .withColumn("documents", array())
            .withColumn("address", array())
            .withColumn("financials", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comments"), col("comments"), lit("_obzvon"), col("_obzvon")
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "relations",
                "documents",
                "address",
                "financials",
                "raw_metadata",
            )
        )

        df_companies = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0147/raw/preprocessed/companies_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", lit(None))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("_mob_tel")), phone_udf(col("_mob_tel2")))
                    )
                ),
            )
            .withColumn("relations", array())
            .withColumn("birth_date", lit(None))
            .withColumn("relations", array())
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
                                    lit("%Y-%m-%d"),
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
                    col("bank_account").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                coalesce(
                                    col("bank_name"), lit("Неопределенный банк")
                                ).alias("title"),
                                col("bank_account").alias("invoice_number"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("bill_id"),
                    col("bill_id"),
                    lit("cor_bank_account"),
                    col("cor_bank_account"),
                    lit("bank_bic"),
                    col("bank_bic"),
                    lit("registration"),
                    col("registration"),
                    lit("credit"),
                    col("credit"),
                    lit("contract_date"),
                    col("contract_date"),
                    lit("representative"),
                    col("representative"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "relations",
                "documents",
                "address",
                "financials",
                "raw_metadata",
            )
        )
        df_companies.cache()

        df = (
            df_admins.unionAll(df_users_1)
            .unionAll(df_users_2)
            .unionAll(df_companies)
            .drop_duplicates()
        )

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
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
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
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
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
            "relations",
            "documents",
            "address",
            "financials",
            "raw_metadata",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
