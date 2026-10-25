from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    split,
    size,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.financials.udfs import yandex_money_number_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phones_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0134"

    def parser(self):
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0134/raw/BigSMM.ru - @StormInDatBase/users_info_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn(
                "phones",
                phones_udf(array_distinct(array_compact(split(col("phones"), ",")))),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "yandex_money_number_1", yandex_money_number_udf(col("yandex1"))
            )
            .withColumn(
                "yandex_money_number_2", yandex_money_number_udf(col("yandex2"))
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() | col("pass").isNotNull(),
                    array(
                        struct(
                            lit("BigSMM").alias("title"),
                            lit("https://bigsmm.ru").alias("link"),
                            col("login").alias("login"),
                            col("pass").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("last_activity_date"), lit("yyyy-MM-dd HH:mm:ss")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "financials",
                when(
                    col("yandex_money_number_1").isNotNull()
                    | col("yandex_money_number_2").isNotNull()
                    | col("qiwi1").isNotNull()
                    | col("qiwi2").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("yandex_money_number_1").isNotNull(),
                                struct(
                                    lit("Яндекс деньги").alias("title"),
                                    col("yandex_money_number_1").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("yandex_money_number_2").isNotNull(),
                                struct(
                                    lit("Яндекс деньги").alias("title"),
                                    col("yandex_money_number_2").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("qiwi1").isNotNull(),
                                struct(
                                    lit("Qiwi").alias("title"),
                                    col("qiwi1").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("qiwi2").isNotNull(),
                                struct(
                                    lit("Qiwi").alias("title"),
                                    col("qiwi2").alias("card_number"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_activity_date"), lit("%Y-%m-%d")),
            )
            .select(
                "names",
                "emails",
                "financials",
                "ips",
                "accounts",
                "phones",
                "actuality",
            )
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
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names", "emails", "financials", "ips", "accounts", "phones", "actuality"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
