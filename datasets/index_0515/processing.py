from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    concat_ws,
    greatest,
    struct,
    array_size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    actuality_date_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    addresses_with_type_udf,
    normalize_address_batch_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0515"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 5

    def parser(self):
        df_users = (
            self.read(
                path="/home/user/Downloads/bases_new/conso.ru - @bereza_bd./users.csv",
                sep=",",
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("LOGIN")),
                            phone_udf(col("PERSONAL_MOBILE")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(array(email_udf(col("EMAIL"))))),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("PERSONAL_STREET").isNotNull()
                                    | col("PERSONAL_MAILBOX").isNotNull()
                                    | col("PERSONAL_CITY").isNotNull()
                                    | col("PERSONAL_STATE").isNotNull()
                                    | col("PERSONAL_ZIP").isNotNull(),
                                    concat_ws(
                                        " ",
                                        col("PERSONAL_STREET"),
                                        col("PERSONAL_MAILBOX"),
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_STATE"),
                                        col("PERSONAL_ZIP"),
                                    ),
                                )
                            )
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
                            lit("CONSO").alias("title"),
                            lit("https://conso.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
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
                "names",
                "emails",
                "phones",
                "address",
                "accounts",
                "actuality",
            )
        )
        df_users_from_orders = (
            self.read(
                path="/home/user/Downloads/bases_new/conso.ru - @bereza_bd./users_from_orders.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("address", array_compact(array(address_udf(col("ADDRESS")))))
            .withColumn("phones", array_compact(array(phone_udf(col("PHONE")))))
            .withColumn("accounts", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "accounts",
                "actuality",
            )
        )

        df = (
            df_users.unionAll(df_users_from_orders)
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    addresses_with_type_udf(col("address"), lit(1))
                ),
            )
            .drop_duplicates(["names"])
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(array_size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(array_size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(array_size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(array_size(col("addresses")) > 0, col("addresses")).otherwise(
                    None
                ),
            )
            .withColumn(
                "accounts",
                when(array_size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
