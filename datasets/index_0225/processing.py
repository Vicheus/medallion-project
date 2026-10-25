from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0225"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0225/raw/morflot.gov.ru - @bereza_bd/morflot_users.csv",
                sep="\t",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("Росморречфлот").alias("title"),
                            lit("https://morflot.gov.ru").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("phones", lit(None))
            .withColumn("works", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("reg_date"), col("last_login_date")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("actuality", lit(None))
            .select("names", "emails", "phones", "accounts", "works", "actuality")
        )

        df_workers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0225/raw/morflot.gov.ru - @bereza_bd/morflot_workers.csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("pass").isNotNull(),
                    array(
                        struct(
                            lit("Росморречфлот").alias("title"),
                            lit("https://morflot.gov.ru").alias("link"),
                            col("login").alias("login"),
                            col("pass").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn(
                "works",
                when(
                    col("comment").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                col("comment"),
                                lit(None),
                                lit(None),
                                lit("Росморречфлот"),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("cdate"), col("mdate")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("names", "emails", "phones", "accounts", "works", "actuality")
        )

        df = df_users.unionAll(df_workers)

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
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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
