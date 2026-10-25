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
    regexp_extract,
    concat_ws,
    coalesce,
    flatten,
    collect_list,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0135"

    def parser(self):
        vk_pattern = r"https://vk\.com/([^/]+)"

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0135/raw/users_sova_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                coalesce(
                    name_udf(col("full_name_1")),
                    name_udf(col("full_name_2")),
                    name_udf(col("full_name_3")),
                    name_udf(col("full_name_4")),
                    name_udf(col("full_name_5")),
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email_1")), email_udf(col("email_2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone_1")),
                            phone_udf(col("phone_2")),
                            phone_udf(col("phone_3")),
                            phone_udf(col("phone_4")),
                            phone_udf(col("phone_5")),
                        )
                    )
                ),
            )
            .withColumn("vk_id", regexp_extract(col("comment_1"), vk_pattern, 1))
            .withColumn("vk_link", regexp_extract(col("comment_1"), vk_pattern, 0))
            .withColumn(
                "address",
                when(
                    col("city").isNotNull(),
                    address_udf(concat_ws(" ", col("city"), col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("vk_id").isNotNull() & (col("vk_id") != ""),
                            struct(
                                lit("Vk").alias("title"),
                                col("vk_id").alias("id"),
                                col("vk_link").alias("link"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "works",
                array_compact(
                    array(
                        when(
                            col("work_position").isNotNull()
                            & (col("work_position") != ""),
                            work_udf(
                                col("work_position"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .select("names", "emails", "socials", "phones", "works", "address")
        )

        df = df.groupBy(["names"]).agg(
            array_distinct(flatten(collect_list("phones"))).alias("phones"),
            array_distinct(flatten(collect_list("emails"))).alias("emails"),
            array_distinct(flatten(collect_list("socials"))).alias("socials"),
            array_distinct(flatten(collect_list("works"))).alias("works"),
            collect_set("address").alias("address"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(col("socials"))) > 0,
                    array_compact(col("socials")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("works").isNotNull()
                | col("socials").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
