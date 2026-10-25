from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    struct,
    array_compact,
    concat,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.financials.udfs import yandex_money_number_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0218"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0218/raw/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "yandex_money_number", yandex_money_number_udf(col("yandex_money"))
            )
            .withColumn(
                "address",
                when(
                    col("city").isNotNull(), concat_ws(", ", col("city"), col("addr"))
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                lit("work5.ru").alias("title"),
                                lit("https://www.work5.ru/").alias("link"),
                                col("email").alias("login"),
                                col("password").alias("password_hash"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "financials",
                when(
                    col("yandex_money_number").isNotNull()
                    | col("webmoney").isNotNull()
                    | col("yoomoney").isNotNull()
                    | col("qiwi").isNotNull(),
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
                                col("webmoney").isNotNull(),
                                struct(
                                    lit("Webmoney").alias("title"),
                                    col("webmoney").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("yoomoney").isNotNull(),
                                struct(
                                    lit("Yoomoney").alias("title"),
                                    col("yoomoney").alias("card_number"),
                                ),
                            ).otherwise(None),
                            when(
                                col("qiwi").isNotNull(),
                                struct(
                                    lit("Qiwi").alias("title"),
                                    col("qiwi").alias("card_number"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "educations",
                when(
                    col("vuz_name1").isNotNull() & (col("vuz_name1") != ""),
                    array_compact(
                        array(
                            education_udf(
                                concat_ws(" ", col("vuz_name1"), col("vuz_fac1")),
                                lit("Высшее"),
                                lit(None),
                                lit(None),
                                when(
                                    col("vuz_year1") != 0,
                                    concat(col("vuz_year1"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "sex",
                "birth_date",
                "ips",
                "educations",
                "accounts",
                "financials",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
            .withColumn(
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
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
