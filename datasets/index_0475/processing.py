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
    concat_ws,
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


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0475"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0475/raw/alpmarathon_ru.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_parts_udf(col("mname"), col("fam"), col("gname")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%Y-%m-%d")))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("country"), col("region"), col("sity"))),
            )
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("pswd").isNotNull(),
                    array(
                        struct(
                            lit("Марафоны БАМ - 2025").alias("title"),
                            lit("https://alpmarathon.ru").alias("link"),
                            col("login").alias("login"),
                            col("pswd").alias("password_hash"),
                            lit(None).alias("id"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_rec"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "address",
                "phones",
                "emails",
                "accounts",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(),
                    array_compact(array_distinct(array(col("address")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(),
                    array_compact(array_distinct(array(col("emails")))),
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("address").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
