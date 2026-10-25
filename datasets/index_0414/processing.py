from pyspark.sql.functions import (
    when,
    col,
    size,
    array,
    lit,
    struct,
    coalesce,
    regexp_extract,
    array_compact,
)
from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    sex_udf,
    email_udf,
    actuality_date_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0414"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        instagram_pattern = r"https://www.instagram.com/([a-zA-Z0-9_]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0414/raw/protuning-company.ru_27.csv",
                sep="|",
            )
            .withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 0))
            .withColumn(
                "instagram_link", regexp_extract("PERSONAL_WWW", instagram_pattern, 0)
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("PERSONAL_MOBILE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull(),
                    array(
                        struct(
                            lit("Pro-Tuning - профессиональное тюнинг - ателье").alias(
                                "title"
                            ),
                            lit("https://protuning-company.ru").alias("link"),
                            col("PASSWORD").alias("PASSWORD"),
                            col("ID").alias("id"),
                            col("LOGIN").alias("login"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_link").isNotNull() | col("instagram_link").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_link").isNotNull(),
                                social_udf(
                                    lit("Vk"), lit(None), col("vk_link"), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("instagram_link").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    lit(None),
                                    col("instagram_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DATE_REGISTER"), col("LAST_LOGIN")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "socials",
                "actuality",
            )
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
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
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
