from pyspark import StorageLevel
from pyspark.sql.functions import col, lit, concat, substring, when, array, struct, size

from parsetron import Parsetron
from parsetron.sections.financials.udfs import financial_card_number_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0170"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0170/raw/parsed_data.csv",
                sep=",",
                header=True,
            )
            .drop_duplicates()
            .filter(col("Cardholder Name") != "CARDHOLDER NAME")
            .withColumn(
                "formatted_date",
                concat(
                    substring(col("Expiration"), 1, 4),
                    lit("-"),
                    substring(col("Expiration"), 5, 2),
                    lit("-01"),
                ),
            )
            .withColumn("card_number", financial_card_number_udf(col("PAN")))
            .withColumn("ip", ip_address_udf(col("IP")))
            .withColumn("names", name_udf(col("Cardholder Name")))
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull(),
                    array(
                        struct(
                            lit("СберБанк").alias("title"),
                            col("card_number").alias("card_number"),
                            lit(None).alias("date_issue"),
                            col("formatted_date").alias("date_expire"),
                            lit(None).alias("comment"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(struct(col("ip").alias("ip"), lit(None).alias("date"))),
                ),
            )
            .select("names", "ips", "financials")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "financials",
                when(size(col("financials")) > 0, col("financials")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & col("financials").isNotNull()
            & col("ips").isNotNull()
        )
        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
