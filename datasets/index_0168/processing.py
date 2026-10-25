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
    flatten,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.financials.udfs import financial_card_number_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0168"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0168/raw/users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .withColumn("emails", email_udf("email"))
            .withColumn("sex", sex_udf("gender"))
            .withColumn("address", address_udf("city_name"))
            .withColumn(
                "Facebook",
                when(
                    col("link").like("https://www.facebook.com/app_scoped_user_id/%"),
                    col("link"),
                ).otherwise(None),
            )
            .withColumn(
                "VK",
                when(col("link").like("https://vk.com/id%"), col("link")).otherwise(
                    None
                ),
            )
            .withColumn(
                "OK",
                when(
                    col("link").like("https://ok.ru/profile/%"), col("link")
                ).otherwise(None),
            )
            .withColumn(
                "Mailru",
                when(
                    col("link").like("http://my.mail.ru/mail/%"), col("link")
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    col("Facebook").isNotNull()
                    | col("VK").isNotNull()
                    | col("OK").isNotNull()
                    | col("Mailru").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Facebook").isNotNull(),
                                struct(
                                    lit("Facebook").alias("title"),
                                    col("Facebook").alias("link"),
                                ),
                            ).otherwise(None),
                            when(
                                col("VK").isNotNull(),
                                struct(
                                    lit("Vk").alias("title"), col("VK").alias("link")
                                ),
                            ).otherwise(None),
                            when(
                                col("OK").isNotNull(),
                                struct(
                                    lit("Ok.ru").alias("title"), col("OK").alias("link")
                                ),
                            ).otherwise(None),
                            when(
                                col("Mailru").isNotNull(),
                                struct(
                                    lit("Mail.ru").alias("title"),
                                    col("Mailru").alias("link"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "user_id", "names", "emails", "address", "birth_date", "sex", "socials"
            )
        )

        df_payment_methods = self.read(
            path="/media/user/SAMSUNG/Databases/index_0168/raw/payment_methods.csv",
            sep=",",
            header=True,
        )

        df_payment_methods = df_payment_methods.withColumn(
            "short_payment_method",
            financial_card_number_udf(col("short_payment_method")),
        ).withColumn(
            "financials",
            when(
                col("short_payment_method").isNotNull()
                & (col("short_payment_method") != ""),
                array_compact(
                    array(
                        when(
                            col("short_payment_method").isNotNull(),
                            struct(
                                lit("Неопределенный банк").alias("title"),
                                col("short_payment_method").alias("card_number"),
                            ),
                        ).otherwise(None)
                    )
                ),
            ).otherwise(None),
        )

        df_payment_methods = (
            df_payment_methods.groupBy("user_id")
            .agg(
                array_compact(
                    array_distinct(flatten(collect_list("financials")))
                ).alias("financials")
            )
            .select("user_id", "financials")
        )

        df_users.show(n=20, truncate=False)
        df_payment_methods.show(n=20, truncate=False)

        df = df_users.join(df_payment_methods, "user_id", "left")

        df = df.select(
            "names", "emails", "address", "birth_date", "sex", "socials", "financials"
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("socials").isNotNull()
                | col("financials").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
