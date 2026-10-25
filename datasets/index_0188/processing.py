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
    coalesce,
    first,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    sex_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0188"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0188/raw/users_preprocessed_kingfish.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("phone"), lit(self.dataset_country_code.value)
                            ),
                            phone_udf(
                                col("phone3"), lit(self.dataset_country_code.value)
                            ),
                            phone_udf(
                                col("phone4"), lit(self.dataset_country_code.value)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("email")),
                            email_udf(col("username")),
                            email_udf(col("email2")),
                            email_udf(col("email3")),
                        )
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password_hash").isNotNull(),
                    array(
                        struct(
                            lit("KingFish").alias("title"),
                            lit("https://kingfish.by").alias("link"),
                            col("username").alias("login"),
                            col("password_hash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (col("inn").isNotNull() & (col("inn") != ""))
                                | (col("inn2").isNotNull() & (col("inn2") != "")),
                                document_udf(
                                    lit("инн"),
                                    coalesce(col("inn"), col("inn2")).alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                    lit("yyyy-MM-dd"),
                                    lit(self.dataset_country_code.value),
                                ),
                            )
                        )
                    )
                ),
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "sex",
            "birth_date",
            "accounts",
            "address",
            "documents",
        )

        df = df.groupBy("names", "emails", "phones").agg(
            first("sex").alias("sex"),
            first("birth_date").alias("birth_date"),
            flatten(collect_set("accounts")).alias("accounts"),
            flatten(collect_set("address")).alias("address"),
            flatten(collect_set("documents")).alias("documents"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
            | col("documents").isNotNull()
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
