from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    size,
    struct,
    first,
    coalesce,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0073"

    def parser(self):
        df_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0073/raw/maksavit.ru_09.2024_(1.023.791).csv",
            sep="\t",
            header=True,
        )

        df_1 = (
            df_1.withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%d.%m.%Y")))
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("hash_passwd").isNotNull(),
                    array(
                        struct(
                            lit("Максавит").alias("title"),
                            lit("https://maksavit.ru").alias("link"),
                            col("email").alias("login"),
                            col("hash_passwd").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("last_login"), col("date_register")),
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

        df_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0073/raw/maksavit.ru_09.2024_orders.csv",
            sep="\t",
            header=True,
        )
        df_2 = (
            df_2.withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("accounts", array())
            .withColumn("actuality", lit(None))
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

        df = df_1.unionAll(df_2)

        df = df.groupBy(["phones", "emails"]).agg(
            collect_set("names").alias("names"),
            collect_set("accounts").alias("accounts"),
            first("sex").alias("sex"),
            first("birth_date").alias("birth_date"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
