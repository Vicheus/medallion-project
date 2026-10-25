from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat_ws,
    array_compact,
    struct,
    array_distinct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0142"

    def parser(self):
        df_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0142/raw/kazany_preprocessed.csv",
            sep=",",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0142/raw/kazany_preprocessed-2.csv",
            sep=",",
            header=True,
        )

        df_2 = (
            df_2.replace("NULL", None)
            .replace("null", None)
            .replace("Null", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(""))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn("emails", lit(None))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("address_1_1").isNotNull()
                                    | col("address_1_2").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("address_1_zipcode") != "",
                                            col("address_1_zipcode"),
                                        ).otherwise(None),
                                        when(
                                            col("address_1_city") != "",
                                            col("address_1_city"),
                                        ).otherwise(None),
                                        when(
                                            col("address_1_1") != "", col("address_1_1")
                                        ).otherwise(None),
                                        when(
                                            col("address_1_2") != "", col("address_1_2")
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("address_2_1").isNotNull()
                                    | col("address_2_2").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("address_2_zipcode") != "",
                                            col("address_2_zipcode"),
                                        ).otherwise(None),
                                        when(
                                            col("address_2_city") != "",
                                            col("address_2_city"),
                                        ).otherwise(None),
                                        when(
                                            col("address_2_1") != "", col("address_2_1")
                                        ).otherwise(None),
                                        when(
                                            col("address_2_2") != "", col("address_2_2")
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn("accounts", array())
            .withColumn("works", array())
            .select("names", "emails", "phones", "address", "accounts", "works")
        )

        df_1 = (
            df_1.replace("NULL", None)
            .replace("null", None)
            .replace("Null", None)
            .withColumn(
                "names", name_parts_udf(col("firstname"), col("lastname"), lit(""))
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
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("address_1_1").isNotNull()
                                    | col("address_1_2").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("address_1_zipcode") != "",
                                            col("address_1_zipcode"),
                                        ).otherwise(None),
                                        when(
                                            col("address_1_city") != "",
                                            col("address_1_city"),
                                        ).otherwise(None),
                                        when(
                                            col("address_1_1") != "", col("address_1_1")
                                        ).otherwise(None),
                                        when(
                                            col("address_1_2") != "", col("address_1_2")
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("address_2_1").isNotNull()
                                    | col("address_2_2").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("address_2_zipcode") != "",
                                            col("address_2_zipcode"),
                                        ).otherwise(None),
                                        when(
                                            col("address_2_city") != "",
                                            col("address_2_city"),
                                        ).otherwise(None),
                                        when(
                                            col("address_2_1") != "", col("address_2_1")
                                        ).otherwise(None),
                                        when(
                                            col("address_2_2") != "", col("address_2_2")
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
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
                            lit("Kazany.ru").alias("title"),
                            lit("https://kazany.ru/").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "address", "accounts", "works")
        )

        df = df_1.unionAll(df_2).drop_duplicates()

        df = df.select("names", "emails", "phones", "address", "accounts", "works")

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
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
