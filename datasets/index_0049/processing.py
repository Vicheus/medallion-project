from pyspark.sql.functions import (
    array_distinct,
    when,
    col,
    lit,
    array,
    array_compact,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0049"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0049/raw/dobro.ru_2022_648k.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_Name"), col("Last_name"), col("Middle_name")),
            )
            .withColumn("address", address_udf(col("Region")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(
                        array(email_udf(col("email2")), email_udf(col("email")))
                    )
                ),
            )
            .withColumn("birth_date", email_udf(col("Birthday")))
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("hash_password").isNotNull(),
                    array(
                        struct(
                            lit("Добро.рф").alias("title"),
                            lit("https://dobro.ru").alias("link"),
                            col("email").alias("login"),
                            col("hash_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )
        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "accounts",
            "birth_date",
            "actuality",
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
