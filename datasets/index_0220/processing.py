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
    first,
    concat_ws,
    trim,
    concat,
    flatten,
    collect_set,
)
from pyspark.sql.types import StructType, StringType, IntegerType

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0220"

    def parser(self):
        cards_schema = (
            StructType()
            .add("id", StringType(), True)
            .add("unknown_field_1", StringType(), True)
            .add("name", StringType(), True)
            .add("unknown_field_2", StringType(), True)
            .add("unknown_field_3", StringType(), True)
            .add("unknown_field_4", StringType(), True)
            .add("unknown_field_5", StringType(), True)
            .add("unknown_field_6", StringType(), True)
            .add("unknown_field_7", StringType(), True)
            .add("unknown_field_8", StringType(), True)
            .add("unknown_field_9", StringType(), True)
            .add("email", StringType(), True)
            .add("unknown_field_10", StringType(), True)
            .add("unknown_field_11", StringType(), True)
            .add("unknown_field_12", StringType(), True)
            .add("unknown_field_13", StringType(), True)
            .add("unknown_field_14", StringType(), True)
            .add("card_type", StringType(), True)
            .add("unknown_field_15", StringType(), True)
            .add("card_number", StringType(), True)
            .add("unknown_field_16", StringType(), True)
            .add("unknown_field_17", StringType(), True)
            .add("unknown_field_18", StringType(), True)
            .add("unknown_field_19", StringType(), True)
            .add("unknown_field_20", StringType(), True)
            .add("unknown_field_21", StringType(), True)
            .add("unknown_field_22", StringType(), True)
            .add("phone", StringType(), True)
            .add("unknown_field_23", StringType(), True)
            .add("unknown_field_24", StringType(), True)
            .add("unknown_field_25", StringType(), True)
            .add("unknown_field_26", StringType(), True)
            .add("unknown_field_27", StringType(), True)
            .add("unknown_field_28", StringType(), True)
            .add("unknown_field_29", StringType(), True)
            .add("unknown_field_30", StringType(), True)
            .add("unknown_field_31", StringType(), True)
            .add("unknown_field_32", StringType(), True)
            .add("unknown_field_33", StringType(), True)
            .add("unknown_field_34", StringType(), True)
            .add("unknown_field_35", StringType(), True)
            .add("unknown_field_36", StringType(), True)
            .add("unknown_field_37", StringType(), True)
            .add("unknown_field_38", StringType(), True)
            .add("unknown_field_39", StringType(), True)
            .add("unknown_field_40", StringType(), True)
            .add("unknown_field_41", StringType(), True)
            .add("unknown_field_42", StringType(), True)
            .add("unknown_field_43", StringType(), True)
        )

        df_cards = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0220/raw/vashdom24.ru/b_kartyloyalnostirequests.txt",
                sep=",",
                header=False,
                schema=cards_schema,
            )
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "accounts",
                when(
                    col("card_number").isNotNull(),
                    array(
                        struct(
                            lit("Карта лояльности Vashdom24").alias("title"),
                            lit("https://vashdom24.by").alias("link"),
                            lit(None).alias("login"),
                            lit(None).alias("password_hash"),
                            col("card_number").alias("client_card_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("address", array())
            .withColumn("ips", array())
            .withColumn("works", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "accounts",
                "ips",
                "works",
            )
        )

        order_props_schema = (
            StructType()
            .add("unknown_field_1", IntegerType(), True)
            .add("order_id", IntegerType(), True)
            .add("unknown_field_3", IntegerType(), True)
            .add("field_type_name", StringType(), True)
            .add("field_value", StringType(), True)
            .add("field_code", StringType(), True)
            .add("unknown_field_4", StringType(), True)
            .add("unknown_field_5", StringType(), True)
            .add("unknown_field_6", StringType(), True)
        )
        df_order_props = self.read(
            path="/media/user/SAMSUNG/Databases/index_0220/raw/vashdom24.ru/b_sale_order_props_value.txt",
            sep=",",
            header=False,
            schema=order_props_schema,
        )
        df_order_props = df_order_props.groupBy("order_id").agg(
            first(
                when(col("field_code") == "FIO", col("field_value")), ignorenulls=True
            ).alias("FIO"),
            first(
                when(col("field_code") == "PHONE", col("field_value")), ignorenulls=True
            ).alias("PHONE"),
            first(
                when(col("field_code") == "CITY", col("field_value")), ignorenulls=True
            ).alias("CITY"),
            first(
                when(col("field_code") == "STREET", col("field_value")),
                ignorenulls=True,
            ).alias("STREET"),
            first(
                when(col("field_code") == "HOUSE", col("field_value")), ignorenulls=True
            ).alias("HOUSE"),
            first(
                when(col("field_code") == "EMAIL", col("field_value")), ignorenulls=True
            ).alias("EMAIL"),
            first(
                when(col("field_code") == "APARTAMENT", col("field_value")),
                ignorenulls=True,
            ).alias("APARTAMENT"),
        )

        df_order_props = (
            df_order_props.withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("FIO")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("EMAIL")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("PHONE")))))
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("CITY").isNotNull(),
                                address_udf(
                                    concat_ws(
                                        " ",
                                        col("CITY"),
                                        col("STREET"),
                                        col("HOUSE"),
                                        col("APARTAMENT"),
                                    )
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("works", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "accounts",
                "ips",
                "works",
            )
        )

        df_order_props = df_order_props.drop_duplicates()

        sender_contact_schema = (
            StructType()
            .add("unknown_field_1", IntegerType(), True)
            .add("unknown_field_2", IntegerType(), True)
            .add("unknown_field_3", IntegerType(), True)
            .add("name", StringType(), True)
            .add("email", StringType(), True)
            .add("unknown_field_4", StringType(), True)
            .add("unknown_field_5", StringType(), True)
            .add("unknown_field_6", StringType(), True)
            .add("ip", StringType(), True)
            .add("unknown_field_7", StringType(), True)
            .add("unknown_field_8", StringType(), True)
            .add("unknown_field_9", StringType(), True)
            .add("unknown_field_10", StringType(), True)
            .add("unknown_field_11", StringType(), True)
            .add("unknown_field_12", StringType(), True)
            .add("unknown_field_13", StringType(), True)
        )

        df_sender_contact = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0220/raw/vashdom24.ru/b_sender_contact.txt",
                sep=",",
                header=False,
                schema=sender_contact_schema,
            )
            .replace("NULL", None)
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("phones", array())
            .withColumn("address", array())
            .withColumn("accounts", array())
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array_compact(array(struct(col("ip_address").alias("ip")))),
                ),
            )
            .withColumn("works", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "accounts",
                "ips",
                "works",
            )
        )

        user_schema = (
            StructType()
            .add("ID", StringType(), True)
            .add("TIMESTAMP_X", StringType(), True)
            .add("LOGIN", StringType(), True)
            .add("PASSWORD", StringType(), True)
            .add("CHECKWORD", StringType(), True)
            .add("ACTIVE", StringType(), True)
            .add("NAME", StringType(), True)
            .add("LAST_NAME", StringType(), True)
            .add("EMAIL", StringType(), True)
            .add("LAST_LOGIN", StringType(), True)
            .add("DATE_REGISTER", StringType(), True)
            .add("LID", StringType(), True)
            .add("PERSONAL_PROFESSION", StringType(), True)
            .add("PERSONAL_WWW", StringType(), True)
            .add("PERSONAL_ICQ", StringType(), True)
            .add("PERSONAL_GENDER", StringType(), True)
            .add("PERSONAL_BIRTHDATE", StringType(), True)
            .add("PERSONAL_PHOTO", StringType(), True)
            .add("PERSONAL_PHONE", StringType(), True)
            .add("PERSONAL_FAX", StringType(), True)
            .add("PERSONAL_MOBILE", StringType(), True)
            .add("PERSONAL_PAGER", StringType(), True)
            .add("PERSONAL_STREET", StringType(), True)
            .add("PERSONAL_MAILBOX", StringType(), True)
            .add("PERSONAL_CITY", StringType(), True)
            .add("PERSONAL_STATE", StringType(), True)
            .add("PERSONAL_ZIP", StringType(), True)
            .add("PERSONAL_COUNTRY", StringType(), True)
            .add("PERSONAL_NOTES", StringType(), True)
            .add("WORK_COMPANY", StringType(), True)
            .add("WORK_DEPARTMENT", StringType(), True)
            .add("WORK_POSITION", StringType(), True)
            .add("WORK_WWW", StringType(), True)
            .add("WORK_PHONE", StringType(), True)
            .add("WORK_FAX", StringType(), True)
            .add("WORK_PAGER", StringType(), True)
            .add("WORK_STREET", StringType(), True)
            .add("WORK_MAILBOX", StringType(), True)
            .add("WORK_CITY", StringType(), True)
            .add("WORK_STATE", StringType(), True)
            .add("WORK_ZIP", StringType(), True)
            .add("WORK_COUNTRY", StringType(), True)
            .add("WORK_PROFILE", StringType(), True)
            .add("WORK_LOGO", StringType(), True)
            .add("WORK_NOTES", StringType(), True)
            .add("ADMIN_NOTES", StringType(), True)
            .add("STORED_HASH", StringType(), True)
            .add("XML_ID", StringType(), True)
            .add("PERSONAL_BIRTHDAY", StringType(), True)
            .add("EXTERNAL_AUTH_ID", StringType(), True)
            .add("CHECKWORD_TIME", StringType(), True)
            .add("SECOND_NAME", StringType(), True)
            .add("CONFIRM_CODE", StringType(), True)
            .add("LOGIN_ATTEMPTS", StringType(), True)
            .add("LAST_ACTIVITY_DATE", StringType(), True)
            .add("AUTO_TIME_ZONE", StringType(), True)
            .add("TIME_ZONE", StringType(), True)
            .add("TIME_ZONE_OFFSET", StringType(), True)
            .add("TITLE", StringType(), True)
            .add("BX_USER_ID", StringType(), True)
            .add("LANGUAGE_ID", StringType(), True)
            .add("BLOCKED", StringType(), True)
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0220/raw/vashdom24.ru/b_user.txt",
                sep=",",
                header=False,
                schema=user_schema,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("WORK_PHONE")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("EMAIL")), email_udf(col("LOGIN")))
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Vashdom24").alias("title"),
                            lit("https://vashdom24.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            lit(None).alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_DEPARTMENT").isNotNull()
                    | col("WORK_POSITION").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    trim(
                                        concat_ws(
                                            " ",
                                            col("WORK_DEPARTMENT"),
                                            col("WORK_POSITION"),
                                        )
                                    ),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn("ips", array())
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
                            )
                        )
                    )
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "accounts",
                "ips",
                "works",
            )
        )

        df = (
            df_cards.unionAll(df_order_props)
            .unionAll(df_sender_contact)
            .unionAll(df_users)
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.groupBy(["emails", "phones"]).agg(
            array_compact(flatten(collect_set(col("names")))).alias("names"),
            array_compact(flatten(collect_set(col("works")))).alias("works"),
            array_compact(flatten(collect_set(col("accounts")))).alias("accounts"),
            array_compact(flatten(collect_set(col("address")))).alias("address"),
            array_compact(flatten(collect_set(col("ips")))).alias("ips"),
            first(col("sex"), ignorenulls=True).alias("sex"),
            first(col("birth_date"), ignorenulls=True).alias("birth_date"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
