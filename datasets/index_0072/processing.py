from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    concat,
    struct,
    from_unixtime,
    array_compact,
    array_distinct,
    array,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0072"

    def parser(self):
        df = self.read(path="infoflot_preprocessed.csv", sep=",", header=True)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(
                    from_unixtime("birthday", "yyyy-MM-dd"), lit("%Y-%m-%d")
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address_legal")),
                            address_udf(col("address_home")),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("passport_series").isNotNull()
                    & col("passport_number").isNotNull(),
                    document_udf(
                        lit(None),
                        concat(col("passport_series"), col("passport_number")),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("passenger_bonus_card").isNotNull()
                    & col("user_id").isNotNull(),
                    array(
                        struct(
                            lit("Инфофлот").alias("title"),
                            lit("https://www.infoflot.com").alias("link"),
                            col("user_id").alias("id"),
                            col("passenger_bonus_card").alias("client_card_number"),
                        )
                    ),
                ),
            )
        )

        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "birth_date",
            "documents",
            "accounts",
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(col("documents").isNotNull(), array(col("documents"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("emails")).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
