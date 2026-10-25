from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
    collect_set,
    flatten,
    size,
    max,
    lit,
    concat_ws,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.financials.udfs import financial_invoice_number_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0436"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0436/raw/users.csv",
            sep=";",
            header=True,
        )

        df_users = (
            df.withColumn("names", name_udf(col("Имя")))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("Страна"), col("Город"), col("Адрес"))),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "works",
                when(
                    col("Название фирмы").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("Название фирмы"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("Авто").isNotNull() & (col("Авто") != ""))
                    | (col("Вин").isNotNull() & (col("Вин") != "")),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("Авто"),
                            lit(None),
                            lit(None),
                            lit(None),
                            col("Вин"),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("financials", array())
            .withColumn("documents", array())
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "works",
                "financials",
                "vehicles",
                "documents",
                "actuality",
            )
        )

        df_users_with_phone = df_users.filter(col("phones").isNotNull())
        df_users_without_phone = df_users.filter(col("phones").isNull())

        df_users_with_phone = (
            df_users_with_phone.groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("financials"))))
                ).alias("financials"),
                array_compact(
                    array_distinct(flatten(collect_set(col("vehicles"))))
                ).alias("vehicles"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "works",
                "financials",
                "vehicles",
                "documents",
                "actuality",
            )
        )

        df_users_without_phone = (
            df_users_without_phone.withColumn("emails", array(col("emails")))
            .withColumn("address", array(col("address")))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "works",
                "financials",
                "vehicles",
                "documents",
                "actuality",
            )
        )

        df_users = df_users_with_phone.unionAll(df_users_without_phone)

        df_companies = (
            df.filter(col("Название фирмы").isNotNull())
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("emails", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("works", array())
            .withColumn(
                "vehicles",
                when(
                    (col("Авто").isNotNull() & (col("Авто") != ""))
                    | (col("Вин").isNotNull() & (col("Вин") != "")),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("Авто"),
                            lit(None),
                            lit(None),
                            lit(None),
                            col("Вин"),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("КПП").isNotNull(),
                                document_udf(
                                    lit("кпп"),
                                    col("КПП"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("ОГРН").isNotNull(),
                                document_udf(
                                    lit("огрн"),
                                    col("ОГРН"),
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
            .withColumn("invoice_num", financial_invoice_number_udf(col("Р/C")))
            .withColumn(
                "financials",
                when(
                    col("invoice_num").isNotNull(),
                    array(
                        struct(
                            col("Банк").alias("title"),
                            col("invoice_num").alias("card_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "works",
                "financials",
                "vehicles",
                "documents",
                "actuality",
            )
        )

        df_companies = (
            df_companies.groupBy(["names"])
            .agg(
                max(col("phones")).alias("phones"),
                array_compact(array_distinct(collect_set((col("emails"))))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set((col("address"))))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("financials"))))
                ).alias("financials"),
                array_compact(
                    array_distinct(flatten(collect_set(col("vehicles"))))
                ).alias("vehicles"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "works",
                "financials",
                "vehicles",
                "documents",
                "actuality",
            )
        )

        df = df_companies.unionAll(df_users)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                (
                    col("phones").isNotNull()
                    | col("emails").isNotNull()
                    | col("documents").isNotNull()
                )
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
