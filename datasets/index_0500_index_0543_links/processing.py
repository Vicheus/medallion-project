from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    array_compact,
    array_distinct,
    array,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_index_0543_links"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0543/raw/dеІtа.ru - @StormBaseAdapter/users.csv",
            sep="\t",
            header=True,
        ).replace("\\N", None)

        df_users = (
            df_users.filter(
                col("full_name").isNull()
                & col("mphone").isNotNull()
                & col("email").isNotNull()
            )
            .withColumn("phones", array_compact(array(phone_udf(col("mphone")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("phones", "emails", "address", "actuality")
        )

        df_support = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0543/raw/dеІtа.ru - @StormBaseAdapter/support.csv",
            sep="\t",
            header=True,
        ).replace("\\N", None)

        df_support_clients = (
            df_support.filter(
                col("contact_name").isNull()
                & (col("phone").isNotNull() | col("mphone").isNotNull())
                & col("email").isNotNull()
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("mphone")))
                    )
                ),
            )
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("phones", "emails", "address", "actuality")
        )

        df = df_users.unionAll(df_support_clients)

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(array_distinct(col("emails")))) > 0,
                    array_compact(array_distinct(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter((col("phones").isNotNull() & col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
