from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    struct,
    array_compact,
    array_distinct,
    array,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0091"

    def parser(self):
        df_passengers = self.read(
            path="millenium_passengers_preprocessed.csv", sep=";", header=True
        )
        df_passengers = (
            df_passengers.withColumn("names", name_udf("name"))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(array(phone_udf("phone1"), phone_udf("phone2")))
                ),
            )
            .withColumn("emails", email_udf("email"))
            .withColumn("sex", sex_udf("sex"))
            .withColumn("birth_date", birth_date_udf("birthdate"))
            .withColumn(
                "accounts",
                when(
                    col("user_id").isNotNull(),
                    array(
                        struct(
                            lit("millennium-platform.ru").alias("title"),
                            lit("https://millennium-platform.ru").alias("link"),
                            col("user_id").alias("id"),
                            lit(None).alias("login"),
                            lit(None).alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("work_position").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("work_position"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull() | col("foreign_passport").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    col("passport_date"),
                                    col("passport_enddate"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("foreign_passport").isNotNull(),
                                document_udf(
                                    lit("заграничный паспорт гражданина рф"),
                                    col("foreign_passport"),
                                    col("foreign_passport_date"),
                                    col("foreign_passport_enddate"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("ips", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "documents",
                "ips",
            )
        )

        df_users = self.read(
            path="millenium_users_preprocessed.csv", sep=";", header=True
        )
        df_users = (
            df_users.withColumn("names", name_udf("name"))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf("phone1"),
                            phone_udf("phone2"),
                            phone_udf("phone3"),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf("email"))
            .withColumn("sex", sex_udf("sex"))
            .withColumn("birth_date", email_udf("birthdate"))
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() | col("pass").isNotNull(),
                    array(
                        struct(
                            lit("millennium-platform.ru").alias("title"),
                            lit("https://millennium-platform.ru").alias("link"),
                            lit(None).alias("id"),
                            col("login").alias("login"),
                            col("pass").alias("password"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("work_position").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("work_position"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull() | col("foreign_passport").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    col("passport_date"),
                                    col("passport_enddate"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("foreign_passport").isNotNull(),
                                document_udf(
                                    lit("заграничный паспорт гражданина рф"),
                                    col("foreign_passport"),
                                    col("foreign_passport_date"),
                                    col("foreign_passport_enddate"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("other_passport").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("other_passport"),
                                    col("other_passport_date"),
                                    col("other_passport_enddate"),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "sex",
                "birth_date",
                "accounts",
                "works",
                "documents",
                "ips",
            )
        )

        df = df_passengers.unionAll(df_users)

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
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
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
