from pyspark.sql.functions import (
    when,
    col,
    lit,
    regexp_replace,
    struct,
    array,
    array_compact,
    array_distinct,
    size,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    address_udf,
    phone_udf,
    raw_metadata_udf,
    actuality_date_udf,
    name_parts_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0429"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,phones"

    def parser(self):
        df_tickets = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0429/raw/re-store.ru - @StormBaseAdapter/Билеты.csv",
                sep=",",
            )
            .replace("\t", "")
            .withColumn("names", name_udf(regexp_replace(col("name"), "\t", "")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(regexp_replace(col("email"), "\t", "")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(regexp_replace(col("phone"), "\t", "")))
                    )
                ),
            )
            .withColumn("address", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    regexp_replace(col("date"), "\t", ""), lit("%Y-%m-%d %H:%M;%S")
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .withColumn("accounts", array())
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "address",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0429/raw/re-store.ru - @StormBaseAdapter/Пользователи.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", "")
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("EMAIL")))))
            )
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
            .withColumn("address", address_udf(col("PERSONAL_CITY")))
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("restore — Сеть фирменных магазинов техники").alias(
                                "title"
                            ),
                            lit("https://www.re-store.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
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
                "address",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_tickets.unionAll(df_users)

        df = df.drop_duplicates(["phones", "emails"])

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
