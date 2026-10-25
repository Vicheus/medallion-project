from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    size,
    concat_ws,
    concat,
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0264"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0264/raw/pharmacosmetica.ru 2021.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date",
                when(
                    col("birthdate") > 0,
                    birth_date_udf(
                        from_unixtime(col("birthdate"), "yyyy-MM-dd HH:mm:ss"),
                        lit("%Y-%m-%d %H:%M:%S"),
                    ),
                ).otherwise(lit(None)),
            )
            .withColumn(
                "dauth",
                when(
                    col("dauth") > 0, from_unixtime(col("dauth"), "yyyy-MM-dd HH:mm:ss")
                ).otherwise(lit(None)),
            )
            .withColumn(
                "date",
                when(
                    col("date") > 0, from_unixtime(col("date"), "yyyy-MM-dd HH:mm:ss")
                ).otherwise(lit(None)),
            )
            .withColumn(
                "address",
                when(
                    col("city").isNotNull(),
                    address_udf(
                        concat_ws(
                            " ",
                            col("zipcode"),
                            col("region"),
                            col("city"),
                            col("street"),
                            when(
                                col("home") != "", concat(lit("д. "), col("home"))
                            ).otherwise(None),
                            when(
                                col("flat") != "", concat(lit("кв. "), col("flat"))
                            ).otherwise(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Pharmacosmetica.ru").alias("title"),
                            lit("https://www.pharmacosmetica.ru").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("date"), col("dauth")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("basket"), col("basket"), lit("area"), col("area")
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "birth_date",
                "accounts",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
