from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0031"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0031/raw/mknc.ru_full/mknc.ru2.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(col("display_name")))
            .withColumn("phones", phone_udf(col("custom1")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender_id")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("pass").isNotNull(),
                    array(
                        struct(
                            lit("МКНЦ им. А.С.Логинова").alias("title"),
                            lit("https://mknc.ru/").alias("link"),
                            col("username").alias("login"),
                            col("pass").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("last_online_date"), col("last_login_date")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "sex",
                "birth_date",
                "accounts",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
            "names", "emails", "phones", "sex", "birth_date", "accounts", "actuality"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
