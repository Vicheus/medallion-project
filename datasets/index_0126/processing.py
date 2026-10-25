from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    size,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    name_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0126"

    def parser(self):
        df_1 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0126/raw/preprocessed/users_info_1_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0126/raw/preprocessed/users_info_2_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = df_1.join(df_2, on="USER_ID", how="left")

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_udf(col("name3")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email")),
                            email_udf(col("email2")),
                            email_udf(col("email3")),
                        )
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn(
                "accounts",
                array(
                    when(
                        col("username").isNotNull() & col("password_hash").isNotNull(),
                        struct(
                            lit("Официальный сайт компании Нанософт").alias("title"),
                            lit("https://nanocad.ru/").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address")),
                            address_udf(col("send_address")),
                            address_udf(col("address2")),
                        )
                    )
                ),
            )
            .select(
                "names", "emails", "phones", "address", "sex", "birth_date", "accounts"
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
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
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names", "emails", "phones", "address", "sex", "birth_date", "accounts"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
