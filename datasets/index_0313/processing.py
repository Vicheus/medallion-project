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
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.financials.udfs import yandex_money_number_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0313"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0313/raw/Telderi_clean.csv",
                sep="\t",
                header=True,
            )
            .replace("\Z", "")
            .filter(col("user_country") != "ua")
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("user_name")), name_udf(col("real_name")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("user_email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("user_phone")),
                            phone_udf(col("new_user_phone")),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("user_last_visit"), col("user_reg_date")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("skype_num").isNotNull(),
                            social_udf(
                                lit("Skype"), col("skype_num"), lit(None), lit(None)
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("user_name").isNotNull() & col("user_password").isNotNull(),
                    array(
                        struct(
                            lit("Telderi").alias("title"),
                            lit("https://www.telderi.ru").alias("link"),
                            col("user_name").alias("login"),
                            col("user_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "yandex_money_number",
                yandex_money_number_udf(col("back_yd_account_id")),
            )
            .withColumn(
                "financials",
                when(
                    col("yandex_money_number").isNotNull()
                    | col("back_webmoney_wmid").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("yandex_money_number").isNotNull(),
                                struct(
                                    lit("Яндекс деньги").alias("title"),
                                    col("yandex_money_number").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("back_webmoney_wmid").isNotNull(),
                                struct(
                                    lit("Webmoney").alias("title"),
                                    col("back_webmoney_wmid").alias("card_number"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("back_user_wmr"),
                    col("back_user_wmr"),
                    lit("back_user_wmz"),
                    col("back_user_wmz"),
                    lit("description"),
                    col("description"),
                    lit("back_card_number"),
                    col("back_card_number"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "socials",
                "financials",
                "accounts",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
