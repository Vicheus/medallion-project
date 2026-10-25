from pyspark import StorageLevel

from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    concat_ws,
    array_distinct,
    concat,
    split,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    birth_date_udf,
    phones_udf,
    emails_udf,
    name_udf,
    sex_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0423"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0423/raw/output.csv", sep=";"
            )
            .withColumn("names", name_udf("fullname"))
            .withColumn("birth_date", birth_date_udf(col("born_date"), lit("%Y-%m-%d")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%dT%H:%M:%S.%fZ")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        phones_udf(
                            split(col("phones"), ","),
                            lit(self.dataset_country_code.value),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(emails_udf(split(col("emails"), ",")))),
            )
            .withColumn(
                "educations",
                array_compact(
                    array(
                        when(
                            col("educations_0_name").isNotNull()
                            & (col("educations_0_name") != ""),
                            education_udf(
                                concat_ws(
                                    " ",
                                    col("educations_0_name"),
                                    col("educations_0_faculty"),
                                ),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("educations_0_duration").isNotNull(),
                                    concat(col("educations_0_duration"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            ),
                        ).otherwise(None),
                        when(
                            col("educations_1_name").isNotNull()
                            & (col("educations_1_name") != ""),
                            education_udf(
                                concat_ws(
                                    " ",
                                    col("educations_1_name"),
                                    col("educations_1_faculty"),
                                ),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("educations_1_duration").isNotNull(),
                                    concat(col("educations_1_duration"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            ),
                        ).otherwise(None),
                        when(
                            col("educations_2_name").isNotNull()
                            & (col("educations_2_name") != ""),
                            education_udf(
                                concat_ws(
                                    " ",
                                    col("educations_2_name"),
                                    col("educations_2_faculty"),
                                ),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("educations_2_duration").isNotNull(),
                                    concat(col("educations_2_duration"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            ),
                        ).otherwise(None),
                        when(
                            col("educations_3_name").isNotNull()
                            & (col("educations_3_name") != ""),
                            education_udf(
                                concat_ws(
                                    " ",
                                    col("educations_3_name"),
                                    col("educations_3_faculty"),
                                ),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("educations_3_duration").isNotNull(),
                                    concat(col("educations_3_duration"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            ),
                        ).otherwise(None),
                        when(
                            col("educations_4_name").isNotNull()
                            & (col("educations_4_name") != ""),
                            education_udf(
                                concat_ws(
                                    " ",
                                    col("educations_4_name"),
                                    col("educations_4_faculty"),
                                ),
                                lit(None),
                                lit(None),
                                lit(None),
                                when(
                                    col("educations_4_duration").isNotNull(),
                                    concat(col("educations_4_duration"), lit("-01-01")),
                                ).otherwise(None),
                                lit(None),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "works",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("experiences_0_name").isNotNull()
                                | col("experiences_0_position").isNotNull(),
                                work_udf(
                                    col("experiences_0_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_0_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_1_name").isNotNull()
                                | col("experiences_1_position").isNotNull(),
                                work_udf(
                                    col("experiences_1_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_1_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_2_name").isNotNull()
                                | col("experiences_2_position").isNotNull(),
                                work_udf(
                                    col("experiences_2_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_2_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_3_name").isNotNull()
                                | col("experiences_3_position").isNotNull(),
                                work_udf(
                                    col("experiences_3_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_3_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_4_name").isNotNull()
                                | col("experiences_4_position").isNotNull(),
                                work_udf(
                                    col("experiences_4_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_4_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_5_name").isNotNull()
                                | col("experiences_5_position").isNotNull(),
                                work_udf(
                                    col("experiences_5_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_5_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_6_name").isNotNull()
                                | col("experiences_6_position").isNotNull(),
                                work_udf(
                                    col("experiences_6_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_6_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_7_name").isNotNull()
                                | col("experiences_7_position").isNotNull(),
                                work_udf(
                                    col("experiences_7_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_7_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_8_name").isNotNull()
                                | col("experiences_8_position").isNotNull(),
                                work_udf(
                                    col("experiences_8_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_8_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_9_name").isNotNull()
                                | col("experiences_9_position").isNotNull(),
                                work_udf(
                                    col("experiences_9_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_9_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_10_name").isNotNull()
                                | col("experiences_10_position").isNotNull(),
                                work_udf(
                                    col("experiences_10_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_10_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_11_name").isNotNull()
                                | col("experiences_11_position").isNotNull(),
                                work_udf(
                                    col("experiences_11_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_11_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("experiences_12_name").isNotNull()
                                | col("experiences_12_position").isNotNull(),
                                work_udf(
                                    col("experiences_12_position"),
                                    lit(None),
                                    lit(None),
                                    col("experiences_12_name"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("telegram").isNotNull(),
                            social_udf(
                                lit("Telegram"), col("telegram"), lit(None), lit(None)
                            ),
                        ).otherwise(None),
                        when(
                            col("whatsapp").isNotNull(),
                            social_udf(
                                lit("Whatsapp"), lit(None), col("whatsapp"), lit(None)
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("additional_educations_0_course"),
                    col("additional_educations_0_course"),
                    lit("additional_educations_1_duration"),
                    col("additional_educations_1_duration"),
                    lit("additional_educations_2_organization"),
                    col("additional_educations_2_organization"),
                    lit("description"),
                    col("description"),
                    lit("experiences_0_duties"),
                    col("experiences_0_duties"),
                    lit("experiences_1_duties"),
                    col("experiences_1_duties"),
                    lit("experiences_2_duties"),
                    col("experiences_2_duties"),
                    lit("experiences_3_duties"),
                    col("experiences_3_duties"),
                    lit("experiences_4_duties"),
                    col("experiences_4_duties"),
                    lit("experiences_5_duties"),
                    col("experiences_5_duties"),
                    lit("experiences_6_duties"),
                    col("experiences_6_duties"),
                    lit("experiences_7_duties"),
                    col("experiences_7_duties"),
                    lit("experiences_8_duties"),
                    col("experiences_8_duties"),
                    lit("experiences_9_duties"),
                    col("experiences_9_duties"),
                    lit("experiences_10_duties"),
                    col("experiences_10_duties"),
                    lit("experiences_11_duties"),
                    col("experiences_11_duties"),
                    lit("experiences_12_duties"),
                    col("experiences_12_duties"),
                    lit("skills"),
                    col("skills"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "emails",
                "educations",
                "works",
                "raw_metadata",
                "actuality",
                "socials",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
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
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
