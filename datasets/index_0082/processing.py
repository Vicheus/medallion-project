from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    when,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    children_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0082"
    important_columns_for_filtering: str = "phones,emails,address"
    write_filtered_rows: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_clients = self.read(
            path="/media/user/SAMSUNG/Databases/index_0082/raw/preprocessed/randevouz_clients_preprocessed.csv",
            sep=",",
            header=True,
        )
        df_clients = (
            df_clients.replace("- -", "")
            .replace("- ", "")
            .replace("- Отсутствует", "")
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email_2")))
                    )
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull()
                    | col("fb_id").isNotNull()
                    | col("tw_id").isNotNull()
                    | col("od_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                struct(
                                    lit("ВКонтакте").alias("title"),
                                    col("vk_id").alias("id"),
                                ),
                            ).otherwise(None),
                            when(
                                col("fb_id").isNotNull(),
                                struct(
                                    lit("Facebook").alias("title"),
                                    col("fb_id").alias("id"),
                                ),
                            ).otherwise(None),
                            when(
                                col("tw_id").isNotNull(),
                                struct(
                                    lit("Twitter").alias("title"),
                                    col("tw_id").alias("id"),
                                ),
                            ).otherwise(None),
                            when(
                                col("od_id").isNotNull(),
                                struct(
                                    lit("Одноклассники").alias("title"),
                                    col("od_id").alias("id"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Rendez-Vous").alias("title"),
                            lit("https://www.rendez-vous.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                            lit(None).alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn("address", lit(None))
            .withColumn("works", lit(None))
            .withColumn("children", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "birth_date",
                "children",
                "sex",
                "socials",
                "accounts",
            )
        )

        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0082/raw/preprocessed/users/*.csv",
            sep=",",
            header=True,
        )
        df_users = (
            df_users.replace("- -", "")
            .replace("- ", "")
            .replace("- Отсутствует", "")
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", lit(None))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("socials", array())
            .withColumn(
                "accounts",
                when(
                    col("client_card").isNotNull(),
                    array(
                        struct(
                            lit("Rendez-Vous").alias("title"),
                            lit("https://www.rendez-vous.ru").alias("link"),
                            lit(None).alias("login"),
                            lit(None).alias("password_hash"),
                            col("client_card").alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("job").isNotNull(),
                    array(
                        work_udf(
                            col("job"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("address", address_udf(col("city")))
            .withColumn("children", children_udf(col("children")))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "works",
                "birth_date",
                "children",
                "sex",
                "socials",
                "accounts",
            )
        )

        df = df_clients.unionAll(df_users)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "birth_date",
            "sex",
            "children",
            "accounts",
        )

        df.show(n=100, truncate=False)
        print(f"df size: {df.count()}")

        df = df.drop_duplicates(["names", "emails", "phones"])
        print(f"df size: {df.count()}")

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
