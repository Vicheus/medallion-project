from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    array_compact,
    coalesce,
)

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
    dataset_code_name: str = "index_0036"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0036/raw/book24_ru.csv",
            sep="|",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array(
                        phone_udf(col("PERSONAL_PHONE")),
                        phone_udf(col("PERSONAL_MOBILE")),
                    )
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() | col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Book24").alias("title"),
                            lit("https://book24.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("LAST_LOGIN"), col("DATE_REGISTER")),
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
