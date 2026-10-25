from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0547"

    def parser(self):
        df_authors = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0547/raw/justclick.ru authors.csv",
                sep="|",
                header=True,
            )
            .filter(col("ФИО") != "Дорогой Друг")
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", array_compact(array(phone_udf(col("ТЕЛЕФОН")))))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("address", lit(None))
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("JustClick. Воронки продаж для бизнеса").alias("title"),
                        lit("https://justclick.ru/").alias("link"),
                        col("НИК").alias("login"),
                        col("ПАРОЛЬ-Хеш").alias("password_hash"),
                    )
                ),
            )
            .withColumn("address", lit(None))
            .select("names", "phones", "emails", "address", "accounts")
        )

        df_buyers = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0547/raw/justclick.ru buyers.csv",
                sep="|",
                header=True,
            )
            .withColumn(
                "ФИО", concat_ws(" ", col("ИМЯ"), col("ФАМИЛИЯ"), col("ОТЧЕСТВО"))
            )
            .filter(col("ФИО") != "Дорогой Друг")
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", array_compact(array(phone_udf(col("ТЕЛЕФОН")))))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("СТРАНА"), col("ГОРОД"), col("АДРЕС"))),
            )
            .withColumn("accounts", array())
            .select("names", "phones", "emails", "address", "accounts")
        )

        df_subscribes = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0547/raw/justclick.ru subscribes.csv",
                sep="|",
                header=True,
            )
            .filter(col("ИМЯ") != "Дорогой Друг")
            .withColumn("names", name_udf(col("ИМЯ")))
            .withColumn(
                "phones",
                array_compact(
                    array(phone_udf(col("ТЕЛЕФОН")), phone_udf(col("СОТОВЫЙ")))
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("address", address_udf(col("ГОРОД")))
            .withColumn("accounts", array())
            .select("names", "phones", "emails", "address", "accounts")
        )

        df = df_buyers.unionAll(df_authors).unionAll(df_subscribes)

        df = df.filter(col("names") != "Дорогой Друг")

        df = df.drop_duplicates(["emails"])

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
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
