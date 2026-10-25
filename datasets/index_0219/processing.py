from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, size, array_compact, concat_ws

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
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
    dataset_code_name: str = "index_0219"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0219/raw/leader-id.ru (3.5m, 2023).csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("father_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn(
                "socials",
                when(
                    col("telegram").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("telegram").isNotNull(),
                                social_udf(
                                    lit("Telegram"),
                                    col("telegram"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("employment_company_name").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                col("employment_position_name"),
                                lit(None),
                                lit(None),
                                col("employment_company_name"),
                                address_udf(
                                    when(
                                        col(
                                            "employment_company_legalAddress"
                                        ).isNotNull(),
                                        col("employment_company_legalAddress"),
                                    )
                                ),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                when(
                    col("address_city").isNotNull()
                    | col("address_country").isNotNull(),
                    concat_ws(
                        " ",
                        col("address_post_code"),
                        col("address_country"),
                        col("address_city"),
                        col("address_street"),
                        col("address_building"),
                        col("address_apartment"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_seen"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "sex",
                "birth_date",
                "works",
                "socials",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
