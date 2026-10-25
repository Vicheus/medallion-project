from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    collect_list,
    first,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0631"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_agents = (
            self.read(
                path="/home/user/Documents/data/index_0631/raw/eci-spb.ru/agents_data*.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Пользователь")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn(
                "works",
                when(
                    col("Агентство Недвижимости").isNotNull(),
                    work_udf(
                        lit(None),
                        lit(None),
                        lit(None),
                        col("Агентство Недвижимости"),
                        lit(None),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_list(col("works")))).alias(
                    "works"
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("accounts", array())
            .withColumn("raw_metadata", array())
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "works",
                "actuality",
                "accounts",
                "raw_metadata",
            )
        )

        df_contact = (
            self.read(
                path="/home/user/Documents/data/index_0631/raw/eci-spb.ru/contacts.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phone_udf(col("Рабочий телефон")))
            .withColumn("emails", email_udf(col("Рабочий e-mail")))
            .withColumn(
                "works",
                when(
                    col("Компания").isNotNull(),
                    work_udf(
                        col("Должность"),
                        lit(None),
                        lit(None),
                        col("Компания"),
                        lit(None),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата создания"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_list(col("works")))).alias(
                    "works"
                ),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
            )
            .withColumn("accounts", array())
            .withColumn("raw_metadata", array())
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "works",
                "actuality",
                "accounts",
                "raw_metadata",
            )
        )

        df_users = (
            self.read(
                path="/home/user/Documents/data/index_0631/raw/eci-spb.ru/users_from_eci.csv",
                sep="|",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("lastName"), lit(None))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("dateOfBirth"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("works", lit(None))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("PASSWORD").isNotNull(),
                    struct(
                        lit("ЕЦИ").alias("title"),
                        lit("https://eci-spb.ru").alias("link"),
                        col("login").alias("login"),
                        col("password").alias("password_hash"),
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("agency"),
                    col("agency"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("updatedAt"), lit("%d.%m.%Y %H:%M:%S.%fZ")),
            )
            .groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_list(col("works")))).alias(
                    "works"
                ),
                array_compact(array_distinct(collect_list(col("accounts")))).alias(
                    "accounts"
                ),
                array_compact(array_distinct(collect_list(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "works",
                "actuality",
                "accounts",
                "raw_metadata",
            )
        )

        df = df_agents.unionAll(df_contact).unionAll(df_users)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
