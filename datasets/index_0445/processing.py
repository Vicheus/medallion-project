from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    size,
    struct,
    greatest,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0445"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0445/raw/users.csv",
            sep=";",
            header=True,
        ).filter(col("lastName") != "Удалить")

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("firstName"), col("lastName"), col("middleName")
                            ),
                            name_parts_udf(
                                col("firstNameEng"), col("lastNameEng"), lit(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date", birth_date_udf(col("dateOfBirth"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("passwordHash").isNotNull(),
                    array(
                        struct(
                            lit("NAUMEN - информационные системы управления").alias(
                                "title"
                            ),
                            lit("https://www.naumen.ru").alias("link"),
                            col("email").alias("login"),
                            col("passwordHash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created"), col("modified")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("names", "emails", "sex", "birth_date", "accounts", "actuality")
        )

        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("emails").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
