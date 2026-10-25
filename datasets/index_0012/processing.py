from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    array_distinct,
    flatten,
    collect_list,
    first,
    collect_set,
    array_compact,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.financials.udfs import (
    financial_date_expire_udf,
    financial_card_number_udf,
)
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 40
    dataset_code_name: str = "index_0012"
    calc_completeness: bool = False
    important_columns_for_filtering: str = "emails,phones,financials"
    write_filtered_rows: bool = True

    def parser(self):
        latin_cyrillic_pattern = ".*[A-Za-z].*[А-Яа-яЁё]|[А-Яа-яЁё].*[A-Za-z].*"

        df_clients = self.read(
            path="/media/user/SAMSUNG/Databases/index_0012/raw/clients.csv",
            sep="\t",
            header=True,
        )
        df_contacts = self.read(
            path="/media/user/SAMSUNG/Databases/index_0012/raw/contacts.csv",
            sep="\t",
            header=True,
        )
        df_cards = self.read(
            path="/media/user/SAMSUNG/Databases/index_0012/raw/cards.csv",
            sep="\t",
            header=True,
        )

        df_clients = (
            df_clients.filter(col("UK").isNotNull() & (col("UK") != "0"))
            .withColumn("names", name_udf(col("CLIENT_NAME")))
            .withColumn(
                "birth_date", birth_date_udf(col("BIRTH_DATE"), lit("%Y-%m-%d"))
            )
        )

        df_clients = (
            df_clients.groupby("UK")
            .agg(
                when(size(collect_set("names")) > 0, collect_set("names"))
                .otherwise(None)
                .alias("names"),
                first("birth_date").alias("birth_date"),
            )
            .alias("df_clients")
        )

        df_clients = df_clients.withColumn(
            "names", expr(f"filter(names, x -> NOT x rlike '{latin_cyrillic_pattern}')")
        )

        df_clients = df_clients.filter(col("names").isNotNull())
        df_clients = df_clients.select("UK", "names", "birth_date")

        df_contacts = (
            df_contacts.filter(col("CLIENT_UK").isNotNull() & (col("CLIENT_UK") != "0"))
            .withColumn(
                "email",
                when(
                    col("CLIENTCONTACT_CCODE").contains("@"), col("CLIENTCONTACT_CCODE")
                ),
            )
            .withColumn(
                "phone",
                when(
                    ~col("CLIENTCONTACT_CCODE").contains("@"),
                    col("CLIENTCONTACT_CCODE"),
                ),
            )
        )

        df_contacts = df_contacts.withColumn(
            "phones", phone_udf(col("phone"))
        ).withColumn("emails", email_udf(col("email")))

        df_contacts = df_contacts.select("CLIENT_UK", "phones", "emails")

        df_contacts = (
            df_contacts.groupby("CLIENT_UK")
            .agg(
                when(size(collect_set("phones")) > 0, collect_set("phones"))
                .otherwise(None)
                .alias("phones"),
                when(size(collect_set("emails")) > 0, collect_set("emails"))
                .otherwise(None)
                .alias("emails"),
            )
            .alias("df_contacts")
        )

        df_cards = (
            df_cards.filter(
                col("CLIENT_OWNER_UK").isNotNull() & (col("CLIENT_OWNER_UK") != "0")
            )
            .withColumn(
                "CARDNUM_CCODE", financial_card_number_udf(col("CARDNUM_CCODE"))
            )
            .withColumn("EXPIRE_DATE", financial_date_expire_udf(col("EXPIRE_DATE")))
        )

        df_cards = df_cards.filter(
            col("CARDNUM_CCODE").isNotNull() & col("EXPIRE_DATE").isNotNull()
        )

        df_cards = df_cards.withColumn(
            "financials",
            array(
                struct(
                    lit("Альфа-Банк").alias("title"),
                    col("CARDNUM_CCODE").alias("card_number"),
                    col("EXPIRE_DATE").alias("card_date_expiry"),
                )
            ),
        ).withColumn(
            "raw_metadata",
            raw_metadata_udf(lit("ACCOUNT_NUMBER"), df_cards["ACCOUNT_NUMBER"]),
        )

        df_cards = df_cards.select("CLIENT_OWNER_UK", "financials", "raw_metadata")
        df_cards = (
            df_cards.groupby("CLIENT_OWNER_UK")
            .agg(
                when(
                    size(array_distinct(flatten(collect_list("financials")))) > 0,
                    array_distinct(flatten(collect_list("financials"))),
                )
                .otherwise(None)
                .alias("financials"),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .alias("df_cards")
        )

        df = (
            df_clients.join(
                df_cards, df_cards["CLIENT_OWNER_UK"] == df_clients["UK"], "left"
            )
            .join(df_contacts, df_contacts["CLIENT_UK"] == df_clients["UK"], "left")
            .drop("CLIENT_UK", "UK")
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0,
                    array_distinct(array_compact(col("names"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(col("financials"))) > 0,
                    array_compact(col("financials")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )

        df = df.select(
            "names", "birth_date", "emails", "phones", "financials", "raw_metadata"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
