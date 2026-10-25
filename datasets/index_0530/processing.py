from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    name_udf,
    phone_udf,
    email_udf,
    raw_metadata_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.settings import DATASET_COUNTRY_CODE

from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    max,
    lit,
    struct,
    array,
    array_distinct,
    first,
    array_compact,
    size,
    concat_ws,
    collect_set,
    flatten,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0530"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    validate_invalid_groupping: bool = True

    def parser(self):

        df_bank_accounts = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0530/raw/quanat_data/mfo_bank_accounts.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("accounts_11375")))
            .withColumn(
                "invoice_number",
                when(col("code").startswith("KZ"), col("code")).otherwise(None),
            )
            .withColumn(
                "card_number",
                when(~col("code").startswith("KZ"), col("code")).otherwise(None),
            )
            .withColumn(
                "phones",
                array(phone_udf(col("users_11396"), lit(self.dataset_country_code))),
            )
            .withColumn(
                "financials",
                when(
                    col("code").isNotNull(),
                    array(
                        struct(
                            col("crm_banks_11376").alias("title"),
                            col("card_number").alias("card_number"),
                            col("invoice_number").alias("invoice_number"),
                            lit(None).alias("date_issue"),
                            lit(None).alias("date_expire"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("account_id", col("user_id"))
            .withColumn("children", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("ips", array())
            .withColumn("devices", array())
            .withColumn("works", array())
            .withColumn("documents", array())
            .select(
                "account_id",
                "names",
                "birth_date",
                "children",
                "sex",
                "emails",
                "phones",
                "address",
                "ips",
                "devices",
                "works",
                "documents",
                "raw_metadata",
                "actuality",
                "financials",
            )
        )

        df_client_users = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0530/raw/quanat_data/mfo_client_users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn(
                "phones",
                array(phone_udf(col("mobile"), lit(self.dataset_country_code))),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("account_id", col("id"))
            .withColumn("children", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("address", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("ips", array())
            .withColumn("devices", array())
            .withColumn("works", array())
            .withColumn("documents", array())
            .withColumn("financials", array())
            .select(
                "account_id",
                "names",
                "birth_date",
                "children",
                "sex",
                "emails",
                "phones",
                "address",
                "ips",
                "devices",
                "works",
                "documents",
                "raw_metadata",
                "actuality",
                "financials",
            )
        )

        df_mfo_reqs = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0530/raw/quanat_data/mfo_reqs.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("children", when(col("children") > 0, True).otherwise(False))
            .withColumn(
                "actuality", actuality_date_udf(col("created_at"), lit("%Y-%m-%d"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "works",
                when(
                    col("employer_name").isNotNull(),
                    array(
                        work_udf(
                            col("employer_name"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn(
                "documents",
                when(
                    col("iin").isNotNull() | col("idcard").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("iin").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("iin"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(self.dataset_country_code),
                                ),
                            ).otherwise(None),
                            when(
                                col("idcard").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рк"),
                                    col("idcard"),
                                    col("idcard_beg"),
                                    col("idcard_exp"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                    lit(self.dataset_country_code),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("ip", ip_address_udf(col("ip_address")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            lit(None).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn("sex", sex_udf(col("mfo_sexs_10120")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(col("work_phone"), col("mobile")))),
            )
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array(
                        struct(
                            lit("Оформление кредита").alias("action"),
                            col("user_agent").alias("user_agent"),
                            device_date_udf(
                                col("created_at"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        lit("ул."),
                        col("fact_street"),
                        lit("д."),
                        col("fact_street_house"),
                        lit("кв."),
                        col("fact_street_flat"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("mfo_status_rejects_10379"),
                    col("mfo_status_rejects_10379"),
                    lit("mfo_position_types_10155"),
                    col("mfo_position_types_10155"),
                    lit("mfo_monthly_incexp_10168"),
                    col("mfo_monthly_incexp_10168"),
                    lit("mfo_monthly_incexp_10425"),
                    col("mfo_monthly_incexp_10425"),
                    lit("mfo_edu_levels_10327"),
                    col("mfo_edu_levels_10327"),
                    lit("mfo_activity_types_10140"),
                    col("mfo_activity_types_10140"),
                ),
            )
            .withColumn("financials", array())
            .select(
                "account_id",
                "names",
                "birth_date",
                "children",
                "sex",
                "emails",
                "phones",
                "address",
                "ips",
                "devices",
                "works",
                "documents",
                "raw_metadata",
                "actuality",
                "financials",
            )
        )

        df = df_mfo_reqs.unionAll(df_bank_accounts).unionAll(df_client_users)

        df = (
            df.groupBy("account_id")
            .agg(
                array_compact(array_distinct(collect_set(col("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                first(col("names"), ignorenulls=True).alias("names"),
                first(col("children"), ignorenulls=True).alias("children"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                max(col("birth_date")).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
                array_compact(
                    array_distinct(flatten(collect_set(col("financials"))))
                ).alias("financials"),
                array_compact(array_distinct(flatten(collect_set(col("ips"))))).alias(
                    "ips"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("devices"))))
                ).alias("devices"),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
            )
            .select(
                "names",
                "birth_date",
                "children",
                "sex",
                "emails",
                "phones",
                "address",
                "ips",
                "devices",
                "works",
                "documents",
                "raw_metadata",
                "actuality",
                "financials",
            )
        )

        df = df.filter(col("names") != "Турехан Улжан Абдыбеккызы")
        df.drop_duplicates(["names"])
        df = df.cache()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(
                    size(array_compact(array_distinct(col("address")))) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(array_distinct(col("emails")))) > 0,
                    array_compact(array_distinct(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(array_distinct(col("documents")))) > 0,
                    array_compact(array_distinct(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(array_distinct(col("works")))) > 0,
                    array_compact(array_distinct(col("works"))),
                ).otherwise(None),
            )
            .withColumn(
                "devices",
                when(
                    size(array_compact(array_distinct(col("devices")))) > 0,
                    array_compact(array_distinct(col("devices"))),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(array_distinct(col("ips")))) > 0,
                    array_compact(array_distinct(col("ips"))),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(array_distinct(col("raw_metadata")))) > 0,
                    array_compact(array_distinct(col("raw_metadata"))),
                ).otherwise(None),
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
