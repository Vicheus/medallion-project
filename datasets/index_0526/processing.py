from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    trim,
    concat_ws,
    array_compact,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    normalize_address_batch_udf,
    address_with_type_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0526"

    def parser(self):
        df_orders = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0526/raw/medvenica/medvenica.ru orders.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_parts_udf(col("Имя"), col("Фамилия"), lit(None)))
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата создания"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("address", lit(None))
            .withColumn("addresses", array())
            .select("names", "emails", "phones", "address", "addresses", "actuality")
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0526/raw/medvenica/medvenica.ru users.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("actuality", lit(None))
            .withColumn(
                "address",
                address_udf(
                    trim(
                        concat_ws(
                            " ",
                            col("Почтовый индекс"),
                            col("Адрес (строка 1)"),
                            col("Город"),
                            col("Адрес (строка 2)"),
                        )
                    )
                ),
            )
            .withColumn(
                "address_with_type", address_with_type_udf(col("address"), lit(1))
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(array(col("address_with_type"))),
            )
            .select("names", "emails", "phones", "address", "addresses", "actuality")
        )

        df = df_orders.unionAll(df_users).drop_duplicates(["emails"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
            )
            .withColumn(
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
