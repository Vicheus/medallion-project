from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    regexp_replace,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0226"

    def parser(self):
        df_patients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0226/raw/preprocessed/patients_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("name"), col("last_name"), col("patronymic")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("mobile")),
                            phone_udf(col("phone_work")),
                            phone_udf(col("phone_home")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("series_identity_doc").isNotNull()
                                & col("num_identity_doc").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat_ws(
                                        "",
                                        col("series_identity_doc"),
                                        col("num_identity_doc"),
                                    ).alias("serial"),
                                    col("date_identity_doc").alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("publ_identity_doc").alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
                            when(
                                col("snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("snils").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
                            when(
                                col("num_insur_policy_oms").isNotNull(),
                                document_udf(
                                    lit("номер страхового полиса"),
                                    col("num_insur_policy_oms").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("date_create"), col("date_mod")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("referer"),
                    col("referer"),
                    lit("other_info"),
                    col("other_info"),
                    lit("parent_name"),
                    col("parent_name"),
                    lit("child_name"),
                    col("child_name"),
                    lit("blood_group"),
                    col("blood_group"),
                    lit("rh_blood_group"),
                    col("rh_blood_group"),
                    lit("chronic_desease"),
                    col("chronic_desease"),
                    lit("allergy"),
                    col("allergy"),
                    lit("ITN"),
                    col("ITN"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "birth_date",
                "sex",
                "documents",
                "actuality",
                "raw_metadata",
            )
        )

        df_patients_customers = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0226/raw/preprocessed/patients_customers_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("mobile")), phone_udf(col("phone_add")))
                    )
                ),
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("email")))))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("address", address_udf(col("address")))
            .withColumn("sex", lit(None))
            .withColumn(
                "additional_doc",
                regexp_replace(regexp_replace(col("reason"), "№", ""), " ", ""),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("passport").alias("serial"),
                                    col("passport_date").alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("passport_publ").alias("authority"),
                                    regexp_replace(
                                        col("passport_subdiv_code"), "-", ""
                                    ).alias("authority_code"),
                                ),
                            ),
                            when(
                                col("additional_doc").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("additional_doc").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("date_create"), col("date_mod")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("ITN"), col("ITN")))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "birth_date",
                "sex",
                "documents",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_patients.unionAll(df_patients_customers)

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
