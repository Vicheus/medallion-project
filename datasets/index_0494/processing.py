from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    concat_ws,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0494"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0494/raw/b_user.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "address",
                when(
                    col("PERSONAL_STREET").isNotNull() & (col("PERSONAL_STREET") != ""),
                    address_udf(
                        concat_ws(" ", col("PERSONAL_ZIP"), col("PERSONAL_STREET"))
                    ),
                ).otherwise(lit(None)),
            )
            .withColumn("phones", phone_udf(col("PERSONAL_PHONE")))
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn("social_link", col("PERSONAL_WWW"))
            .withColumn("vk_id", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Интернет-магазин Мам, купи!").alias("title"),
                            lit("https://mamcupy.com").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull() & (col("vk_id") != ""),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "socials",
                "accounts",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
