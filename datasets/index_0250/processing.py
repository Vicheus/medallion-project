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
)

from parsetron import Parsetron
from parsetron.sections.financials.udfs import (
    financial_card_number_udf,
    financial_date_expire_udf,
)
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0250"

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0250/raw/AlfaBank 2024_gold_client.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("FullName")))
            .withColumn("birth_date", birth_date_udf(col("BDay"), lit("%Y-%m-%d")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("Email")), email_udf(col("Email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Phone")),
                            phone_udf(col("Phone2")),
                            phone_udf(col("Phone3")),
                            phone_udf(col("Phone4")),
                            phone_udf(col("Phone5")),
                            phone_udf(col("Phone6")),
                            phone_udf(col("Phone7")),
                            phone_udf(col("Phone8")),
                        )
                    )
                ),
            )
            .withColumn("credit_card_num", financial_card_number_udf(col("CreditCard")))
            .withColumn(
                "financials",
                when(
                    col("credit_card_num").isNotNull(),
                    array(
                        struct(
                            lit("Альфа Банк").alias("title"),
                            col("credit_card_num").alias("card_number"),
                            lit(None).alias("date_issue"),
                            financial_date_expire_udf(col("CardExpiration")).alias(
                                "date_expire"
                            ),
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "phones", "birth_date", "financials")
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
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
