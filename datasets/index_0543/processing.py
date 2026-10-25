from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    array_compact,
    array_distinct,
    array,
    concat,
    split,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    phones_udf,
    email_udf,
    emails_udf,
    actuality_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0543"
    validate_invalid_groupping: bool = True
    calc_completeness: bool = False

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0543/raw/dеІtа.ru - @StormBaseAdapter/users.csv",
            sep="\t",
            header=True,
        ).replace("\\N", None)

        df_users = (
            df_users.withColumn("names", name_udf(col("full_name")))
            .withColumn("phones", array_compact(array(phone_udf(col("mphone")))))
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df_support = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0543/raw/dеІtа.ru - @StormBaseAdapter/support.csv",
            sep="\t",
            header=True,
        ).replace("\\N", None)

        df_support_executors = (
            df_support.withColumn("names", name_udf(col("executor_fio")))
            .withColumn(
                "phones", array_compact(array(phone_udf(col("executor_phone"))))
            )
            .withColumn("emails", array())
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df_support_managers = (
            df_support.withColumn("names", name_udf(col("manager")))
            .withColumn("emails", array_compact(array(email_udf(col("manager_email")))))
            .withColumn("phones", array())
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df_support_clients = (
            df_support.withColumn("names", name_udf(col("contact_name")))
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
            .select("names", "phones", "emails", "address", "actuality")
        )

        df_business_clients = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0543/raw/dеІtа.ru - @StormBaseAdapter/business_clients.csv",
                sep="\t",
                header=True,
            )
            .replace("\\N", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        concat(
                            phones_udf(split(col("phones"), ",")),
                            array(phone_udf(col("mobile_phones"))),
                        )
                    )
                ),
            )
            .withColumn("emails", emails_udf(split(col("emails"), ";")))
            .withColumn("address", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%d.%m.%Y %H:%M:%S.%f")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df = (
            df_users.unionAll(df_support_managers)
            .unionAll(df_support_clients)
            .unionAll(df_support_executors)
            .unionAll(df_business_clients)
        )

        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
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
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
