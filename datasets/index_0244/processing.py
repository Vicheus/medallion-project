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
    concat_ws,
    coalesce,
    first,
    flatten,
    collect_set,
    greatest,
    max,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0244"

    def parser(self):
        df_contact_emails1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/contact_emails_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("email1", email_udf("email"))
            .select("contact_id", "email1")
        )
        df_contact_emails2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/registered_contact_emails_names_from_messages_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("name2", name_udf("name"))
            .withColumn("email2", email_udf("email"))
            .select("contact_id", "email2", "name2")
        )
        df_contacts_data = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/contacts_info_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "address",
                when(
                    col("address_street").isNotNull() | col("address_city").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                address_udf(
                                    concat_ws(
                                        " ",
                                        col("address_zip"),
                                        col("address_city"),
                                        col("address_street"),
                                    )
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("ip_address", ip_address_udf(col("create_ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(ip_address_udf(col("ip_address")).alias("ip"))),
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("create_user_agent").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(
                                    lit("https://kora.ru").alias("title"),
                                    col("create_user_agent").alias("user_agent"),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    col("vkontakte_id").isNotNull() | col("facebook_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vkontakte_id").isNotNull(),
                                social_udf(
                                    lit("Vk"), col("vkontakte_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .select("contact_id", "socials", "devices", "ips", "phones", "address")
        )

        df_contacts1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/contacts1_preprocessed.csv",
            sep=",",
            header=True,
        )

        df_contacts1 = (
            df_contacts1.join(
                df_contact_emails1,
                df_contact_emails1["contact_id"] == df_contacts1["id"],
                "left",
            )
            .join(
                df_contact_emails2,
                df_contact_emails2["contact_id"] == df_contacts1["id"],
                "left",
            )
            .join(
                df_contacts_data,
                df_contacts_data["contact_id"] == df_contacts1["id"],
                "left",
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(array(coalesce(name_udf(col("name")), col("name2"))))
                ),
            )
            .withColumn(
                "emails",
                array_distinct(array_compact(array(col("email1"), col("email2")))),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date",
                birth_date_udf(
                    concat_ws(
                        "-", col("birth_year"), col("birth_month"), col("birth_day")
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("last_datetime"), col("create_datetime")),
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
                "socials",
                "devices",
                "ips",
                "actuality",
            )
        )

        df_contacts2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/contacts2_preprocessed.csv",
            sep=",",
            header=True,
        )

        df_contacts2 = (
            df_contacts2.join(
                df_contact_emails1,
                df_contact_emails1["contact_id"] == df_contacts2["id"],
                "left",
            )
            .join(
                df_contact_emails2,
                df_contact_emails2["contact_id"] == df_contacts2["id"],
                "left",
            )
            .join(
                df_contacts_data,
                df_contacts_data["contact_id"] == df_contacts2["id"],
                "left",
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(array(coalesce(name_udf(col("name")), col("name2"))))
                ),
            )
            .withColumn(
                "emails",
                array_distinct(array_compact(array(col("email1"), col("email2")))),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date",
                birth_date_udf(
                    concat_ws(
                        "-", col("birth_year"), col("birth_month"), col("birth_day")
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("last_datetime"), col("create_datetime")),
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
                "socials",
                "devices",
                "ips",
                "actuality",
            )
        )

        df_unregistered_contacts = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/not_registered_contact_emails_names_from_messages_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn(
                "emails", array_distinct(array_compact(array(email_udf(col("email")))))
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("phones", array())
            .withColumn("address", array())
            .withColumn("socials", array())
            .withColumn("devices", array())
            .withColumn("ips", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "socials",
                "devices",
                "ips",
                "actuality",
            )
        )

        df_unregistered_contacts = df_unregistered_contacts.drop_duplicates(["names"])

        df_contacts_from_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0244/raw/preprocessed/shop_order_params_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            coalesce(
                                name_udf(col("contact_name")),
                                name_udf(col("billing_contact_name")),
                                name_udf(col("sdekint_contact_name")),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("contact_email")),
                            email_udf(col("sdekint_contact_email")),
                        )
                    )
                ),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(ip_address_udf(col("ip_address")).alias("ip"))),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("billing_address_street").isNotNull(),
                                address_udf(
                                    concat_ws(
                                        " ",
                                        col("billing_address_region"),
                                        col("billing_address_street"),
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("sdekint_street").isNotNull()
                                | col("sdekint_city_name").isNotNull(),
                                address_udf(
                                    concat_ws(
                                        " ",
                                        col("sdekint_zip"),
                                        col("sdekint_city_country_name"),
                                        col("sdekint_city_region_name"),
                                        col("sdekint_city_name"),
                                        col("sdekint_street"),
                                    )
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("sdekint_contact_phone")),
                            phone_udf(col("sdekint_contact_phones_0")),
                            phone_udf(col("sdekint_contact_phones_1")),
                            phone_udf(col("sdekint_contact_phones_2")),
                            phone_udf(col("sdekint_contact_phones_3")),
                        )
                    )
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                struct(
                                    lit("https://kora.ru").alias("title"),
                                    col("user_agent").alias("user_agent"),
                                )
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("socials", array())
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "socials",
                "devices",
                "ips",
                "actuality",
            )
        )

        df_contacts_from_orders = df_contacts_from_orders.drop_duplicates(["names"])

        df = (
            df_contacts1.unionAll(df_contacts2)
            .unionAll(df_unregistered_contacts)
            .unionAll(df_contacts_from_orders)
        )

        df = df.groupBy(["names"]).agg(
            flatten(collect_set("emails")).alias("emails"),
            flatten(collect_set("phones")).alias("phones"),
            flatten(collect_set("address")).alias("address"),
            first("sex").alias("sex"),
            first("birth_date").alias("birth_date"),
            flatten(collect_set("socials")).alias("socials"),
            flatten(collect_set("devices")).alias("devices"),
            flatten(collect_set("ips")).alias("ips"),
            max("actuality").alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
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
