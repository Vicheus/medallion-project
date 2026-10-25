from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    regexp_replace,
    lit,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0227"

    def parser(self):
        df_orders = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0227/raw/raw_csv/заказы libex.ru - @bereza_bd.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn("names", name_udf(regexp_replace(col("fullname"), "-", "")))
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("aaddress"))))),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf("aemail"))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf("phone"))))
            )
            .withColumn("ip_address_udf", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address_udf").isNotNull(),
                    array(
                        struct(
                            col("ip_address_udf").alias("ip"),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("lastmsgid"), col("lastmsgid"), lit("body"), col("body")
                ),
            )
            .select("names", "emails", "phones", "address", "ips", "raw_metadata")
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0227/raw/raw_csv/пользователи libex.ru - @bereza_bd.csv",
                sep=",",
                header=True,
            )
            .replace("<blank>", None)
            .withColumn(
                "names",
                regexp_replace(
                    name_parts_udf(
                        col("firstname"), col("lastname"), col("patronimic")
                    ),
                    "-",
                    "",
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("city").isNotNull() & col("zip").isNotNull(),
                                address_udf(
                                    concat_ws(
                                        " ", col("zip"), col("city"), col("address")
                                    )
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf("email"))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf("phone"))))
            )
            .withColumn("ips", array())
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("homepage"), col("homepage"))
            )
            .select("names", "emails", "phones", "address", "ips", "raw_metadata")
        )

        df = df_orders.unionAll(df_users)

        df = df.drop_duplicates(["names", "emails", "phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
