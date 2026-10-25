from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    split,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    phones_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0289"

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0289/raw/oqprint/users_type_1_*.csv",
                sep=",",
                header=True,
            )
            .filter(col("Полное имя") != col("Почта1"))
            .withColumn("names", name_udf(regexp_replace(col("Полное имя"), "\.", "")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Телефоны"))))),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("Почта1")), email_udf(col("Почта2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("Адреса")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата создания"), lit("%d.%m.%Y %H:%M")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0289/raw/oqprint/users_type_2_*.csv",
                sep=",",
                header=True,
            )
            .filter(col("Полное имя") != col("Почта1"))
            .withColumn("names", name_udf(regexp_replace(col("Полное имя"), "\.", "")))
            .withColumn("phones", phones_udf(split(col("Телефоны"), ",")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("Почта1")), email_udf(col("Почта2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("Адреса")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата создания"), lit("%d.%m.%Y %H:%M")),
            )
            .select("names", "phones", "emails", "address", "actuality")
        )

        df = df_1.unionAll(df_2)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
