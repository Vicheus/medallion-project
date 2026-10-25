from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    concat,
    size,
    concat_ws,
    array_distinct,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    name_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0122"

    def parser(self):
        df_persons = self.read(
            path="/media/user/SAMSUNG/Databases/index_0122/raw/osp.ru person - @bereza_bd .csv",
            sep=",",
            header=True,
        )
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0122/raw/osp.ru user - @bereza_bd.csv",
            sep=",",
            header=True,
        )

        df_users = (
            df_users.replace("<blank>", None)
            .withColumn(
                "names",
                name_parts_udf(col("FirstName"), col("LastName"), col("MidName")),
            )
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "emails", array(email_udf(col("Email")), email_udf(col("spam_email")))
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%M-%d")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("city").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("city"),
                                        when(
                                            col("street") != "",
                                            concat(lit("ул. "), col("street")),
                                        ).otherwise(None),
                                        when(
                                            col("house") != "",
                                            concat(lit("д. "), col("house")),
                                        ).otherwise(None),
                                        when(
                                            col("flat") != "",
                                            concat(lit("кв. "), col("flat")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("address").isNotNull(), col("address")
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                array(
                    when(
                        col("job").isNotNull(),
                        work_udf(
                            col("job"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("Login").isNotNull() | col("Password").isNotNull(),
                    array(
                        struct(
                            lit("Издательство Открытые системы").alias("title"),
                            lit("https://www.osp.ru").alias("link"),
                            col("Login").alias("login"),
                            col("Password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("LastLoginDate"), col("LastUpdated")),
                    lit("%Y-%m-%d %H:%M:%S%z"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "accounts",
                "works",
                "birth_date",
                "sex",
                "actuality",
            )
        )

        df_users.show(n=20, truncate=False)

        df_persons = (
            df_persons.replace("<blank>", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", array(email_udf(col("email"))))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("address", array())
            .withColumn(
                "works",
                array(
                    when(
                        col("position").isNotNull(),
                        work_udf(
                            col("position"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn("accounts", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_updated"), lit("%Y-%m-%d %H:%M:%S%z")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "accounts",
                "works",
                "birth_date",
                "sex",
                "actuality",
            )
        )

        df = df_persons.unionAll(df_users)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df = df.dropDuplicates()

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "accounts",
            "works",
            "birth_date",
            "sex",
            "actuality",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
