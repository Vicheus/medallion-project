from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    struct,
    trim,
    size,
    array_distinct,
)
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.financials.udfs import (
    financial_date_issue_udf,
    financial_date_expire_udf,
)
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0010"
    output_file_count: int = 10
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,phones,documents,financials"

    def format_and_clean_df(self, df):
        for column in df.columns:
            df = df.withColumn(column, trim(col(column)))
            df = df.withColumn(
                column, when(col(column) == "", lit(None)).otherwise(col(column))
            )
        df = df.replace("NULL", None)

        id_regex_pattern = "^[0-9]+$"
        df = df.filter(col("icusid").rlike(id_regex_pattern))

        return df

    def parser(self):
        df_main = self.read(
            path="/media/user/SAMSUNG/Databases/index_0010/raw/cusmain.csv",
            sep="\t",
            header=True,
        )
        df_contact = self.read(
            path="/media/user/SAMSUNG/Databases/index_0010/raw/cuscontact.csv",
            sep="\t",
            header=True,
        )
        df_card = self.read(
            path="/media/user/SAMSUNG/Databases/index_0010/raw/cardmain.csv",
            sep="\t",
            header=True,
        )

        df_main = self.format_and_clean_df(df_main)
        df_contact = self.format_and_clean_df(df_contact)

        df_card = self.format_and_clean_df(df_card)
        df_card = df_card.dropDuplicates(["chashpan"])

        df_card = (
            df_card.withColumn("card_number", col("cmaskedpan"))
            .withColumn("card_number_hash", col("chashpan"))
            .withColumn("card_date_issue", financial_date_issue_udf(col("dissuedate")))
            .withColumn(
                "card_date_expiry", financial_date_expire_udf(col("dexpirydate"))
            )
        )

        df_card.show(n=50)

        df_contact = df_contact.withColumn(
            "email",
            when(col("icontacttype") == "6", email_udf(col("cvalue"))).otherwise(None),
        ).withColumn(
            "phone",
            when(col("icontacttype") != "6", phone_udf(col("cvalue"))).otherwise(None),
        )
        df_contact = df_contact.select("icusid", "email", "phone").alias("df_contact")

        df = df_main.join(df_contact, "icusid", "outer").join(df_card, "icusid", "left")

        df = (
            df.withColumn("names", name_udf(col("ccusfullname")))
            .withColumn("sex", sex_udf(col("cgender")))
            .withColumn(
                "birth_date", birth_date_udf(col("dbirthdate"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(phone_udf(col("cmainphonenum")), phone_udf(col("phone")))
                    )
                ),
            )
            .withColumn("emails", col("email"))
            .withColumn(
                "documents",
                when(
                    col("csnils").isNotNull() | col("ccusinn").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("csnils").isNotNull(),
                                    document_udf(
                                        lit("снилс"),
                                        col("csnils"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ),
                                when(
                                    col("ccusinn").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("ccusinn"),
                                        lit(None),
                                        lit(None),
                                        col("ctaxagencyname"),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ),
                                when(
                                    col("ccuskpp").isNotNull(),
                                    document_udf(
                                        lit("кпп"),
                                        col("ccuskpp"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("icusid").isNotNull(),
                    array(
                        struct(
                            lit("MTS bank app").alias("title"),
                            lit("https://www.mtsbank.ru/").alias("link"),
                            col("icusid").alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "relationship",
                when(col("cmaritalstatus") == "NOTMARRIED", 1)
                .when(col("cmaritalstatus") == "MARRIED", 0)
                .when(col("cmaritalstatus") == "WIDOWED", 2)
                .when(col("cmaritalstatus") == "DIVORCED", 3)
                .otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull(),
                    array(
                        struct(
                            lit("МТС Банк").alias("title"),
                            col("card_number").alias("card_number"),
                            col("card_date_issue").alias("date_issue"),
                            col("card_date_expiry").alias("date_expire"),
                            col("card_number_hash").alias("comment"),
                        )
                    ),
                ).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "sex",
            "birth_date",
            "phones",
            "emails",
            "relationship",
            "documents",
            "accounts",
            "financials",
        )
        df = df.drop_duplicates(["names"])
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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
        )
        df = df.drop_duplicates(["names"])

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
