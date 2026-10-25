from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    size,
    array_distinct,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    address_udf,
    name_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0029"

    def parser(self):
        df = self.read(
            path="/home/user/Documents/dev/git/datasphere/Parsetron/data/input/users_kuchenland_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_udf("name2"),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone1")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email1")),
                            email_udf(col("email2")),
                            email_udf(col("email3")),
                            email_udf(col("email4")),
                        )
                    )
                ),
            )
            .withColumn(
                "sex", when(col("sex") != "", sex_udf(col("sex"))).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() | col("password").isNotNull(),
                    array(
                        struct(
                            lit("Kuchenland").alias("title"),
                            lit("https://www.kuchenland.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address2").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip_address2")).alias("ip"),
                                    ip_date_udf(col("ip_date")).alias("date"),
                                ),
                            ),
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip_address")).alias("ip"),
                                    lit(None).alias("date"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(concat_ws(" ", col("city"), col("address"))),
                            address_udf(
                                concat_ws(" ", col("work_city"), col("work_address"))
                            ),
                            address_udf(col("address2")),
                            address_udf(col("address3")),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("ip_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "ips",
                "accounts",
                "address",
                "sex",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "ips",
            "accounts",
            "address",
            "sex",
            "actuality",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
