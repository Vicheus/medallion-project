from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    concat,
    size,
    concat_ws,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.financials.udfs import financial_card_number_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    name_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0111"

    def parser(self):
        df_users_info = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0111/raw/users_info.csv",
                sep=",",
                header=True,
            )
            .withColumn("delivery_address", concat_ws(" ", col("ZIP"), col("ADDRESS")))
            .withColumn("additional_name", col("FIO"))
            .withColumn("additional_phone1", col("USER_PHONE"))
            .withColumn("additional_phone2", col("PHONE"))
            .withColumn("additional_email", col("EMAIL"))
            .withColumn("discount_card_number", col("number_card_dk"))
            .withColumn("bank_card_number", col("CARD_NUMBER"))
            .select(
                "USER_ID",
                "CLIENT_IP",
                "LAT",
                "LON",
                "delivery_address",
                "additional_name",
                "additional_phone1",
                "additional_phone2",
                "additional_email",
                "discount_card_number",
                "bank_card_number",
            )
        )
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0111/raw/users.csv",
            sep=",",
            header=True,
        )

        df = (
            df_users.join(
                df_users_info, df_users["ID"] == df_users_info["USER_ID"], "left"
            )
            .withColumn("ip", ip_address_udf(col("CLIENT_IP")))
            .withColumn(
                "bank_card_number", financial_card_number_udf(col("bank_card_number"))
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            ),
                            name_udf("additional_name"),
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDATE"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_FAX")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("PERSONAL_PAGER")),
                            phone_udf(col("WORK_PHONE")),
                            phone_udf(col("WORK_FAX")),
                            phone_udf(col("WORK_PAGER")),
                            phone_udf(col("additional_phone1")),
                            phone_udf(col("additional_phone2")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("EMAIL")), email_udf(col("additional_email"))
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("PERSONAL_CITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_ZIP"),
                                        when(
                                            col("PERSONAL_STREET").isNotNull(),
                                            concat(lit("ул. "), col("PERSONAL_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            address_udf(col("delivery_address")),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Ортека").alias("title"),
                            lit("https://orteka.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            col("ID").alias("id"),
                            col("discount_card_number").alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_POSITION").isNotNull() | col("WORK_COMPANY").isNotNull(),
                    array(
                        work_udf(
                            col("WORK_POSITION"),
                            lit(None),
                            lit(None),
                            col("WORK_COMPANY"),
                            address_udf(
                                when(
                                    col("WORK_CITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("WORK_CITY"),
                                        col("WORK_ZIP"),
                                        when(
                                            col("WORK_STREET").isNotNull(),
                                            concat(lit("ул. "), col("WORK_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "financials",
                when(
                    col("bank_card_number").isNotNull()
                    & (col("bank_card_number") != ""),
                    array_compact(
                        array(
                            when(
                                col("bank_card_number").isNotNull(),
                                struct(
                                    lit("Неопределенный банк").alias("title"),
                                    col("bank_card_number").alias("card_number"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                when(
                                    col("ip").isNotNull(), struct(col("ip").alias("ip"))
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "coordinates",
                when(
                    (
                        col("LAT").isNotNull()
                        & (col("LAT") != 0.0)
                        & col("LON").isNotNull()
                        & (col("LON") != 0.0)
                    ),
                    array(
                        array((col("LON").cast("double")), col("LAT").cast("double"))
                    ).alias("coordinates"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("LAST_LOGIN"),
                        col("DATE_REGISTER"),
                        col("LAST_ACTIVITY_DATE"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "financials",
                "ips",
                "coordinates",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "coordinates",
                when(size(col("coordinates")) > 0, col("coordinates")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("financials").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "accounts",
            "works",
            "financials",
            "ips",
            "coordinates",
            "actuality",
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
