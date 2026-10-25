from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
)
from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0426"

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0426/raw/investprojects.info - @StormBaseAdapter/Пользователи.txt",
                sep=",",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "works",
                when(
                    col("position").isNotNull(),
                    work_udf(
                        col("position"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .select("names", "phones", "emails", "address", "works", "actuality")
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0426/raw/investprojects.info - @StormBaseAdapter/Клиенты из другого источника.txt",
                sep=",",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", lit(None))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("works", lit(None))
            .withColumn("actuality", lit(None))
            .select("names", "phones", "emails", "address", "works", "actuality")
        )

        df = df_users_1.unionAll(df_users_2)
        df = df.drop_duplicates(["names", "emails", "phones"])

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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "works",
                when(col("works").isNotNull(), array(col("works"))).otherwise(None),
            )
        )
        df = df.select("names", "phones", "emails", "address", "works", "actuality")

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("address").isNotNull()
                | col("phones").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
