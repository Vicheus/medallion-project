from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    struct,
    concat_ws,
)
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    sex_udf,
    phone_udf,
    address_udf,
    raw_metadata_udf,
    email_udf,
    actuality_date_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0406"
    output_file_count: int = 20
    calc_completeness: bool = False

    def parser(self):
        df_accounts = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0406/raw/preprocessed/accounts.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("address", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", lit(None))
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn("documents", array())
            .withColumn("works", array())
            .withColumn("educations", array())
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("modifiedAt"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "accounts",
                "ips",
                "documents",
                "works",
                "educations",
                "raw_metadata",
                "actuality",
            )
        )

        df_students = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0406/raw/preprocessed/students.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("shownname")))
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("address", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "accounts",
                when(
                    col("username").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Курсы 1Т").alias("title"),
                            lit("https://kurs.1t.ru").alias("link"),
                            col("username").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip_address").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip_address")).alias("ip"),
                                    lit(None).alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn("documents", array())
            .withColumn("works", array())
            .withColumn("educations", array())
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "accounts",
                "ips",
                "documents",
                "works",
                "educations",
                "raw_metadata",
                "actuality",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0406/raw/preprocessed/users.csv",
                sep=";",
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("lastName"))
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%M.%Y")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("subject"), col("registrationAddress"))),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phoneNumber")))
            .withColumn("accounts", array())
            .withColumn("ips", array())
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("passportSeries").isNotNull()
                            & col("passportNumber").isNotNull(),
                            document_udf(
                                lit("паспорт гражданина рф"),
                                concat_ws(
                                    "", col("passportSeries"), col("passportNumber")
                                ),
                                col("issuedDate"),
                                lit(None),
                                col("passportIssued"),
                                lit(None),
                                lit("%d.%M.%Y"),
                            ),
                        ).otherwise(None),
                        when(
                            col("snils").isNotNull(),
                            document_udf(
                                lit("снилс"),
                                col("snils"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("%d.%M.%Y"),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("jobInfo").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                col("jobTitle"),
                                lit(None),
                                lit(None),
                                col("jobInfo"),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "educations",
                when(
                    col("educationTitle").isNotNull() & (col("educationTitle") != ""),
                    array_compact(
                        array(
                            education_udf(
                                col("educationTitle"),
                                col("educationLevel"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("bio"),
                    col("bio"),
                    lit("statusSvo"),
                    col("statusSvo"),
                    lit("isInvalid"),
                    col("isInvalid"),
                    lit("academicDegree"),
                    col("academicDegree"),
                    lit("educationSeries"),
                    col("educationSeries"),
                    lit("educationNumber"),
                    col("educationNumber"),
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "accounts",
                "ips",
                "documents",
                "works",
                "educations",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_accounts.unionAll(df_students).unionAll(df_users)

        df = df.drop_duplicates(["names", "phones", "emails"])

        df = df.repartition(self.output_file_count)

        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
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
            & (col("documents").isNotNull() | col("address").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
