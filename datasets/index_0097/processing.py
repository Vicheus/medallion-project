from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_distinct,
    array_compact,
    concat_ws,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf, work_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    name_parts_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0097"

    def parser(self):
        df_employee = self.read(
            path="/media/user/SAMSUNG/Databases/index_0097/raw/sberbank_sberlogistics.ru_02.2023_1,3kk/sberbank.ru_logistic_employee.csv",
            sep="\t",
            header=True,
        )

        df_employee = (
            df_employee.withColumn(
                "names",
                array_distinct(
                    array_compact(
                        array(name_udf(col("name")), name_udf(col("displayname")))
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("mail")))))
            )
            .withColumn("phones", phone_udf(col("homephone")))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    work_udf(
                        col("title"),
                        work_date_udf(col("whencreated"), lit("2020-07-28")),
                        lit(None),
                        concat_ws(" ", col("company"), col("department")),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn("accounts", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("lastlogontimestamp"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("directreports"),
                    df_employee["directreports"],
                    lit("manager"),
                    df_employee["manager"],
                    lit("memberof"),
                    df_employee["memberof"],
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "accounts",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0097/raw/sberbank_sberlogistics.ru_02.2023_1,3kk/sberlogistics.ru_users.csv",
            sep="\t",
            header=True,
        )
        df_users = (
            df_users.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), lit(None)
                            )
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
                            email_udf(col("package_notify_email")),
                            email_udf(col("finance_notify_email")),
                            email_udf(col("support_notify_email")),
                        )
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("birth_date", birth_date_udf(col("birth_at"), lit("%Y-%m-%d")))
            .withColumn("works", lit(None))
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("email").isNotNull(),
                    struct(
                        lit("СберЛогистика").alias("title"),
                        lit("https://sberlogistics.ru").alias("link"),
                        col("password").alias("password_hash"),
                        col("email").alias("login"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("last_visited_at"), col("registered_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "accounts",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_employee.unionAll(df_users)

        df = df.select(
            "names",
            "emails",
            "phones",
            "birth_date",
            "accounts",
            "works",
            "actuality",
            "raw_metadata",
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "works",
                when(col("works").isNotNull(), array(col("works"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
