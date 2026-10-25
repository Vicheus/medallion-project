from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0096"

    def parser(self):
        df_user_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0096/raw/sberbank.ru_SberPravo_2023_116k/SberPravo_user.csv",
            sep="\t",
            header=True,
        )
        df_user_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0096/raw/sberbank.ru_SberPravo_2023_116k/SberPravo_user2.csv",
            sep="\t",
            header=True,
        )
        df_userphone = self.read(
            path="/media/user/SAMSUNG/Databases/index_0096/raw/sberbank.ru_SberPravo_2023_116k/SberPravo_userphone.csv",
            sep="\t",
            header=True,
        )

        df_user_1 = (
            df_user_1.withColumn("user_id", col("id"))
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull(),
                    struct(
                        lit("СберПраво").alias("title"),
                        lit("https://sberpravo.ru").alias("link"),
                        col("username").alias("login"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("created_timestamp"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
            .select("names", "emails", "birth_date", "accounts", "user_id", "actuality")
        )

        df_user_2 = (
            df_user_2.withColumn("user_id", col("id"))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("accounts", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("registration_date"), lit("%Y-%m-%d")),
            )
            .select("names", "emails", "birth_date", "accounts", "user_id", "actuality")
        )

        df_users = df_user_1.unionAll(df_user_2)

        df_userphone = df_userphone.withColumn("user_id", col("users_id")).withColumn(
            "phones", phone_udf(col("phone"))
        )
        df = df_users.join(df_userphone, "user_id", "left")

        df = df.select(
            "names", "emails", "phones", "birth_date", "accounts", "actuality"
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

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
                when(col("accounts").isNotNull(), array(col("accounts"))).otherwise(
                    None
                ),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
