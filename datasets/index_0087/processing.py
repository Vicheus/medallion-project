from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0087"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0087/raw/volgofarm_users_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_users = (
            df_users.withColumn("names", name_udf("name"))
            .withColumn("phones", phone_udf("phone"))
            .withColumn("emails", email_udf("email"))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Аптека Волгофарм").alias("title"),
                            lit("https://volgofarm.ru").alias("link"),
                            col("login").alias("login"),
                            col("id_user").alias("id"),
                            col("password").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("work_place").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("work_place"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "accounts",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0087/raw/volgofarm.ru_16.05.2023_219k/Заказы.csv",
            sep=";",
            header=True,
        )
        df_orders = (
            df_orders.withColumn("names", name_udf("name_user"))
            .withColumn("phones", phone_udf("phone"))
            .withColumn("emails", email_udf("email"))
            .withColumn("accounts", lit(None))
            .withColumn("works", lit(None))
            .withColumn("actuality", actuality_date_udf(col("date"), lit("%d.%m.%Y")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("apteka"),
                    df_orders["apteka"],
                    lit("summa"),
                    df_orders["summa"],
                    lit("comment"),
                    df_orders["comment"],
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "accounts",
                "works",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_users.unionAll(df_orders)

        df = df.select(
            "names",
            "emails",
            "phones",
            "accounts",
            "works",
            "actuality",
            "raw_metadata",
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
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
