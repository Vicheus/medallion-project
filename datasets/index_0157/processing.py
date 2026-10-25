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
from parsetron.sections.document.udfs import document_udf
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
    dataset_code_name: str = "index_0157"

    def parser(self):
        df_b_sale_order = self.read(
            path="/media/user/SAMSUNG/Databases/index_0157/raw/finewall.ru/b_sale_order.csv",
            sep=";",
            header=True,
        )
        df_b_sale_order_props_value = self.read(
            path="/media/user/SAMSUNG/Databases/index_0157/raw/finewall.ru/b_sale_order_props_value.csv",
            sep=";",
            header=True,
        )
        df_b_user = self.read(
            path="/media/user/SAMSUNG/Databases/index_0157/raw/finewall.ru/b_user.csv",
            sep=";",
            header=True,
        )

        df_b_sale_user_props = self.read(
            path="/media/user/SAMSUNG/Databases/index_0157/raw/finewall.ru/b_sale_user_props.csv",
            sep=";",
            header=True,
        )
        df_b_sale_user_props_value = self.read(
            path="/media/user/SAMSUNG/Databases/index_0157/raw/finewall.ru/b_sale_user_props_value.csv",
            sep=";",
            header=True,
        )

        df_user_props = (
            df_b_sale_user_props.join(
                df_b_sale_user_props_value,
                df_b_sale_user_props_value["USER_PROPS_ID"]
                == df_b_sale_user_props["ID"],
                "inner",
            )
            .select(
                df_b_sale_user_props["USER_ID"].alias("USER_ID"),
                df_b_sale_user_props_value["NAME"].alias("NAME"),
                df_b_sale_user_props_value["VALUE"].alias("VALUE"),
            )
            .dropDuplicates(["USER_ID", "NAME"])
            .groupBy("USER_ID")
            .pivot("NAME")
            .agg({"VALUE": "first"})
            .withColumnRenamed("e-mai", "email3")
            .withColumnRenamed("e-mail", "email4")
            .withColumnRenamed("Ваше имя", "name2")
            .withColumnRenamed("Телефон", "phone2")
        )

        df_orders_props = (
            df_b_sale_order.join(
                df_b_sale_order_props_value,
                df_b_sale_order_props_value["ORDER_ID"] == df_b_sale_order["ID"],
                "inner",
            )
            .select("USER_ID", "NAME", "VALUE")
            .filter(col("NAME") != "e-mail")
            .dropDuplicates(["USER_ID", "NAME"])
            .groupBy("USER_ID")
            .pivot("NAME")
            .agg({"VALUE": "first"})
        )

        df_orders_props = (
            df_orders_props.withColumnRenamed("E-Mail", "email1")
            .withColumnRenamed("e-mai", "email2")
            .withColumnRenamed("Ф.И.О.", "name")
            .select(
                "USER_ID",
                "email1",
                "email2",
                "Адрес",
                "Адрес доставки",
                "Дата выдачи паспорта",
                "Паспорт",
                "Телефон",
            )
        )

        df = df_b_user.join(
            df_orders_props, df_orders_props["USER_ID"] == df_b_user["ID"], "left"
        ).join(df_user_props, df_user_props["USER_ID"] == df_b_user["ID"], "left")

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            ),
                            name_udf(col("name")),
                            name_udf(col("name2")),
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
                            phone_udf(col("Телефон")),
                            phone_udf(col("phone2")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("EMAIL")),
                            email_udf(col("email1")),
                            email_udf(col("email2")),
                            email_udf(col("email3")),
                            email_udf(col("email4")),
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
                            address_udf(col("Адрес")),
                            address_udf(col("Адрес доставки")),
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
                            lit("FineWall").alias("title"),
                            lit("https://finewall.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            col("ID").alias("id"),
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
                "documents",
                when(
                    col("Паспорт").isNotNull(),
                    array_compact(
                        array(
                            document_udf(
                                lit(None),
                                col("Паспорт"),
                                col("Дата выдачи паспорта"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            )
                        )
                    ),
                ).otherwise(None),
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
            "documents",
            "actuality",
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
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
