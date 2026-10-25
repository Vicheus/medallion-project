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
    first,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0224"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0224/raw/users_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_order_props = self.read(
            path="/media/user/SAMSUNG/Databases/index_0224/raw/order_props_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_order_props = df_order_props.groupBy("user_id").agg(
            first(
                when(col("prop_code") == "fio", col("prop_value")), ignorenulls=True
            ).alias("fio"),
            first(
                when(col("prop_code") == "e-mail", col("prop_value")), ignorenulls=True
            ).alias("e-mail"),
            first(
                when(col("prop_code") == "nomer_tel", col("prop_value")),
                ignorenulls=True,
            ).alias("nomer_tel"),
            first(
                when(col("prop_code") == "ADDRESS", col("prop_value")), ignorenulls=True
            ).alias("ADDRESS"),
        )

        df = (
            df_users.join(
                df_order_props, df_users["ID"] == df_order_props["user_id"], "left"
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_udf(col("fio")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("e-mail")), email_udf(col("email")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("nomer_tel")), phone_udf(col("phone")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("city").isNotNull(),
                                address_udf(concat_ws(" ", col("city"), col("street"))),
                            ),
                            when(
                                col("ADDRESS").isNotNull(), address_udf(col("ADDRESS"))
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("Zimnie").alias("title"),
                            lit("https://www.zimnie.com").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "accounts", "address", "sex")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
