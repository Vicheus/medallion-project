from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    array_compact,
    array_distinct,
    coalesce,
)
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0038"

    def parser(self):

        users_schema = StructType(
            [
                StructField("id", StringType(), nullable=True),
                StructField("created_at", StringType(), nullable=True),
                StructField("updated_at", StringType(), nullable=True),
                StructField("user_email", StringType(), nullable=True),
                StructField("user_phone", StringType(), nullable=True),
                StructField("unknown_field_1", StringType(), nullable=True),
                StructField("unknown_field_2", StringType(), nullable=True),
            ]
        )
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0038/raw/gloriajeans/users.csv",
            sep="\t",
            schema=users_schema,
            header=False,
        )

        customers_schema = StructType(
            [
                StructField("id", StringType(), nullable=True),
                StructField("unknown_field_1", StringType(), nullable=True),
                StructField("unknown_field_2", StringType(), nullable=True),
                StructField("email", StringType(), nullable=True),
                StructField("unknown_field_3", StringType(), nullable=True),
                StructField("phone", StringType(), nullable=True),
                StructField("unknown_field_4", StringType(), nullable=True),
                StructField("client_card_number", StringType(), nullable=True),
                StructField("unknown_field_5", StringType(), nullable=True),
                StructField("first_name", StringType(), nullable=True),
                StructField("last_name", StringType(), nullable=True),
                StructField("unknown_field_6", StringType(), nullable=True),
                StructField("birth_date", StringType(), nullable=True),
                StructField("gender", IntegerType(), nullable=True),
                StructField("unknown_field_7", StringType(), nullable=True),
                StructField("unknown_field_8", StringType(), nullable=True),
                StructField("unknown_field_9", StringType(), nullable=True),
                StructField("unknown_field_10", StringType(), nullable=True),
                StructField("unknown_field_11", StringType(), nullable=True),
                StructField("unknown_field_12", StringType(), nullable=True),
                StructField("unknown_field_13", StringType(), nullable=True),
                StructField("unknown_field_14", StringType(), nullable=True),
                StructField("unknown_field_15", StringType(), nullable=True),
                StructField("unknown_field_16", StringType(), nullable=True),
                StructField("unknown_field_17", StringType(), nullable=True),
                StructField("password", StringType(), nullable=True),
                StructField("unknown_field_18", StringType(), nullable=True),
                StructField("unknown_field_19", StringType(), nullable=True),
                StructField("unknown_field_20", StringType(), nullable=True),
                StructField("unknown_field_21", StringType(), nullable=True),
                StructField("unknown_field_22", StringType(), nullable=True),
                StructField("unknown_field_23", StringType(), nullable=True),
                StructField("unknown_field_24", StringType(), nullable=True),
                StructField("unknown_field_25", StringType(), nullable=True),
            ]
        )
        df_customers = self.read(
            path="/media/user/SAMSUNG/Databases/index_0038/raw/gloriajeans/customers.csv",
            sep="\t",
            schema=customers_schema,
            header=False,
        )

        df_customers.select(
            "id",
            "email",
            "phone",
            "client_card_number",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "password",
        ).show(truncate=False)

        df = (
            df_customers.join(df_users, "id", "left")
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("user_phone")), phone_udf(col("phone")))
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("user_email")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull()
                    & (
                        col("password").isNotNull()
                        | col("client_card_number").isNotNull()
                    ),
                    array(
                        struct(
                            lit("Глория Джинс").alias("title"),
                            lit("https://gloria-jeans.ru").alias("link"),
                            col("id").alias("id"),
                            col("password").alias("password"),
                            col("client_card_number").alias("client_card_number"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )
        df = df.select(
            "names", "emails", "phones", "sex", "birth_date", "accounts", "actuality"
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
