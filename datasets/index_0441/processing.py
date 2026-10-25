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
    length,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0441"

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0441/raw/kant/preprocessed/users_1.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("LOGIN")), email_udf(col("EMAIL")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("PERSONAL_ZIP"),
                        col("PERSONAL_CITY"),
                        col("PERSONAL_STREET"),
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Спортивные магазины КАНТ").alias("title"),
                            lit("https://www.kant.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("financials", array())
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0441/raw/kant/preprocessed/users_2.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("address", lit(None))
            .withColumn("accounts", array())
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn("financials", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df_users_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0441/raw/kant/preprocessed/users_3.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("index"),
                        col("city"),
                        col("street"),
                        col("building"),
                        col("flat"),
                    )
                ),
            )
            .withColumn("accounts", array())
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn("financials", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df_users_from_cards = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0441/raw/kant/preprocessed/cards.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("cardholder")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", array())
            .withColumn("phones", array())
            .withColumn("address", lit(None))
            .withColumn("accounts", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("amount"),
                    col("amount"),
                    lit("number"),
                    col("number"),
                    lit("cardtype"),
                    col("cardtype"),
                ),
            )
            .withColumn(
                "financials",
                array(
                    when(
                        col("PAN").isNotNull()
                        & (col("PAN") != "")
                        & (col("PAN") != "NULL"),
                        struct(
                            lit("Номер банковской карты").alias("title"),
                            col("PAN").alias("card_number"),
                        ),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("datetime"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "financials",
                "raw_metadata",
                "actuality",
            )
        )

        df = (
            df_users_1.unionAll(df_users_2)
            .unionAll(df_users_3)
            .unionAll(df_users_from_cards)
        )

        df = df.drop_duplicates(["names", "phones"])

        df = df.filter(
            (length(col("names")) < 50)
            & ~(
                col("names").contains("test")
                | col("names").contains("TEST")
                | col("names").contains("тест")
                | col("names").contains("Тест")
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
