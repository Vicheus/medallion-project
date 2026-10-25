from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0130"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0130/raw/detskiyMir@StormInDataBase/detskiy_mir.csv",
            sep="\t",
            header=True,
        )

        df = (
            (
                df.withColumn("names", name_udf(col("name")))
                .withColumn("emails", email_udf(col("email")))
                .withColumn("phones", phone_udf(col("phone")))
                .withColumn(
                    "accounts",
                    when(
                        col("bonus_card").isNotNull(),
                        array(
                            struct(
                                lit("Карта лояльности Детский мир").alias("title"),
                                col("bonus_card").alias("client_card_number"),
                            )
                        ),
                    ).otherwise(None),
                )
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("user_agent"), df["user_agent"])
            )
        )

        df = df.select(
            "names", "phones", "emails", "accounts", "actuality", "raw_metadata"
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = df.select(
            "names", "emails", "phones", "accounts", "actuality", "raw_metadata"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
