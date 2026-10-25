from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0228"

    def parser(self):
        df_clients_props = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0228/raw/clients_props_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("name")),
                            name_parts_udf(col("fio1"), col("fio2"), col("fio3")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("mail")))))
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address")),
                            when(
                                col("region").isNotNull() & col("nas_pun").isNotNull(),
                                address_udf(
                                    concat_ws(
                                        " ",
                                        col("index2"),
                                        col("region"),
                                        col("nas_pun"),
                                        col("street"),
                                        col("house"),
                                        col("flat"),
                                    )
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("КомБук").alias("title"),
                            lit("https://combook.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("ips", array())
            .select("names", "phones", "emails", "address", "accounts", "ips")
        )

        df_orders_props = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0228/raw/orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("fio")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone_cl")),
                            phone_udf(col("phone2")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("mail")))))
            )
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn("accounts", array())
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ),
            )
            .select("names", "phones", "emails", "address", "accounts", "ips")
        )

        df = df_clients_props.unionAll(df_orders_props)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
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
