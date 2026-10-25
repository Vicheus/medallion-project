from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    array_compact,
    array_distinct,
    array,
    expr,
    flatten,
    collect_list,
    collect_set,
    first,
    max,
    struct,
    coalesce,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    raw_metadata_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
    actuality_date_udf,
)
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0464"
    validate_invalid_groupping: bool = True

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0464/raw/MixZipUTF8_08.05.2024/preprocessed/users.csv",
            sep=";",
            header=True,
        )
        df_companies = self.read(
            path="/media/user/SAMSUNG/Databases/index_0464/raw/MixZipUTF8_08.05.2024/preprocessed/companies.csv",
            sep=";",
            header=True,
        )

        df_users = (
            df_users.withColumn(
                "names",
                array_distinct(
                    array_compact(array(name_udf(col("name2")), name_udf(col("name"))))
                ),
            )
            .withColumn(
                "emails",
                when(
                    email_udf(col("login")).isNotNull(), email_udf(col("login"))
                ).otherwise(email_udf(col("mail"))),
            )
            .withColumn("phones", phone_udf(col("tel2")))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("adres"))))),
            )
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("dop_info"), col("dop_info"))
            )
            .withColumn(
                "actuality", actuality_date_udf(col("created_at"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "works",
                when(
                    (col("company").isNotNull() | col("company2").isNotNull()),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            coalesce(col("company"), col("company2")),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("documents", array())
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("MIXZIP: Магазин запчастей для бытовой техники").alias(
                                "title"
                            ),
                            lit("https://mixzip.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "works",
                "documents",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_users.show(n=10)

        df_users_with_email = (
            df_users.filter(col("emails").isNotNull() & (col("emails") != ""))
            .groupBy(["emails", "names"])
            .agg(
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("works"))).alias("works"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                array_distinct(flatten(collect_list("accounts"))).alias("accounts"),
                collect_set("phones").alias("phones"),
                collect_set("raw_metadata").alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "works",
                "documents",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_users_without_email = (
            df_users.filter(col("emails").isNull() | (col("emails") == ""))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "works",
                "documents",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_users = df_users_with_email.unionAll(df_users_without_email)

        df_users.show(n=20)

        df_companies = (
            df_companies.withColumn(
                "names", array_distinct(array_compact(array(name_udf(col("org_name")))))
            )
            .withColumn("emails", lit(None))
            .withColumn("phones", lit(None))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("org_yur_adres")),
                            address_udf(col("org_fakt_adres")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("org_ras"),
                    col("org_ras"),
                    lit("org_kor"),
                    col("org_kor"),
                    lit("org_bik"),
                    col("org_bik"),
                    lit("org_bank"),
                    col("org_bank"),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("created_at"), lit("%Y-%m-%d"))
            )
            .withColumn("works", array())
            .withColumn("accounts", array())
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("org_inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("org_inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("org_kpp").isNotNull(),
                                document_udf(
                                    lit("кпп"),
                                    col("org_kpp"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "works",
                "documents",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies_with_phones = df_companies.filter(
            col("phones").isNotNull() & (col("phones") != "")
        )

        df_companies_without_phones = df_companies.filter(
            col("phones").isNull() | (col("phones") == "")
        )

        df_companies_without_phones = (
            df_companies_without_phones.withColumn(
                "phones", array_distinct(array_compact(array(name_udf(col("phones")))))
            )
            .withColumn(
                "emails", array_distinct(array_compact(array(name_udf(col("emails")))))
            )
            .withColumn(
                "raw_metadata",
                array_distinct(array_compact(array(name_udf(col("raw_metadata"))))),
            )
        )

        df_companies_with_phones = (
            df_companies_with_phones.groupBy(["names", "phones"])
            .agg(
                array_distinct(flatten(collect_list("address"))).alias("address"),
                array_distinct(flatten(collect_list("works"))).alias("works"),
                array_distinct(flatten(collect_list("documents"))).alias("documents"),
                array_distinct(flatten(collect_list("accounts"))).alias("accounts"),
                collect_set("emails").alias("emails"),
                collect_set("raw_metadata").alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .withColumn(
                "phones", array_distinct(array_compact(array(name_udf(col("phones")))))
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "works",
                "documents",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies = df_companies_with_phones.unionAll(df_companies_without_phones)

        df = df_users.unionAll(df_companies)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
            .withColumn("phones", expr("slice(phones, 1, 5)"))
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("address").isNotNull()
                | col("documents").isNotNull()
            )
        )

        email_counts = df.groupBy("emails").count()
        duplicate_emails = email_counts.filter(col("count") > 1).select("emails")
        df_duplicates = df.join(duplicate_emails, on="emails", how="inner")
        df_cleaned = df_duplicates.withColumn("emails", array()).withColumn(
            "accounts", array()
        )
        df_non_duplicates = df.join(duplicate_emails, on="emails", how="left_anti")
        df = df_non_duplicates.unionByName(df_cleaned)

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
