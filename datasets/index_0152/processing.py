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
    max,
    collect_list,
    greatest,
    flatten,
    first,
    coalesce,
)

from parsetron import Parsetron
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
    dataset_code_name: str = "index_0152"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0152/raw/preprocessed/b_user_preprocessed.csv",
            sep=",",
            header=True,
        )
        df_presale_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0152/raw/preprocessed/pre_sale_orders_preprocessed.csv",
            sep=",",
            header=True,
        )
        df_booking_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0152/raw/preprocessed/booking_orders_preprocessed.csv",
            sep=",",
            header=True,
        )

        df_users = (
            df_users.replace("NULL", None)
            .withColumn("user_id", col("ID"))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            ),
                            name_parts_udf(col("NAME"), col("LAST_NAME"), lit(None)),
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
                            phone_udf(col("PHONE2")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("EMAIL")), email_udf(col("EMAIL2")))
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
                            address_udf(
                                when(
                                    col("CITY2").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("CITY2"),
                                        col("POSTCODE2"),
                                        when(
                                            col("STREET2").isNotNull(),
                                            concat(lit("ул. "), col("STREET2")),
                                        ).otherwise(None),
                                        when(
                                            col("BUILDING2").isNotNull(),
                                            concat(lit("д. "), col("BUILDING2")),
                                        ).otherwise(None),
                                        when(
                                            col("APARTMENT2").isNotNull(),
                                            concat(lit("кв. "), col("APARTMENT2")),
                                        ).otherwise(None),
                                    ),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull()
                    & (~col("LOGIN").contains("@example.com"))
                    & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Ekonika").alias("title"),
                            lit("https://ekonika.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            col("ID").alias("id"),
                            when(col("LOYALTY_CARD").isNotNull(), col("LOYALTY_CARD"))
                            .otherwise(None)
                            .alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_POSITION").isNotNull() | col("WORK_COMPANY").isNotNull(),
                    array_compact(
                        array_distinct(
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
                                                    concat(
                                                        lit("ул. "), col("WORK_STREET")
                                                    ),
                                                ).otherwise(None),
                                            ),
                                        )
                                    ),
                                    lit(None),
                                )
                            )
                        )
                    ),
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
                "user_id",
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "actuality",
            )
        )

        df_presale_orders = (
            df_presale_orders.replace("NULL", None)
            .withColumn("user_id", col("UF_USER_ID"))
            .withColumn(
                "names",
                array_compact(array_distinct(array(name_udf(col("UF_FULL_NAME"))))),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("UF_PHONE"))))),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(array(email_udf(col("UF_EMAIL"))))),
            )
            .withColumn("address", array())
            .withColumn("accounts", array())
            .withColumn("works", array())
            .withColumn("actuality", lit(None))
            .select(
                "user_id",
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "actuality",
            )
        )

        df_booking_orders = (
            df_booking_orders.replace("NULL", None)
            .withColumn("user_id", col("UF_USER_ID"))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("UF_LAST_NAME"), col("UF_NAME"), lit(None)
                            )
                        )
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("UF_PHONE"))))),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(array(email_udf(col("UF_EMAIL"))))),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(array((address_udf(col("UF_DELIVERY_ADDRESS")))))
                ),
            )
            .withColumn("accounts", array())
            .withColumn("works", array())
            .withColumn("actuality", lit(None))
            .select(
                "user_id",
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "actuality",
            )
        )

        print(
            f"Presale orders with user id: {df_presale_orders.where(col("user_id").isNotNull()).count()}, without user_id: {df_presale_orders.where(col("user_id").isNull()).count()}"
        )
        print(
            f"booking orders with user id: {df_booking_orders.where(col("user_id").isNotNull()).count()}, without user_id: {df_booking_orders.where(col("user_id").isNull()).count()}"
        )

        df_booking_orders_with_users = df_booking_orders.where(
            col("user_id").isNotNull()
        )
        df_booking_orders_without_users = df_booking_orders.where(
            col("user_id").isNull()
        ).select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "accounts",
            "works",
            "actuality",
        )

        df = df_users.unionAll(df_presale_orders).unionAll(df_booking_orders_with_users)

        df = (
            df.groupBy(["user_id"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(flatten(collect_list("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(flatten(collect_list("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("accounts")))).alias(
                    "accounts"
                ),
                array_compact(array_distinct(flatten(collect_list("works")))).alias(
                    "works"
                ),
                first(coalesce("sex")).alias("sex"),
                first(coalesce("birth_date")).alias("birth_date"),
                max("actuality").alias("actuality"),
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
                "actuality",
            )
        )

        df = df.unionAll(df_booking_orders_without_users)

        df = df.drop_duplicates()

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
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)
        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
