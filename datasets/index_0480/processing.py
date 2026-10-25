from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    flatten,
    size,
    concat_ws,
    regexp_extract,
    expr,
    max,
)

from parsetron import Parsetron
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0480"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        vk_pattern = r"https://vk\.com/([^/]+)"

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0480/raw/trudvsem_ru_11_2024.csv",
            sep="\t",
            header=True,
        )
        df = (
            df.withColumn("vk_id", regexp_extract(col("VK"), vk_pattern, 1))
            .withColumn("names", name_udf(col("FullName")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("Region"), col("Location")))
            )
            .withColumn("birth_date", birth_date_udf(col("BDay"), lit("%Y-%m-%d")))
            .withColumn(
                "educations",
                when(
                    col("Education").isNotNull() | col("University").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                col("University"),
                                col("Education"),
                                lit(None),
                                lit(None),
                                col("YearOfIssue"),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                array(
                    when(
                        col("PlaceOfWork").isNotNull() | col("Profession").isNotNull(),
                        work_udf(
                            col("Profession"),
                            lit(None),
                            lit(None),
                            col("PlaceOfWork"),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
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
                                    lit("VK"),
                                    col("vk_id"),
                                    col("VK"),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("actuality", actuality_date_udf(col("Date"), lit("%Y-%m-%d")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Nickname"),
                    col("Nickname"),
                    lit("Date"),
                    col("Date"),
                    lit("Salary"),
                    col("Salary"),
                    lit("Grafic"),
                    col("Grafic"),
                    lit("NameOfWork"),
                    col("NameOfWork"),
                    lit("Specialty"),
                    col("Specialty"),
                    lit("KnowledgeOfTheLanguage"),
                    col("KnowledgeOfTheLanguage"),
                    lit("DriversLicense"),
                    col("DriversLicense"),
                    lit("Skills"),
                    col("Skills"),
                    lit("TechnicalSkills"),
                    col("TechnicalSkills"),
                    lit("Past"),
                    col("Past"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "educations",
                "works",
                "socials",
                "actuality",
                "raw_metadata",
            )
        )

        df = (
            df.groupBy(["names", "birth_date"])
            .agg(
                array_distinct(array_compact(collect_set(col("phones")))).alias(
                    "phones"
                ),
                array_distinct(array_compact(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_distinct(array_compact(collect_set(col("address")))).alias(
                    "address"
                ),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("educations"))))
                ).alias("educations"),
                array_distinct(array_compact(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("socials"))))
                ).alias("socials"),
                max("actuality").alias("actuality"),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 30)"))
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "educations",
                "works",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
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
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
