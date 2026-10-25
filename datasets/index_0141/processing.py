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
    concat_ws,
    regexp_replace,
    trim,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0141"

    def parser(self):
        schema_admin = StructType(
            [
                StructField("username", StringType(), True),
                StructField("password", StringType(), True),
                StructField("_c0", StringType(), True),
                StructField("_c1", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("email", StringType(), True),
                StructField("_c2", StringType(), True),
                StructField("_c3", StringType(), True),
                StructField("_c4", StringType(), True),
                StructField("_c5", StringType(), True),
                StructField("_c6", StringType(), True),
                StructField("_c7", StringType(), True),
                StructField("_c8", StringType(), True),
                StructField("_c9", StringType(), True),
                StructField("_c10", StringType(), True),
                StructField("_c11", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("_c12", StringType(), True),
                StructField("_c13", StringType(), True),
                StructField("_c14", StringType(), True),
                StructField("_c15", StringType(), True),
                StructField("_c16", StringType(), True),
                StructField("_c17", StringType(), True),
                StructField("_c18", StringType(), True),
                StructField("_c19", StringType(), True),
                StructField("_c20", StringType(), True),
                StructField("_c21", StringType(), True),
                StructField("_c22", StringType(), True),
                StructField("_c23", StringType(), True),
                StructField("_c24", StringType(), True),
                StructField("_c25", StringType(), True),
                StructField("_c26", StringType(), True),
                StructField("_c27", StringType(), True),
                StructField("_c28", StringType(), True),
                StructField("_c29", StringType(), True),
                StructField("_c30", StringType(), True),
                StructField("_c31", StringType(), True),
                StructField("_c32", StringType(), True),
                StructField("_c33", StringType(), True),
                StructField("_c34", StringType(), True),
                StructField("_c35", StringType(), True),
                StructField("_c36", StringType(), True),
                StructField("_c37", StringType(), True),
                StructField("_c38", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("_c40", StringType(), True),
                StructField("_c41", StringType(), True),
                StructField("_c42", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("_c43", StringType(), True),
                StructField("_c44", StringType(), True),
                StructField("_c45", StringType(), True),
                StructField("_c46", StringType(), True),
                StructField("_c47", StringType(), True),
                StructField("_c48", StringType(), True),
                StructField("_c49", StringType(), True),
                StructField("_c50", StringType(), True),
                StructField("_c51", StringType(), True),
                StructField("_c52", StringType(), True),
            ]
        )
        df_admin = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0141/raw/aslife.ru/Администрация.csv",
                sep="\t",
                header=False,
                schema=schema_admin,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("АльфаСтрахование-Жизнь").alias("title"),
                            lit("https://aslife.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("address", array())
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", lit(None))
            .select(
                "names", "phones", "emails", "accounts", "address", "birth_date", "sex"
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0141/raw/aslife.ru/Пользователи.csv",
                sep="\t",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn(
                "username",
                trim(
                    regexp_replace(
                        "username", r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", ""
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("АльфаСтрахование-Жизнь").alias("title"),
                            lit("https://aslife.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(address_udf(concat_ws(" ", col("city"), col("address"))))
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("sex")))
            .select(
                "names", "phones", "emails", "accounts", "address", "birth_date", "sex"
            )
        )

        df_cases = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0141/raw/aslife.ru/Обращения_2.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn("accounts", array())
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("city"))))),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", lit(None))
            .select(
                "names", "phones", "emails", "accounts", "address", "birth_date", "sex"
            )
        )

        df = df_admin.unionAll(df_cases).unionAll(df_users).drop_duplicates()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
            "names", "emails", "birth_date", "address", "accounts", "phones", "sex"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
