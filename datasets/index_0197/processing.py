from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    max,
    array_distinct,
    regexp_replace,
    array_compact,
    flatten,
    size,
    concat_ws,
    collect_set,
    transform,
    trim,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = True
    dataset_code_name: str = "index_0197"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df_clients = self.read(
            path="/media/user/SAMSUNG/Databases/index_0197/raw/autolight_by/all/clients_*.json",
            sep="\n",
            header=False,
        )
        df_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0197/raw/autolight_by/all/orders_*.json",
            sep="\n",
            header=False,
        )

        df_clients = (
            df_clients.withColumn(
                "names",
                when(
                    col("UF_CONTACT").isNotNull(),
                    regexp_replace(name_udf(col("UF_CONTACT")), r"-|\.", ""),
                ).otherwise(
                    regexp_replace(
                        name_parts_udf(
                            col("UF_NAME"), col("UF_LAST_NAME"), col("UF_SECOND_NAME")
                        ),
                        r"-|.",
                        "",
                    )
                ),
            )
            .withColumn(
                "phones",
                array(phone_udf(col("UF_PHONE"), lit(self.dataset_country_code.value))),
            )
            .withColumn("emails", array(email_udf(col("UF_EMAIL"))))
            .withColumn(
                "address",
                array(
                    address_udf(
                        regexp_replace(
                            concat_ws(
                                " ",
                                when(
                                    col("UF_COUNTRY").isNotNull(), col("UF_COUNTRY")
                                ).otherwise(lit(None)),
                                when(
                                    col("UF_CITY").isNotNull(), col("UF_CITY")
                                ).otherwise(lit(None)),
                                when(
                                    col("UF_STREET").isNotNull(), col("UF_STREET")
                                ).otherwise(lit(None)),
                                when(
                                    col("UF_HOUSE").isNotNull(),
                                    concat_ws(" ", lit("д. "), col("UF_HOUSE")),
                                ).otherwise(lit(None)),
                                when(
                                    col("UF_KORPUS").isNotNull(),
                                    concat_ws(" ", lit("корп. "), col("UF_KORPUS")),
                                ).otherwise(lit(None)),
                                when(
                                    col("UF_FLAT").isNotNull(),
                                    concat_ws(" ", lit("кв. "), col("UF_FLAT")),
                                ).otherwise(lit(None)),
                            ),
                            r"\[\{\d+\}\]",
                            "",
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                array(
                    when(
                        col("UF_ORGANIZATION").isNotNull(),
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("UF_ORGANIZATION"),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn("relations", array())
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df_users_who_posted = (
            df_orders.withColumn("names", name_udf(col("UF_RAZMESTIL_FIO")))
            .withColumn(
                "phones",
                array(
                    phone_udf(
                        col("UF_RAZMESTIL_PHONE"), lit(self.dataset_country_code.value)
                    )
                ),
            )
            .withColumn("emails", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn("relations", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("UF_DATE_TIME"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("UF_ADDITIONAL_OPTIONS_STRING"),
                    col("UF_ADDITIONAL_OPTIONS_STRING"),
                    lit("UF_DELIVERY_FROM"),
                    col("UF_DELIVERY_FROM"),
                    lit("UF_DELIVERY_TO"),
                    col("UF_DELIVERY_TO"),
                    lit("UF_DRIVER"),
                    col("UF_DRIVER"),
                    lit("UF_DRIVER_DATA"),
                    col("UF_DRIVER_DATA"),
                    lit("UF_OPERATOR"),
                    col("UF_OPERATOR"),
                    lit("UF_OPIS"),
                    col("UF_OPIS"),
                    lit("UF_OUT_COMMENT"),
                    col("UF_OUT_COMMENT"),
                    lit("UF_TTN"),
                    col("UF_TTN"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df_senders = (
            df_orders.withColumn("names", name_udf(col("UF_SENDER_FIO")))
            .withColumn("phones", array())
            .withColumn("emails", array(col("UF_EMAIL_SENDER")))
            .withColumn("address", array(address_udf(col("UF_FULL_ADRES_OTPRAVITEL"))))
            .withColumn(
                "works",
                array(
                    when(
                        col("UF_ORGANIZATION_SENDER").isNotNull(),
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("UF_ORGANIZATION_SENDER"),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "relations",
                when(
                    col("UF_CONTACT_SENDER").isNotNull()
                    & col("UF_CONTACT_MOBILE_SENDER").isNotNull(),
                    array(
                        concat_ws(
                            " ",
                            name_udf(col("UF_CONTACT_SENDER")),
                            phone_udf(
                                col("UF_CONTACT_MOBILE_SENDER"),
                                lit(self.dataset_country_code.value),
                            ),
                            lit("Контактное лицо"),
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("UF_DATE_TIME"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("UF_ADDITIONAL_OPTIONS_STRING"),
                    col("UF_ADDITIONAL_OPTIONS_STRING"),
                    lit("UF_DELIVERY_FROM"),
                    col("UF_DELIVERY_FROM"),
                    lit("UF_DELIVERY_TO"),
                    col("UF_DELIVERY_TO"),
                    lit("UF_DRIVER"),
                    col("UF_DRIVER"),
                    lit("UF_DRIVER_DATA"),
                    col("UF_DRIVER_DATA"),
                    lit("UF_OPERATOR"),
                    col("UF_OPERATOR"),
                    lit("UF_OPIS"),
                    col("UF_OPIS"),
                    lit("UF_OUT_COMMENT"),
                    col("UF_OUT_COMMENT"),
                    lit("UF_TTN"),
                    col("UF_TTN"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df_senders_contact_persons = (
            df_orders.withColumn("names", name_udf(col("UF_CONTACT_SENDER")))
            .withColumn(
                "phones",
                array(
                    phone_udf(
                        col("UF_CONTACT_MOBILE_SENDER"),
                        lit(self.dataset_country_code.value),
                    )
                ),
            )
            .withColumn("emails", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "relations",
                when(
                    col("UF_SENDER_FIO").isNotNull(),
                    array(
                        concat_ws(" ", name_udf(col("UF_SENDER_FIO"))),
                        lit("Контактное лицо"),
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("UF_DATE_TIME"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("UF_ADDITIONAL_OPTIONS_STRING"),
                    col("UF_ADDITIONAL_OPTIONS_STRING"),
                    lit("UF_DELIVERY_FROM"),
                    col("UF_DELIVERY_FROM"),
                    lit("UF_DELIVERY_TO"),
                    col("UF_DELIVERY_TO"),
                    lit("UF_DRIVER"),
                    col("UF_DRIVER"),
                    lit("UF_DRIVER_DATA"),
                    col("UF_DRIVER_DATA"),
                    lit("UF_OPERATOR"),
                    col("UF_OPERATOR"),
                    lit("UF_OPIS"),
                    col("UF_OPIS"),
                    lit("UF_OUT_COMMENT"),
                    col("UF_OUT_COMMENT"),
                    lit("UF_TTN"),
                    col("UF_TTN"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df_recipients = (
            df_orders.withColumn("names", name_udf(col("UF_RECIPIENT_FIO")))
            .withColumn("phones", array())
            .withColumn("emails", array(email_udf(col("UF_EMAIL_RECIPIENT"))))
            .withColumn("address", array(address_udf(col("UF_FULL_ADRES_POLUCHATEL"))))
            .withColumn("works", array())
            .withColumn("relations", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("UF_DATE_TIME"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("UF_ADDITIONAL_OPTIONS_STRING"),
                    col("UF_ADDITIONAL_OPTIONS_STRING"),
                    lit("UF_DELIVERY_FROM"),
                    col("UF_DELIVERY_FROM"),
                    lit("UF_DELIVERY_TO"),
                    col("UF_DELIVERY_TO"),
                    lit("UF_DRIVER"),
                    col("UF_DRIVER"),
                    lit("UF_DRIVER_DATA"),
                    col("UF_DRIVER_DATA"),
                    lit("UF_OPERATOR"),
                    col("UF_OPERATOR"),
                    lit("UF_OPIS"),
                    col("UF_OPIS"),
                    lit("UF_OUT_COMMENT"),
                    col("UF_OUT_COMMENT"),
                    lit("UF_TTN"),
                    col("UF_TTN"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df = (
            df_recipients.unionAll(df_senders)
            .unionAll(df_senders_contact_persons)
            .unionAll(df_users_who_posted)
            .unionAll(df_clients)
        )

        df_with_phone = (
            df.filter(col("phones").isNotNull() & (col("phones") != ""))
            .groupBy(col("phones"))
            .agg(
                array_distinct(array_compact(collect_set(col("names")))).alias("names"),
                array_distinct(
                    array_compact(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_distinct(
                    array_compact(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_distinct(array_compact(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("relations"))))
                ).alias("relations"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "relations",
                "actuality",
                "raw_metadata",
            )
        )

        df_without_phone = df.filter(col("phones").isNull()).select(
            "names",
            "phones",
            "emails",
            "address",
            "works",
            "relations",
            "actuality",
            "raw_metadata",
        )

        df = df_with_phone.unionAll(df_without_phone)

        df = (
            df.withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    size(array_compact(col("relations"))) > 0,
                    array_compact(col("relations")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0,
                    transform(array_compact(col("names")), lambda x: trim(x)),
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
