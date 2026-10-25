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
    split,
    struct,
    slice,
)


from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    raw_metadata_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0648"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_1 = (
            self.read(
                path="/home/user/Documents/data/index_0648/raw/rjb_ru/контактн_лиц_компаний_utf8.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(split(col("Контактное лицо"), ",")[0]))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Телефон")),
                            phone_udf(col("Телефон 2")),
                            phone_udf(col("Телефон 3")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("Город")))
            .withColumn("accounts", lit(None))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Сфера деятельности"),
                    col("Сфера деятельности"),
                    lit("Юрлицо-работодатель"),
                    col("Юридическое лицо"),
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "raw_metadata")
        )

        df_2 = (
            self.read(
                path="/home/user/Documents/data/index_0648/raw/rjb_ru/контакт_лица_компаний_2_utf8.txt",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(split(col("Контактное лицо"), ",")[0]))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Телефон"))))),
            )
            .withColumn("address", lit(None))
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
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Юрлицо-работодатель"), col("Юрлицо-работодатель")
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "raw_metadata")
        )

        df = df_1.unionAll(df_2)

        df_with_emails = df.filter(col("emails").isNotNull())
        df_without_emails = (
            df.filter(col("emails").isNull())
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("accounts", array_compact(array(col("accounts"))))
            .withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))
            .select("names", "emails", "phones", "address", "accounts", "raw_metadata")
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
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "raw_metadata")
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
                "raw_metadata",
                when(
                    size(array_distinct(array_compact(col("raw_metadata")))) > 0,
                    array_distinct(array_compact(col("raw_metadata"))),
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
            .withColumn(
                "raw_metadata",
                when(
                    size(col("raw_metadata")) > 3, slice("raw_metadata", 1, 3)
                ).otherwise(col("raw_metadata")),
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
