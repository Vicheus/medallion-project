from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    trim,
    coalesce,
)
from pyspark.sql.types import StructType, StringType, IntegerType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    address_with_type_udf,
    normalize_address_batch_udf
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 5
    dataset_code_name: str = "index_0005"
    calc_completeness: bool = False

    def parser(self):
        schema_main = (
            StructType()
            .add("user_id", StringType(), True)
            .add("first_name", StringType(), True)
            .add("last_name", StringType(), True)
            .add("middle_name", StringType(), True)
            .add("email", StringType(), True)
            .add("phone", StringType(), True)
            .add("password_hash", StringType(), True)
            .add("gender", StringType(), True)
            .add("birth_date", StringType(), True)
            .add("address", StringType(), True)
            .add("source", StringType(), True)
            .add("not_identified_column_1", StringType(), True)
            .add("metric", StringType(), True)
            .add("not_identified_column_2", StringType(), True)
            .add("not_identified_column_3", StringType(), True)
            .add("created_at", StringType(), True)
            .add("updated_at", StringType(), True)
        )

        schema_inn = (
            StructType()
            .add("id", StringType(), True)
            .add("user_id", StringType(), True)
            .add("inn", StringType(), True)
            .add("response_code", StringType(), True)
            .add("response_inn", StringType(), True)
            .add("captcha_required", StringType(), True)
            .add("error_details", StringType(), True)
            .add("created_at_2", StringType(), True)
            .add("updated_at_2", StringType(), True)
        )

        schema_passport = (
            StructType()
            .add("id", StringType(), True)
            .add("user_id", StringType(), True)
            .add("serial", StringType(), True)
            .add("number", StringType(), True)
            .add("date_issue", StringType(), True)
            .add("authority", StringType(), True)
            .add("authority_code", StringType(), True)
            .add("date_expire", StringType(), True)
            .add("created_at_3", StringType(), True)
            .add("updated_at_3", StringType(), True)
        )

        df_main = self.read(
            path="/media/user/SAMSUNG/Databases/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_adengi.ru.csv",
            sep=",",
            schema=schema_main,
            header=False,
        )
        df_inn = self.read(
            path="/media/user/SAMSUNG/Databases/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_inn_adengi.ru.csv",
            sep=",",
            schema=schema_inn,
            header=False,
        )
        df_passport = self.read(
            path="/media/user/SAMSUNG/Databases/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_passports_adengi.ru.csv",
            sep=",",
            schema=schema_passport,
            header=False,
        )

        df_main = (
            df_main.withColumn("user_id", trim(col("user_id")).cast(IntegerType()))
            .alias("df_main")
            .coalesce(5)
        )
        df_inn = (
            df_inn.withColumn("user_id", trim(col("user_id")).cast(IntegerType()))
            .alias("df_inn")
            .coalesce(5)
        )
        df_passport = (
            df_passport.withColumn("user_id", trim(col("user_id")).cast(IntegerType()))
            .alias("df_passport")
            .coalesce(5)
        )

        df = (
            df_main.join(df_inn, "user_id", "left")
            .join(df_passport, "user_id", "left")
            .coalesce(5)
        )

        df = df.dropDuplicates(
            ["phone", "email", "first_name", "last_name", "middle_name"]
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("last_name"), col("first_name"), col("middle_name")),
            )
            .withColumn("address_str", col("address"))
            .withColumn("address_str", address_udf(col("address")))
            .withColumn("address_with_type", address_with_type_udf(col("address_str"), lit(1)))
            .withColumn('address', normalize_address_batch_udf(array(col('address_with_type'))))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    col("number").isNotNull() | col("inn").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("number"),
                                    col("date_issue"),
                                    lit(None),
                                    col("authority"),
                                    col("authority_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("adengi").alias("title"),
                        lit("https://adengi.ru/").alias("link"),
                        col("user_id").alias("id"),
                        col("password_hash").alias("password_hash"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        ).coalesce(5)

        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "accounts",
            "documents",
            "sex",
            "birth_date",
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("accounts").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.show(n=10, truncate=False)

        return df.coalesce(5)


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
