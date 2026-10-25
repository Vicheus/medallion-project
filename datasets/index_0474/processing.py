from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    collect_set,
    flatten,
    first,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0474"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0474/raw/Russia-(Moscow)-122,957.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("full_name")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("address")), email_udf(col("work_email")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("mobile_phone"))))),
            )
            .withColumn("address", address_udf(col("location_name")))
            .withColumn(
                "socials",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("facebook_url").isNotNull(),
                                array_compact(
                                    array(
                                        when(
                                            col("facebook_url").isNotNull()
                                            & (col("facebook_url") != ""),
                                            social_udf(
                                                lit("Facebook"),
                                                lit(None),
                                                col("facebook_url"),
                                                lit(None),
                                            ),
                                        ).otherwise(None)
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_url").isNotNull(),
                                array_compact(
                                    array(
                                        when(
                                            col("twitter_url").isNotNull()
                                            & (col("twitter_url") != ""),
                                            social_udf(
                                                lit("Twitter"),
                                                lit(None),
                                                col("twitter_url"),
                                                lit(None),
                                            ),
                                        ).otherwise(None)
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("linkedin_url").isNotNull(),
                                array_compact(
                                    array(
                                        when(
                                            col("linkedin_url").isNotNull()
                                            & (col("linkedin_url") != ""),
                                            social_udf(
                                                lit("LinkedIn"),
                                                lit(None),
                                                col("linkedin_url"),
                                                lit(None),
                                            ),
                                        ).otherwise(None)
                                    )
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("job_company_name").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("job_company_name"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("industry"),
                    col("industry"),
                    lit("job_company_industry"),
                    col("job_company_industry"),
                    lit("job_company_facebook_url"),
                    col("job_company_facebook_url"),
                    lit("job_company_twitter_url"),
                    col("job_company_twitter_url"),
                    lit("inferred_salary"),
                    col("inferred_salary"),
                    lit("job_company_website"),
                    col("job_company_website"),
                ),
            )
            .select(
                "pnum",
                "names",
                "sex",
                "emails",
                "phones",
                "address",
                "works",
                "socials",
                "raw_metadata",
            )
        )

        df = (
            df.groupBy("pnum")
            .agg(
                array_compact(array_distinct(collect_set(col("names")))).alias("names"),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("socials"))))
                ).alias("socials"),
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                first(col("sex")).alias("sex"),
            )
            .select(
                "names",
                "sex",
                "emails",
                "phones",
                "address",
                "works",
                "socials",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
