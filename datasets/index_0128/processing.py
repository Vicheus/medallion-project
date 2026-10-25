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
from parsetron.sections.work.udfs import work_udf
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
    dataset_code_name: str = "index_0128"

    def parser(self):
        df_1 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0128/raw/preprocessed/users_info_1_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0128/raw/preprocessed/users_info_2_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = df_2.join(df_1, on="USER_ID", how="left")

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_udf(col("name2")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("Магазин игрушек Лимпопо").alias("title"),
                            lit("https://limpopo56.ru/").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    (col("company").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                lit(None),
                                lit(None),
                                lit(None),
                                col("company"),
                                col("company_addr"),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "works",
                "accounts",
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
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "works",
            "accounts",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
