from pyspark.sql.types import StructType, StringType
from pyspark.sql.functions import when, col, lit, array, struct

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0046"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails,documents"

    def parser(self):
        schema = (
            StructType()
            .add("id", StringType(), True)
            .add("email", StringType(), True)
            .add("unknown_field_1", StringType(), True)
            .add("unknown_field_2", StringType(), True)
            .add("first_name", StringType(), True)
            .add("middle_name", StringType(), True)
            .add("last_name", StringType(), True)
            .add("birth_date", StringType(), True)
            .add("phone", StringType(), True)
            .add("unknown_field_4", StringType(), True)
            .add("unknown_field_5", StringType(), True)
            .add("unknown_field_6", StringType(), True)
            .add("unknown_field_7", StringType(), True)
            .add("unknown_field_8", StringType(), True)
            .add("unknown_field_9", StringType(), True)
            .add("unknown_field_10", StringType(), True)
            .add("unknown_field_11", StringType(), True)
            .add("unknown_field_12", StringType(), True)
            .add("unknown_field_13", StringType(), True)
            .add("unknown_field_14", StringType(), True)
            .add("unknown_field_15", StringType(), True)
            .add("unknown_field_16", StringType(), True)
            .add("unknown_field_17", StringType(), True)
            .add("unknown_field_18", StringType(), True)
            .add("unknown_field_19", StringType(), True)
            .add("unknown_field_20", StringType(), True)
            .add("username", StringType(), True)
            .add("unknown_field_21", StringType(), True)
            .add("unknown_field_22", StringType(), True)
            .add("unknown_field_23", StringType(), True)
            .add("unknown_field_24", StringType(), True)
            .add("unknown_field_25", StringType(), True)
            .add("unknown_field_26", StringType(), True)
            .add("unknown_field_27", StringType(), True)
            .add("unknown_field_28", StringType(), True)
            .add("unknown_field_29", StringType(), True)
            .add("unknown_field_30", StringType(), True)
            .add("unknown_field_31", StringType(), True)
            .add("unknown_field_32", StringType(), True)
            .add("unknown_field_33", StringType(), True)
            .add("snils", StringType(), True)
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0046/raw/school.mos.ru.csv",
                sep="\t",
                schema=schema,
                header=False,
            )
            .replace("\\N", None)
            .select(
                "id",
                "email",
                "last_name",
                "first_name",
                "middle_name",
                "birth_date",
                "phone",
                "snils",
                "username",
            )
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                when(
                    col("snils").isNotNull(),
                    array(
                        when(
                            col("snils").isNotNull(),
                            document_udf(
                                lit("снилс"),
                                col("snils"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull() & col("username").isNotNull(),
                    array(
                        struct(
                            lit("«Московская электронная школа» «МЭШ»").alias("title"),
                            lit("https://school.mos.ru").alias("link"),
                            col("username").alias("login"),
                            col("id").alias("id"),
                        )
                    ),
                ),
            )
        )

        df = df.select("names", "phones", "emails", "birth_date", "documents")

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
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
