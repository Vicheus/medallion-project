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
    concat,
    from_unixtime,
    flatten,
    collect_set,
    first,
    max,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0433"
    validate_invalid_groupping: bool = True

    def parser(self):
        df_users_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0433/raw/credit_customers.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_place", address_udf(col("birth_place")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("full_address")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("workexperience"),
                    col("workexperience"),
                    lit("amount"),
                    col("amount"),
                    lit("income"),
                    col("income"),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("passport_series").isNotNull()
                    & col("passport_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_series").isNotNull()
                                & col("passport_number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat(
                                        col("passport_series"), col("passport_number")
                                    ),
                                    col("passport_issued_date"),
                                    lit(None),
                                    col("passport_issued_by"),
                                    col("passport_unit_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("accounts", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("datetime"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "accounts",
                "actuality",
            )
        )

        df_users_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0433/raw/user.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("username")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn("documents", array())
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("Kreditos.ru - подбор финансовых услуг").alias("title"),
                            lit("https://kreditos.ru").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("created_at"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "accounts",
                "actuality",
            )
        )

        df_users_2 = (
            df_users_2.join(df_users_1, on="emails", how="left_anti")
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "accounts",
                "actuality",
            )
        )

        df_users_1_with_doc = df_users_1.filter(size(col("documents")) > 0)
        df_users_1_without_doc = (
            df_users_1.filter(size(col("documents")) == 0)
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "accounts",
                "actuality",
            )
        )

        df_users_1_with_doc = (
            df_users_1_with_doc.groupby(
                col("documents")[0]["serial"], col("documents")[0]["type"]
            )
            .agg(
                array_compact(array_distinct(collect_set("names"))).alias("names"),
                first("birth_date", ignorenulls=True).alias("birth_date"),
                first("sex", ignorenulls=True).alias("sex"),
                first("birth_place", ignorenulls=True).alias("birth_place"),
                array_compact(array_distinct(collect_set("phones"))).alias("phones"),
                array_compact(array_distinct(collect_set("emails"))).alias("emails"),
                array_compact(array_distinct(collect_set("address"))).alias("address"),
                array_compact(array_distinct(collect_set("raw_metadata"))).alias(
                    "raw_metadata"
                ),
                array_compact(array_distinct(flatten(collect_set("accounts")))).alias(
                    "accounts"
                ),
                array_compact(array_distinct(flatten(collect_set("documents")))).alias(
                    "documents"
                ),
                max("actuality").alias("actuality"),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "birth_place",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "accounts",
                "actuality",
            )
        )

        df = df_users_1_with_doc.unionAll(df_users_1_without_doc).unionAll(df_users_2)

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
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
