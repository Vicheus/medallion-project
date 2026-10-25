from pyspark.sql.functions import (
    when,
    col,
    lit,
    regexp_replace,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    flatten,
    collect_set,
    first,
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0241"

    def parser(self):
        df_auth = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0241/raw/auth.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                regexp_replace(
                    name_parts_udf(col("first_name"), col("last_name"), lit(None)),
                    r"\.",
                    "",
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", array())
            .withColumn("birth_date", birth_date_udf(col("bdate"), lit("%d.%m.%Y")))
            .withColumn(
                "address",
                when(
                    col("country").isNotNull() | col("city").isNotNull(),
                    address_udf(concat_ws(" ", col("country"), col("city"))),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                social_udf(
                                    lit("ВКонтакте"), col("vk_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("sex", lit(None))
            .withColumn("documents", array())
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "socials",
                "address",
                "documents",
                "sex",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0241/raw/users.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                regexp_replace(
                    name_parts_udf(
                        col("first_name"), col("last_name"), col("father_name")
                    ),
                    r"\.",
                    "",
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone_org")),
                            phone_udf(col("phone_org_dop")),
                            phone_udf(col("phone_mob")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("address", lit(None))
            .withColumn("socials", array())
            .withColumn(
                "documents",
                when(
                    col("Inn").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("Inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "socials",
                "address",
                "documents",
                "sex",
            )
        )

        df = df_auth.unionAll(df_users)

        df = (
            df.groupby(["names", "phones"])
            .agg(
                array_compact(collect_set("emails")).alias("emails"),
                array_compact(collect_set("address")).alias("address"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("socials"))).alias("socials"),
                first("birth_date").alias("birth_date"),
                first("sex").alias("sex"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "socials",
                "address",
                "documents",
                "sex",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
