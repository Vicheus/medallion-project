from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    coalesce,
    struct,
    concat_ws,
    concat,
    array_union,
    size,
    array_compact,
    array_distinct,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    address_udf,
    name_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0042"

    def parser(self):

        df_drivers_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Водители_8.9к.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("family"), col("sec_fam"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones")
        )
        df_drivers_2_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Водители2_26к.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("family"), col("sec_fam"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones")
        )
        df_drivers_2_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Водители_39.9к.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("full_name")))
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones")
        )
        df_drivers_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Водители_770.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("family"), col("sec_fam"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .select("names", "phones")
        )

        df_drivers = (
            df_drivers_1.unionAll(df_drivers_2_1)
            .unionAll(df_drivers_2_2)
            .unionAll(df_drivers_3)
            .filter(col("names").isNotNull() & col("phones").isNotNull())
            .withColumn("address", lit(None))
            .withColumn("accounts", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("raw_metadata", array())
            .drop_duplicates(["names", "phones"])
            .select("names", "phones", "emails", "accounts", "address", "raw_metadata")
        )

        df_users_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Пользователи_2.4к.csv",
            sep=",",
            header=True,
        )
        df_users_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Пользователи_2к.csv",
            sep=",",
            header=True,
        )
        df_users_3 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Пользователи_1.8к.csv",
            sep=",",
            header=True,
        )
        df_users = (
            df_users_1.unionAll(df_users_2)
            .unionAll(df_users_3)
            .drop_duplicates(["name", "family", "phone"])
        )

        df_users = (
            df_users.withColumn(
                "names", coalesce(name_udf(col("family")), name_udf(col("family")))
            )
            .withColumn("phones", phone_udf("phone"))
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull(),
                    array(
                        struct(
                            lit("DOSTAЕВСКИЙ — Доставка еды - Достаевский").alias(
                                "title"
                            ),
                            lit("https://dostaevsky.ru").alias("link"),
                            col("id").alias("id"),
                            col("password").alias("password"),
                        )
                    ),
                ),
            )
            .filter(col("names").isNotNull() & col("phones").isNotNull())
            .withColumn("address", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("raw_metadata", lit(None))
            .drop_duplicates(["names", "phones"])
            .select("names", "phones", "emails", "accounts", "address", "raw_metadata")
        )

        df_clients_addresses = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Адрес_клиентов_9.3к.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        lit("г. Москва"),
                        when(col("street").isNotNull(), col("street")).otherwise(None),
                        when(
                            col("building").isNotNull(),
                            concat(lit("д. "), col("building")),
                        ).otherwise(None),
                        when(
                            col("parade").isNotNull(),
                            concat(lit("под. "), col("parade")),
                        ).otherwise(None),
                        when(
                            col("floor").isNotNull(), concat(lit("эт. "), col("floor"))
                        ).otherwise(None),
                        when(
                            col("flat").isNotNull(), concat(lit("кв. "), col("flat"))
                        ).otherwise(None),
                        when(
                            col("intercomcode").isNotNull(),
                            concat(lit("домофон "), col("intercomcode")),
                        ).otherwise(None),
                    )
                ),
            )
            .groupBy(["id_client"])
            .agg(
                collect_set("address").alias("client_addresses"),
            )
            .select("id_client", "client_addresses")
        )

        df_orders_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Заказы_3.2M.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                coalesce(
                    address_udf(col("adress")),
                    address_udf(
                        concat_ws(
                            ", ",
                            lit("г. Москва"),
                            when(col("street").isNotNull(), col("street")).otherwise(
                                None
                            ),
                            when(
                                col("house_number").isNotNull(),
                                concat(lit("д. "), col("house_number")),
                            ).otherwise(None),
                            when(
                                col("entrance").isNotNull(),
                                concat(lit("под. "), col("entrance")),
                            ).otherwise(None),
                            when(
                                col("floor").isNotNull(),
                                concat(lit("эт. "), col("floor")),
                            ).otherwise(None),
                            when(
                                col("appartment_number").isNotNull(),
                                concat(lit("кв. "), col("appartment_number")),
                            ).otherwise(None),
                            when(
                                col("intercom").isNotNull(),
                                concat(lit("домофон "), col("intercom")),
                            ).otherwise(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("note_adress"),
                    col("note_adress"),
                    lit("sum"),
                    col("sum"),
                    lit("count_person"),
                    col("count_person"),
                    lit("dat_add_utc"),
                    col("dat_add_utc"),
                    lit("ingridients"),
                    col("ingridients"),
                    lit("website"),
                    col("website"),
                    lit("delivery"),
                    col("delivery"),
                    lit("delivery_date_utc"),
                    col("delivery_date_utc"),
                ),
            )
            .groupBy(["id_client"])
            .agg(
                collect_set("address").alias("order_addresses"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("id_client", "order_addresses", "raw_metadata")
        )
        df_orders_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Заказы_19.9М.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                coalesce(
                    address_udf(col("adress")),
                    address_udf(
                        concat_ws(
                            ", ",
                            lit("г. Санкт-Петербург"),
                            when(col("street").isNotNull(), col("street")).otherwise(
                                None
                            ),
                            when(
                                col("house_number").isNotNull(),
                                concat(lit("д. "), col("house_number")),
                            ).otherwise(None),
                            when(
                                col("entrance").isNotNull(),
                                concat(lit("под. "), col("entrance")),
                            ).otherwise(None),
                            when(
                                col("floor").isNotNull(),
                                concat(lit("эт. "), col("floor")),
                            ).otherwise(None),
                            when(
                                col("appartment_number").isNotNull(),
                                concat(lit("кв. "), col("appartment_number")),
                            ).otherwise(None),
                            when(
                                col("intercom").isNotNull(),
                                concat(lit("домофон "), col("intercom")),
                            ).otherwise(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("note_adress"),
                    col("note_adress"),
                    lit("sum"),
                    col("sum"),
                    lit("count_person"),
                    col("count_person"),
                    lit("dat_add_utc"),
                    col("dat_add_utc"),
                    lit("ingridients"),
                    col("ingridients"),
                    lit("website"),
                    col("website"),
                    lit("delivery"),
                    col("delivery"),
                    lit("delivery_date_utc"),
                    col("delivery_date_utc"),
                ),
            )
            .groupBy(["id_client"])
            .agg(
                collect_set("address").alias("order_addresses"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("id_client", "order_addresses", "raw_metadata")
        )
        df_orders_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Заказы_927к.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                coalesce(
                    address_udf(col("adress")),
                    address_udf(
                        concat_ws(
                            ", ",
                            lit("г. Сочи"),
                            when(col("street").isNotNull(), col("street")).otherwise(
                                None
                            ),
                            when(
                                col("house_number").isNotNull(),
                                concat(lit("д. "), col("house_number")),
                            ).otherwise(None),
                            when(
                                col("entrance").isNotNull(),
                                concat(lit("под. "), col("entrance")),
                            ).otherwise(None),
                            when(
                                col("floor").isNotNull(),
                                concat(lit("эт. "), col("floor")),
                            ).otherwise(None),
                            when(
                                col("appartment_number").isNotNull(),
                                concat(lit("кв. "), col("appartment_number")),
                            ).otherwise(None),
                            when(
                                col("intercom").isNotNull(),
                                concat(lit("домофон "), col("intercom")),
                            ).otherwise(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("note_adress"),
                    col("note_adress"),
                    lit("sum"),
                    col("sum"),
                    lit("count_person"),
                    col("count_person"),
                    lit("dat_add_utc"),
                    col("dat_add_utc"),
                    lit("ingridients"),
                    col("ingridients"),
                    lit("website"),
                    col("website"),
                    lit("delivery"),
                    col("delivery"),
                    lit("delivery_date_utc"),
                    col("delivery_date_utc"),
                ),
            )
            .groupBy(["id_client"])
            .agg(
                collect_set("address").alias("order_addresses"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("id_client", "order_addresses", "raw_metadata")
        )

        df_clients_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Клиенты_440к.csv",
            sep=",",
            header=True,
        ).replace("\x00\x00\x00\x00", "")
        df_clients_1 = (
            df_clients_1.join(
                df_clients_addresses,
                df_clients_1.id == df_clients_addresses.id_client,
                "left",
            )
            .join(df_orders_1, df_clients_1.id == df_orders_1.id_client, "left")
            .withColumn(
                "address",
                array_union(
                    col("client_addresses"),
                    array_union(col("order_addresses"), array(col("street"))),
                ),
            )
            .select("id", "name", "card", "phone", "email", "address", "raw_metadata")
        )
        df_clients_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Клиенты_2.4М.csv",
            sep=",",
            header=True,
        ).replace("\x00\x00\x00\x00", "")
        df_clients_2 = (
            df_clients_2.join(
                df_orders_2, df_clients_2.id == df_orders_2.id_client, "left"
            )
            .withColumn(
                "address", array_union(col("order_addresses"), array(col("street")))
            )
            .select("id", "name", "card", "phone", "email", "address", "raw_metadata")
        )
        df_clients_3 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0042/raw/Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Клиенты_187к.csv",
            sep=",",
            header=True,
        ).replace("\x00\x00\x00\x00", "")
        df_clients_3 = (
            df_clients_3.join(
                df_orders_3, df_clients_3.id == df_orders_3.id_client, "left"
            )
            .withColumn(
                "address", array_union(col("order_addresses"), array(col("street")))
            )
            .select("id", "name", "card", "phone", "email", "address", "raw_metadata")
        )
        df_clients = (
            df_clients_1.unionAll(df_clients_2)
            .unionAll(df_clients_3)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull() | col("card").isNotNull(),
                    array(
                        struct(
                            lit("DOSTAЕВСКИЙ — Доставка еды - Достаевский").alias(
                                "title"
                            ),
                            lit("https://dostaevsky.ru").alias("link"),
                            col("id").alias("id"),
                            col("card").alias("client_card_number"),
                        )
                    ),
                ),
            )
        )
        df_clients = df_clients.select(
            "names", "phones", "emails", "accounts", "address", "raw_metadata"
        )

        df = (
            df_drivers.unionAll(df_users)
            .unionAll(df_clients)
            .drop_duplicates(["names", "phones"])
        )

        df = df.select(
            "names", "emails", "phones", "accounts", "address", "raw_metadata"
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(array_distinct(col("accounts")))) > 0,
                    array_compact(array_distinct(col("accounts"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(array_distinct(col("address")))) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(array_distinct(col("raw_metadata")))) > 0,
                    array_compact(array_distinct(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df.show(truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
