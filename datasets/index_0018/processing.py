from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    concat_ws,
    concat,
    coalesce,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.financials.udfs import financial_date_issue_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    email_udf,
    sex_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 10
    dataset_code_name: str = "index_0018"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0018/raw/s_users.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("firstname"), col("lastname"), col("middlename")),
            )
            .withColumn("birth_date", birth_date_udf(col("bday"), lit("%Y-%m-%d")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("login")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("spasp").isNotNull()
                        & (col("spasp") != "")
                        & (col("spasp") != "NULL"),
                        document_udf(
                            lit("паспорт гражданина рф"),
                            col("spasp").alias("serial"),
                            col("dpasp").alias("date_issue"),
                            lit(None).alias("date_expire"),
                            lit(None).alias("authority"),
                            col("cpasp").alias("authority_code"),
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
                    when(
                        col("snils").isNotNull(),
                        document_udf(
                            lit("снилс"),
                            col("snils").alias("serial"),
                            lit(None).alias("date_issue"),
                            lit(None).alias("date_expire"),
                            lit(None).alias("authority"),
                            lit(None).alias("authority_code"),
                        ),
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "address_str",
                address_udf(
                    concat_ws(
                        ", ",
                        when(col("region").isNotNull(), col("region")).otherwise(None),
                        when(col("city").isNotNull(), col("city")).otherwise(None),
                        when(col("street").isNotNull(), col("street")).otherwise(None),
                        when(col("house").isNotNull(), col("house")).otherwise(None),
                        when(
                            col("apartament").isNotNull(),
                            concat(lit("кв. "), col("apartament")),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("address", address_udf(col("address_str")))
            .withColumn(
                "financials",
                array(
                    when(
                        col("card_mask").isNotNull()
                        & (col("card_mask") != "")
                        & (col("card_mask") != "NULL"),
                        struct(
                            coalesce(
                                col("card_bank"), lit("Номер банковской карты")
                            ).alias("title"),
                            col("card_mask").alias("card_number"),
                            financial_date_issue_udf(col("card_exp")).alias(
                                "date_expire"
                            ),
                        ),
                    )
                ),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull(),
                    array(
                        struct(
                            lit("Qzaem").alias("title"),
                            lit("https://qzaem.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                            col("uid").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("tocall"), col("created"), col("activated")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("tocall"),
                    col("tocall"),
                    lit("operator"),
                    col("operator"),
                    lit("monthly_amount"),
                    col("monthly_amount"),
                    lit("total_amount"),
                    col("total_amount"),
                    lit("total_amount_partner"),
                    col("total_amount_partner"),
                    lit("total_amount_zayms"),
                    col("total_amount_zayms"),
                    lit("total_zayms_srv"),
                    col("total_zayms_srv"),
                    lit("total_amount_call"),
                    col("total_amount_call"),
                    lit("send_month_date"),
                    col("send_month_date"),
                    lit("fssp"),
                    col("fssp"),
                    lit("manager"),
                    col("manager"),
                ),
            )
        )

        df = df.select(
            "names",
            "sex",
            "address",
            "phones",
            "emails",
            "birth_date",
            "documents",
            "financials",
            "actuality",
            "raw_metadata",
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("financials").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = (
            df.withColumn(
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

        df.show(n=100, truncate=False)

        df.printSchema()

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
