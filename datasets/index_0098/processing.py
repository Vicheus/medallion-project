from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    array_distinct,
    size,
    regexp_extract,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0098"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0098/raw/Social-apteka.ru_2023_332k+141k/Social-apteka.ru_(users)_141k.txt",
            sep=",",
            header=True,
        ).replace("NULL", None)

        df_users = (
            df_users.withColumn(
                "names",
                name_parts_udf(col("LAST_NAME"), col("NAME"), col("SECOND_NAME")),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                        )
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    struct(
                        lit("apteka.ru").alias("title"),
                        lit("https://apteka.ru").alias("link"),
                        col("LOGIN").alias("login"),
                        col("PASSWORD").alias("password_hash"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("LAST_LOGIN"), col("DATE_REGISTER")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "accounts",
                "actuality",
            )
        )

        fio_pattern = r"ФИО:\s*([\w\s]+)"
        phone_pattern = r"Телефон:\s*([\+?\d]+)"
        email_pattern = r"Email:\s*([\w\.\-]+@[\w\.\-]+\.\w+)"

        df_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0098/raw/Social-apteka.ru_2023_332k+141k/Social-apteka.ru_(заказы)_332k.txt",
            sep=",",
            header=True,
        ).replace("NULL", None)

        df_orders = (
            df_orders.withColumn(
                "names",
                name_udf(regexp_extract(col("USER_DESCRIPTION"), fio_pattern, 1)),
            )
            .withColumn(
                "emails",
                email_udf(regexp_extract(col("USER_DESCRIPTION"), email_pattern, 1)),
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(
                                regexp_extract(
                                    col("USER_DESCRIPTION"), phone_pattern, 1
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("accounts", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_INSERT"), col("DATE_UPDATE")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .dropDuplicates(["names", "phones", "emails"])
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "accounts",
                "actuality",
            )
        )

        df = df_users.unionAll(df_orders)

        df = df.select(
            "names", "emails", "phones", "birth_date", "accounts", "actuality"
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
