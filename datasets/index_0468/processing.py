from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    array_compact,
    size,
    flatten,
    expr,
    max,
    first,
    array_distinct,
    struct,
    concat_ws,
    from_unixtime,
    split,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    phone_udf,
    phones_udf,
    address_udf,
    raw_metadata_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0468"
    validate_invalid_groupping: bool = True
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails,address,socials"

    def parser(self):
        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0468/raw/PlaySexShop.ru - @StormBaseAdapter/Заказы_parsed.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("tmp_phone")), phone_udf(col("phone")))
                    )
                ),
            )
            .withColumn(
                "address", address_udf(concat_ws(" ", col("postcode"), col("address")))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("campaign"),
                    col("campaign"),
                    lit("ritm_comment"),
                    col("ritm_comment"),
                    lit("comment"),
                    col("comment"),
                ),
            )
            .withColumn("socials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("create_ts")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        instagram_pattern = r"https://instagram\.com/([^/]+)"
        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0468/raw/PlaySexShop.ru - @StormBaseAdapter/Клиенты.csv",
                sep=";",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", lit(None))
            .withColumn("emails", array())
            .withColumn(
                "instagram_id",
                regexp_extract(col("Личная страница"), instagram_pattern, 1),
            )
            .withColumn("phones", phones_udf(split(col("Рабочий телефон"), ",")))
            .withColumn("address", address_udf(col("Реквизит (Казахстан) Адрес")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Ответственный"),
                    col("Ответственный"),
                    lit("Источник"),
                    col("Источник"),
                    lit("Кем создан"),
                    col("Кем создан"),
                    lit("Кем изменен"),
                    col("Кем изменен"),
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("instagram_id").isNotNull()
                            & (col("instagram_id") != ""),
                            struct(
                                lit("Instagram").alias("title"),
                                col("instagram_id").alias("id"),
                                col("Личная страница").alias("link"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Последняя активность"), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0468/raw/PlaySexShop.ru - @StormBaseAdapter/Пользователи_parsed.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "address", address_udf(concat_ws(" ", col("postcode"), col("address")))
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn("socials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("create_ts")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df_workers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0468/raw/PlaySexShop.ru - @StormBaseAdapter/Сотрудники.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("E-Mail")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Мобильный телефон")),
                            phone_udf(col("Рабочий телефон")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Интересы"),
                    col("Интересы"),
                    lit("Подразделение"),
                    col("Подразделение"),
                    lit("Должность"),
                    col("Должность"),
                    lit("Дата принятия на работу"),
                    col("Дата принятия на работу"),
                ),
            )
            .withColumn("socials", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_orders.unionAll(df_workers).unionAll(df_clients).unionAll(df_users)

        df_with_phone = df.filter(size(col("phones")) > 0)
        df_without_phone_with_email = df.filter(
            (size(col("phones")) == 0) & (size(col("emails")) > 0)
        )
        df_without_phone_and_email = df.filter(
            (size(col("phones")) == 0) & (size(col("emails")) == 0)
        )

        df_with_phone = (
            df_with_phone.groupBy(["names", "phones"])
            .agg(
                first("birth_date", ignorenulls=True).alias("birth_date"),
                first("sex", ignorenulls=True).alias("sex"),
                array_compact(flatten(collect_set((col("emails"))))).alias("emails"),
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(flatten(collect_set((col("socials"))))).alias("socials"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df_without_phone_with_email = (
            df_without_phone_with_email.groupBy(["names", "emails"])
            .agg(
                first("birth_date", ignorenulls=True).alias("birth_date"),
                first("sex", ignorenulls=True).alias("sex"),
                array_compact(flatten(collect_set((col("phones"))))).alias("phones"),
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(flatten(collect_set((col("socials"))))).alias("socials"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df_without_phone_and_email = df_without_phone_and_email.withColumn(
            "address", array_compact(array(col("address")))
        ).withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))

        df = df_with_phone.unionAll(df_without_phone_and_email).unionAll(
            df_without_phone_with_email
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
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
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
                | col("socials").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
