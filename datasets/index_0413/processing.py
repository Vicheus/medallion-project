from pyspark.sql.functions import when, col, size, array, lit, struct, coalesce
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    sex_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0413"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0413/raw/avtopilot-ekat.ru_14.csv",
                sep="|",
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn("phones", phone_udf(col("PERSONAL_PHONE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull(),
                    array(
                        struct(
                            lit("avtopilot-ekat.ru").alias("title"),
                            col("PASSWORD").alias("PASSWORD"),
                            col("ID").alias("id"),
                            col("LOGIN").alias("login"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_REGISTER"), col("LAST_LOGIN")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "sex", "emails", "phones", "accounts", "actuality")
        )

        df = df.drop_duplicates(["names", "emails", "phones"])

        df = df.repartition(self.output_file_count)

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
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
