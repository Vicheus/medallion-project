from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    max,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    first,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
    address_udf,
    relations_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0274"
    output_file_count: int = 10

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0274/raw/vitaexpress.ru/preprocessed/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf("PERSONAL_GENDER"))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("PERSONAL_PHONE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Аптека Вита").alias("title"),
                            lit("https://vitaexpress.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("relations", array())
            .withColumn("address", array())
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "actuality",
                "accounts",
                "relations",
                "address",
            )
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0274/raw/vitaexpress.ru/preprocessed/*from_orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("UF_CREATED_AT"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("accounts", array())
            .withColumn(
                "relations",
                when(
                    col("relation_name").isNotNull(),
                    array(
                        when(
                            col("relation_name").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("relation_name"),
                                    col("relation_phone"),
                                    lit("Контактное лицо"),
                                )
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(),
                    array(
                        when(
                            col("address").isNotNull(),
                            address_udf(concat_ws(" ", col("city"), col("address"))),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "actuality",
                "accounts",
                "relations",
                "address",
            )
        )

        df = df_users_1.unionAll(df_users_2)

        df = df.groupBy(["names", "phones", "emails"]).agg(
            first(col("sex"), ignorenulls=True).alias("sex"),
            first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            max(col("actuality")).alias("actuality"),
            array_distinct(array_compact(flatten(collect_set(col("accounts"))))).alias(
                "accounts"
            ),
            array_distinct(array_compact(flatten(collect_set(col("relations"))))).alias(
                "relations"
            ),
            array_distinct(array_compact(flatten(collect_set(col("address"))))).alias(
                "address"
            ),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
