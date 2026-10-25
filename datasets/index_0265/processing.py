from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    coalesce,
    flatten,
    collect_set,
    first,
    max,
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.financials.udfs import financial_invoice_number_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0265"

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0265/raw/users_preprocessed_1.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone_yandex")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("city")))
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("financials", array())
            .withColumn(
                "data_reg",
                when(
                    col("data_reg") > 0,
                    from_unixtime(col("data_reg"), "yyyy-MM-dd HH:mm:ss"),
                ).otherwise(lit(None)),
            )
            .withColumn(
                "data_login",
                when(
                    col("data_login") > 0,
                    from_unixtime(col("data_login"), "yyyy-MM-dd HH:mm:ss"),
                ).otherwise(lit(None)),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("data_reg"), col("data_login")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "financials",
                "actuality",
            )
        )

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0265/raw/users_preprocessed_2.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("financials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_update_orders"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "financials",
                "actuality",
            )
        )

        df_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0265/raw/users_preprocessed_3.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn(
                "documents",
                array(
                    when(
                        col("document").isNotNull(),
                        document_udf(
                            lit(None),
                            col("document"),
                            col("document_date"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("%d.%m.%Y"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("date_of_birth"), lit("%d.%m.%Y"))
            )
            .withColumn("financials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_accept"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "financials",
                "actuality",
            )
        )

        df_4 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0265/raw/users_preprocessed_4.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn("phones", array())
            .withColumn("invoice_number", financial_invoice_number_udf(col("r_schet")))
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn(
                "documents",
                array(
                    when(
                        col("document").isNotNull(),
                        document_udf(
                            lit(None),
                            col("document"),
                            col("document_date"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("%d.%m.%Y"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("date_of_birth"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "financials",
                when(
                    col("invoice_number").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                coalesce(
                                    col("recipient_bank"), lit("Неопределенный банк")
                                ).alias("title"),
                                col("invoice_number").alias("invoice_number"),
                            )
                        )
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "financials",
                "actuality",
            )
        )

        df_4.show(n=20, truncate=False)

        df_5 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0265/raw/users_preprocessed_5.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn("documents", array())
            .withColumn("birth_date", lit(None))
            .withColumn("financials", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "financials",
                "actuality",
            )
        )

        df = df_1.unionAll(df_2).unionAll(df_3).unionAll(df_4).unionAll(df_5)

        df = df.groupBy(["names"]).agg(
            collect_set("emails").alias("emails"),
            flatten(collect_set("phones")).alias("phones"),
            collect_set("address").alias("address"),
            first("birth_date", ignorenulls=True).alias("birth_date"),
            flatten(collect_set("documents")).alias("documents"),
            flatten(collect_set("financials")).alias("financials"),
            max("actuality").alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
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
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
