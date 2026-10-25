from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    expr,
    from_unixtime,
    max,
    greatest,
    concat_ws,
    udf,
    array_distinct,
    size,
    flatten,
    collect_set,
    regexp_extract,
)
from pyspark.sql.types import StringType

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    address_udf,
    name_udf,
    relations_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0136"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        def decode_unicode_escape(input_string):
            try:
                if not input_string:
                    return None
                input_string = input_string.rstrip("\\")
                input_string = input_string.replace("\\\\", "\\").replace('\\"', '"')

                return input_string.encode("utf-8").decode("unicode_escape")
            except:  # noqa: E722
                print(f"Error decoding: {input_string}")
                return None

        decode_unicode_escape_udf = udf(decode_unicode_escape, StringType())

        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0136/raw/rozavam.ru/flr_clients_@kingsmanrecovery.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("name", decode_unicode_escape_udf(col("name")))
            .withColumn(
                "names", array_distinct(array_compact(array(name_udf(col("name")))))
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(array(regexp_extract(col("phone"), r"\d+", 0)))
                ),
            )
            .withColumn("emails", array())
            .withColumn("address", array())
            .withColumn("ips", array())
            .withColumn("accounts", array())
            .withColumn("relations", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("addDate"), col("DateChange"), col("lastOrderDate")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                array(
                    raw_metadata_udf(
                        lit("bonuses"),
                        col("bonuses"),
                        lit("Comment"),
                        decode_unicode_escape_udf(col("Comment")),
                        lit("totalSumm"),
                        col("totalSumm"),
                        lit("ordersCount"),
                        col("ordersCount"),
                        lit("totalProfit"),
                        col("totalProfit"),
                    )
                ),
            )
            .select(
                "names",
                "phones",
                "relations",
                "emails",
                "address",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df_clients.cache()

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0136/raw/rozavam.ru/fl_users_@kingsmanrecovery.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("name", decode_unicode_escape_udf(col("name")))
            .withColumn("fullname", decode_unicode_escape_udf(col("fullname")))
            .withColumn("logged_ip", ip_address_udf(col("logged_ip")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("lastdate"), col("reg_date"), col("lastOrderDate")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata_1",
                raw_metadata_udf(
                    lit("bonuses"),
                    col("bonuses"),
                    lit("totalProfit"),
                    col("totalProfit"),
                ),
            )
            .select(
                "user_id",
                "email",
                "name",
                "fullname",
                "password",
                "logged_ip",
                "lastdate",
                "actuality",
                "raw_metadata_1",
            )
        )

        df_users.cache()

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0136/raw/rozavam.ru/flr_orders_@kingsmanrecovery.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("NameI", decode_unicode_escape_udf(col("NameI")))
            .withColumn("NameP", decode_unicode_escape_udf(col("NameP")))
            .withColumn("Adress", decode_unicode_escape_udf(col("Adress")))
            .withColumn("EmailI", decode_unicode_escape_udf(col("EmailI")))
            .withColumn("PhoneI", regexp_extract(col("PhoneI"), r"\d+", 0))
            .withColumn("PhoneP", regexp_extract(col("PhoneP"), r"\d+", 0))
            .withColumn("IP", ip_address_udf(col("IP")))
            .withColumn(
                "raw_metadata_2",
                raw_metadata_udf(
                    lit("cardText"),
                    decode_unicode_escape_udf(col("cardText")),
                    lit("Comment"),
                    decode_unicode_escape_udf(col("Comment")),
                    lit("totalSumm"),
                    col("totalSumm"),
                    lit("AdressPoint"),
                    decode_unicode_escape_udf(col("AdressPoint")),
                    lit("courierName"),
                    decode_unicode_escape_udf(col("courierName")),
                    lit("paymentType"),
                    decode_unicode_escape_udf(col("paymentType")),
                    lit("AdminComments"),
                    decode_unicode_escape_udf(col("AdminComments")),
                ),
            )
            .select(
                "orderId",
                "user_id",
                "IP",
                "NameI",
                "NameP",
                "Adress",
                "EmailI",
                "PhoneI",
                "PhoneP",
                "Date",
                "DateAdd",
                "raw_metadata_2",
            )
        )

        df_orders_sender = (
            df_orders.join(df_users, "user_id", "left")
            .withColumn(
                "names",
                array_distinct(
                    array_compact(
                        array(name_udf(col("NameI")), name_udf(col("fullname")))
                    )
                ),
            )
            .withColumn(
                "phones", array_distinct(array_compact(array(phone_udf(col("PhoneI")))))
            )
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(
                        array(email_udf(col("email")), email_udf(col("EmailI")))
                    )
                ),
            )
            .withColumn("address", array())
            .withColumn(
                "relations",
                when(
                    name_udf(col("NameP")).isNotNull(),
                    array_compact(
                        array(
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("NameP")),
                                    col("PhoneP"),
                                    col("Address"),
                                )
                            )
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "accounts",
                when(
                    col("name").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("RozaVam.ru").alias("title"),
                            lit("https://rozavam.ru").alias("link"),
                            col("user_id").alias("id"),
                            col("name").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("IP").isNotNull() | col("logged_ip").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                when(
                                    col("IP").isNotNull(),
                                    struct(
                                        ip_address_udf(col("IP")).alias("ip"),
                                        ip_date_udf(col("Date")).alias("date"),
                                    ),
                                ),
                                when(
                                    col("logged_ip").isNotNull(),
                                    struct(
                                        ip_address_udf(col("logged_ip")).alias("ip"),
                                        ip_date_udf(
                                            from_unixtime(col("lastdate"))
                                        ).alias("date"),
                                    ),
                                ),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                array_distinct(
                    array_compact(
                        array(
                            name_udf(col("raw_metadata_1")),
                            name_udf(col("raw_metadata_2")),
                        )
                    )
                ),
            )
            .select(
                "names",
                "phones",
                "relations",
                "emails",
                "address",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df_orders_receiver = (
            df_orders.withColumn(
                "names", array_distinct(array_compact(array(name_udf(col("NameP")))))
            )
            .withColumn(
                "phones", array_distinct(array_compact(array(phone_udf(col("PhoneP")))))
            )
            .withColumn("emails", array())
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("Adress"))))),
            )
            .withColumn(
                "relations",
                when(
                    name_udf(col("NameI")).isNotNull(),
                    array_compact(
                        array(
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_udf(col("NameI")),
                                    col("PhoneI"),
                                    col("EmailI"),
                                )
                            )
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("DateAdd"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("raw_metadata", array(col("raw_metadata_2")))
            .select(
                "names",
                "phones",
                "relations",
                "emails",
                "address",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_orders_receiver.unionAll(df_orders_sender).unionAll(df_clients)

        df_with_phone = df.filter(col("phones").isNotNull())
        df_with_phone = (
            df_with_phone.groupby(["names", "phones"])
            .agg(
                flatten(collect_set("address")).alias("address"),
                flatten(collect_set("emails")).alias("emails"),
                flatten(collect_set("accounts")).alias("accounts"),
                flatten(collect_set("relations")).alias("relations"),
                flatten(collect_set("ips")).alias("ips"),
                flatten(collect_set(col("raw_metadata"))).alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array_distinct(array_compact(col("names"))))
            .withColumn("phones", array_distinct(array_compact(col("phones"))))
            .select(
                "names",
                "phones",
                "relations",
                "emails",
                "address",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df_without_phone = (
            df.filter(col("phones").isNull())
            .withColumn("names", array_distinct(array_compact(col("names"))))
            .withColumn("phones", array_distinct(array_compact(col("phones"))))
            .select(
                "names",
                "phones",
                "relations",
                "emails",
                "address",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_with_phone.unionAll(df_without_phone)

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = (
            df.withColumn("address", expr("slice(address, 1, 15)"))
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
            .withColumn("ips", expr("slice(ips, 1, 15)"))
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
