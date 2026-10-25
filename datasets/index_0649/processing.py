from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    size,
    array_distinct,
    collect_set,
    flatten,
    struct,
    slice,
    lower,
    first,
)

from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0649"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.RU

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0649/raw/пользователи_*.txt",
                sep="|",
                header=True,
            )
            .filter(lower(col("Гражданство")).isin(["ru", "рф"]))
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Телефон")), phone_udf(col("Телефон2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "accounts",
                when(
                    col("Логин").isNotNull() & col("Пароль").isNotNull(),
                    struct(
                        lit("RJB.ru").alias("title"),
                        col("Логин").alias("login"),
                        col("Пароль").alias("password"),
                    ),
                ),
            )
            .select("names", "birth_date", "emails", "phones", "address", "accounts")
        )

        df_with_emails = df.filter(col("emails").isNotNull())
        df_without_emails = (
            df.filter(col("emails").isNull())
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("accounts", array_compact(array(col("accounts"))))
            .select("names", "birth_date", "emails", "phones", "address", "accounts")
        )

        df_with_emails = (
            df_with_emails.groupBy(["names", "emails"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("accounts")))).alias(
                    "accounts"
                ),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .select("names", "birth_date", "emails", "phones", "address", "accounts")
        )

        df = df_with_emails.unionAll(df_without_emails)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_distinct(array_compact(col("phones")))) > 0,
                    array_distinct(array_compact(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_distinct(array_compact(col("address")))) > 0,
                    array_distinct(array_compact(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_distinct(array_compact(col("accounts")))) > 0,
                    array_distinct(array_compact(col("accounts"))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 3, slice("phones", 1, 3)).otherwise(
                    col("phones")
                ),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 3, slice("accounts", 1, 3)).otherwise(
                    col("accounts")
                ),
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
