from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    first,
    array_compact,
    array,
    lit,
    size,
    max,
    struct,
    coalesce,
    regexp_replace,
    array_distinct,
    flatten,
    collect_list,
    lower,
    concat_ws,
    udf,
)
from pyspark.sql.types import StringType, ArrayType, StructType, StructField

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    name_parts_udf,
    actuality_date_udf,
    address_udf,
    raw_metadata_udf,
)


@udf(
    returnType=ArrayType(
        StructType(
            [
                StructField("title", StringType()),
                StructField("link", StringType()),
                StructField("login", StringType()),
                StructField("password_hash", StringType()),
                StructField("client_card_number", StringType()),
            ]
        )
    )
)
def update_accounts_udf(struct_arr, value_arr):
    if not struct_arr:
        return []
    result = []
    for s in struct_arr:
        s_dict = s.asDict()
        if value_arr and len(value_arr) > 0:
            for value in value_arr:
                s_updated = s_dict.copy()
                s_updated["client_card_number"] = value
                result.append(s_updated)
        else:
            result.append(s_dict)
    return result


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    calc_completeness: bool = True
    dataset_code_name: str = "index_0553"
    validate_invalid_groupping: bool = True

    ignore_fio_titles = [
        "заказ сбермаркета",
        "магазин магнолия",
        "магнолия магазин",
        "иванов иван",
        "иванов иван иванович",
    ]
    ignore_email_patterns = ["feedback@mail.mgnl.ru", "miratleta@yandex.ru"]

    def _prepare_form_result(self):
        form_result_df = (
            self.read(path="b_form_result.csv", sep=",", header=True)
            .withColumn(
                "actuality",
                actuality_date_udf(col("DATE_CREATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("ID", "actuality")
        )

        form_result_df.persist(StorageLevel.DISK_ONLY).count()

        return form_result_df

    def _prepare_form_result_answer(self):
        form_result_answer_df = (
            self.read(path="b_form_result_answer.csv", sep=",", header=True)
            .filter(col("FIELD_ID").isin(1, 2, 3, 20, 21, 22, 35, 36, 58))
            .select("RESULT_ID", "FIELD_ID", "USER_TEXT")
            .groupBy("RESULT_ID")
            .pivot("FIELD_ID")
            .agg(first("USER_TEXT"))
            .withColumn("fio", coalesce(col("1"), col("20"), col("35")))
            .withColumn("email", coalesce(col("3"), col("22"), col("36")))
            .withColumn("phone", coalesce(col("2"), col("21")))
            .select(
                col("RESULT_ID"),
                col("fio"),
                col("email"),
                col("phone"),
                when(
                    regexp_replace(col("58"), " ", "").rlike(r"^\d{16}"),
                    regexp_replace(col("58"), " ", ""),
                ).alias("client_card_number"),
            )
            .filter(
                ~lower(col("fio")).rlike(
                    f"^\\s*({"|".join(self.ignore_fio_titles)})\\s*$"
                )
            )
            .filter(
                ~lower(col("email")).rlike(
                    f"^\\s*({"|".join(self.ignore_email_patterns)})\\s*$"
                )
            )
        )

        form_result_answer_df.persist(StorageLevel.DISK_ONLY).count()

        return form_result_answer_df

    def _prepare_sale_order(self):
        sale_order_df = (
            self.read(path="b_sale_order.csv", sep=",", header=True)
            .withColumn(
                "actuality",
                actuality_date_udf(col("DATE_UPDATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select("ID", "actuality")
        )

        return sale_order_df

    def _prepare_sale_order_props_value(self):
        sale_order_props_value_df = (
            self.read(path="b_sale_order_props_value.csv", sep=",", header=True)
            .filter(col("ORDER_PROPS_ID").isin(1, 2, 3, 7))
            .select("ORDER_ID", "NAME", "ORDER_PROPS_ID", "VALUE")
            .groupBy("ORDER_ID")
            .pivot("NAME")
            .agg(first("VALUE"))
            .select(
                col("ORDER_ID"),
                col("`Ф.И.О.`").alias("fio"),
                col("E-Mail").alias("email"),
                col("Телефон").alias("phone"),
                col("Адрес доставки").alias("address1"),
                col("Адрес доставки (улица, дом)").alias("address2"),
            )
            .filter(
                ~lower(col("fio")).rlike(
                    f"^\\s*({"|".join(self.ignore_fio_titles)})\\s*$"
                )
            )
            .filter(
                ~lower(col("email")).rlike(
                    f"^\\s*({"|".join(self.ignore_email_patterns)})\\s*$"
                )
            )
        )

        sale_order_props_value_df.persist(StorageLevel.DISK_ONLY).count()

        return sale_order_props_value_df

    def _join_forms(self):
        form_result_df = self._prepare_form_result()
        form_result_answer_df = self._prepare_form_result_answer()
        joined_df = form_result_df.join(
            form_result_answer_df,
            form_result_df["ID"] == form_result_answer_df["RESULT_ID"],
            how="inner",
        )

        joined_forms_df = (
            joined_df.withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .select("names", "emails", "phones", "client_card_number", "actuality")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        joined_forms_df.persist(StorageLevel.DISK_ONLY).count()
        form_result_answer_df.unpersist()

        return joined_forms_df

    def _join_sales(self):
        sale_order_df = self._prepare_sale_order()
        sale_order_props_df = self._prepare_sale_order_props_value()
        joined_sales_df = (
            sale_order_df.join(
                sale_order_props_df,
                sale_order_df["ID"] == sale_order_props_df["ORDER_ID"],
                how="inner",
            )
            .withColumn("names", array_compact(array(name_udf(col("fio")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn(
                "address",
                array_compact(
                    array(address_udf(col("address1")), address_udf(col("address2")))
                ),
            )
            .select("names", "emails", "phones", "address", "actuality")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (col("emails").isNotNull() | col("phones").isNotNull())
            )
            .distinct()
        )

        joined_sales_df.persist(StorageLevel.DISK_ONLY).count()
        sale_order_props_df.unpersist()

        return joined_sales_df

    def _prepare_user(self):
        user_df = (
            self.read(path="b_user.csv", sep=",", header=True)
            .withColumn(
                "names",
                array_compact(
                    array(
                        name_parts_udf(
                            col("NAME"), col("LAST_NAME"), col("SECOND_NAME")
                        )
                    )
                ),
            )
            .withColumn("emails", array_compact(array(email_udf(col("EMAIL")))))
            .withColumn(
                "phones", array_compact(array(phone_udf(col("PERSONAL_PHONE"))))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    when(
                        col("LAST_ACTIVITY_DATE").isNotNull(), col("LAST_ACTIVITY_DATE")
                    ).otherwise(
                        when(
                            col("LAST_LOGIN").isNotNull(), col("LAST_LOGIN")
                        ).otherwise(col("DATE_REGISTER"))
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "accounts",
                array_compact(
                    array(
                        struct(
                            lit("Магнолия").alias("title"),
                            lit("https://mgnl.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                            lit(None).cast(StringType()).alias("client_card_number"),
                        )
                    )
                ),
            )
            .select("names", "emails", "phones", "actuality", "accounts")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (
                    col("emails").isNotNull()
                    | col("phones").isNotNull()
                    | col("accounts").isNotNull()
                )
            )
            .distinct()
        )

        user_df.persist(StorageLevel.DISK_ONLY).count()

        return user_df

    def _process(self, df):
        null_df = df.filter(col("emails").isNull() & col("phones").isNull()).withColumn(
            "client_card_number", array_compact(array(col("client_card_number")))
        )
        email_phone_df = df.filter(
            col("emails").isNotNull() | col("phones").isNotNull()
        )

        df = (
            email_phone_df.groupBy("emails", "phones")
            .agg(
                array_distinct(flatten(collect_list("names"))).alias("names"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                max(col("actuality")).alias("actuality"),
                array_distinct(flatten(collect_list(col("accounts")))).alias(
                    "accounts"
                ),
                array_distinct(collect_list("client_card_number")).alias(
                    "client_card_number"
                ),
            )
            .unionByName(null_df)
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        null_df = df.filter(col("names").isNull() | col("accounts").isNull())
        names_accounts_df = df.filter(
            col("names").isNotNull() & col("accounts").isNotNull()
        )

        df = (
            names_accounts_df.groupBy("names", "accounts")
            .agg(
                array_distinct(flatten(collect_list("emails"))).alias("emails"),
                array_distinct(flatten(collect_list("phones"))).alias("phones"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
                max(col("actuality")).alias("actuality"),
                array_distinct(flatten(collect_list("client_card_number"))).alias(
                    "client_card_number"
                ),
            )
            .unionByName(null_df)
            .withColumn(
                "client_card_number",
                when(
                    size(col("client_card_number")) > 0, col("client_card_number")
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "accounts",
                when(
                    col("accounts").isNotNull() & col("client_card_number").isNotNull(),
                    update_accounts_udf(col("accounts"), col("client_card_number")),
                ).otherwise(col("accounts")),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("client_card_number").isNotNull() & col("accounts").isNull(),
                    array(
                        raw_metadata_udf(
                            lit("client_card_number"),
                            concat_ws(" ", col("client_card_number")),
                        )
                    ),
                ),
            )
            .drop("client_card_number")
            .withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
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
            .filter(
                col("names").isNotNull()
                & (
                    col("emails").isNotNull()
                    | col("phones").isNotNull()
                    | col("accounts").isNotNull()
                )
            )
        )
        return df

    def parser(self):
        joined_forms_df = self._join_forms()
        joined_sales_df = self._join_sales()
        user_df = self._prepare_user()

        df = user_df.unionByName(joined_forms_df, True).unionByName(
            joined_sales_df, True
        )

        df = self._process(df)

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
