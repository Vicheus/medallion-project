from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    length,
    struct,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0011"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0011/raw/Kari_club_raw.csv",
            sep=";",
            header=True,
        )

        df = df.dropDuplicates(
            ["phone_number", "email", "last_name", "first_name", "patronymic_name"]
        )

        df = df.withColumn(
            "names",
            when(
                (length(col("first_name")) > 2)
                & (length(col("last_name")) > 2)
                & (length(col("patronymic_name")) > 2),
                concat_ws(
                    " ", col("last_name"), col("first_name"), col("patronymic_name")
                ),
            ).otherwise(None),
        ).withColumn(
            "address",
            when(
                (col("region") == col("city")) | (col("city").isNull()),
                coalesce(col("region"), col("city")),
            ).otherwise(concat_ws(", ", col("region"), col("city"))),
        )

        df = (
            df.withColumn("names", name_udf(col("names")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("Kari Club").alias("title"),
                        lit("https://kari.com/").alias("link"),
                        col("card_number").alias("client_card_number"),
                    )
                ),
            )
        ).withColumn(
            "actuality", actuality_date_udf(col("timestamp"), lit("%Y-%m-%d %H:%M:%S"))
        )

        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "birth_date",
            "sex",
            "accounts",
            "actuality",
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), col("accounts")).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
