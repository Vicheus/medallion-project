from pyspark import StorageLevel
from pyspark.sql.types import StructType, StringType
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    regexp_extract,
    concat,
    concat_ws,
    trim,
    flatten,
    collect_set,
    first,
    greatest,
    max,
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.work.udfs import work_udf
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
    dataset_code_name: str = "index_0222"

    def parser(self):
        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"

        user_schema = (
            StructType()
            .add("ID", StringType(), True)
            .add("TIMESTAMP_X", StringType(), True)
            .add("LOGIN", StringType(), True)
            .add("ACTIVE", StringType(), True)
            .add("NAME", StringType(), True)
            .add("LAST_NAME", StringType(), True)
            .add("EMAIL", StringType(), True)
            .add("LAST_LOGIN", StringType(), True)
            .add("DATE_REGISTER", StringType(), True)
            .add("LID", StringType(), True)
            .add("PERSONAL_PROFESSION", StringType(), True)
            .add("PERSONAL_WWW", StringType(), True)
            .add("PERSONAL_ICQ", StringType(), True)
            .add("PERSONAL_GENDER", StringType(), True)
            .add("PERSONAL_BIRTHDATE", StringType(), True)
            .add("PERSONAL_PHOTO", StringType(), True)
            .add("PERSONAL_PHONE", StringType(), True)
            .add("PERSONAL_FAX", StringType(), True)
            .add("PERSONAL_MOBILE", StringType(), True)
            .add("PERSONAL_PAGER", StringType(), True)
            .add("PERSONAL_STREET", StringType(), True)
            .add("PERSONAL_MAILBOX", StringType(), True)
            .add("PERSONAL_CITY", StringType(), True)
            .add("PERSONAL_STATE", StringType(), True)
            .add("PERSONAL_ZIP", StringType(), True)
            .add("PERSONAL_COUNTRY", StringType(), True)
            .add("PERSONAL_NOTES", StringType(), True)
            .add("WORK_COMPANY", StringType(), True)
            .add("WORK_DEPARTMENT", StringType(), True)
            .add("WORK_POSITION", StringType(), True)
            .add("WORK_WWW", StringType(), True)
            .add("WORK_PHONE", StringType(), True)
            .add("WORK_FAX", StringType(), True)
            .add("WORK_PAGER", StringType(), True)
            .add("WORK_STREET", StringType(), True)
            .add("WORK_MAILBOX", StringType(), True)
            .add("WORK_CITY", StringType(), True)
            .add("WORK_STATE", StringType(), True)
            .add("WORK_ZIP", StringType(), True)
            .add("WORK_COUNTRY", StringType(), True)
            .add("WORK_PROFILE", StringType(), True)
            .add("WORK_LOGO", StringType(), True)
            .add("WORK_NOTES", StringType(), True)
            .add("ADMIN_NOTES", StringType(), True)
            .add("STORED_HASH", StringType(), True)
            .add("XML_ID", StringType(), True)
            .add("PERSONAL_BIRTHDAY", StringType(), True)
            .add("EXTERNAL_AUTH_ID", StringType(), True)
            .add("CHECKWORD_TIME", StringType(), True)
            .add("SECOND_NAME", StringType(), True)
            .add("CONFIRM_CODE", StringType(), True)
            .add("LOGIN_ATTEMPTS", StringType(), True)
            .add("LAST_ACTIVITY_DATE", StringType(), True)
            .add("AUTO_TIME_ZONE", StringType(), True)
            .add("TIME_ZONE", StringType(), True)
            .add("TIME_ZONE_OFFSET", StringType(), True)
            .add("TITLE", StringType(), True)
            .add("BX_USER_ID", StringType(), True)
            .add("LANGUAGE_ID", StringType(), True)
            .add("BLOCKED", StringType(), True)
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0222/raw/cafemumu - @bereza_bd.txt",
                sep="\t",
                header=False,
                schema=user_schema,
            )
            .replace("NULL", None)
            .withColumn("vk_link", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "socials",
                when(
                    col("vk_link").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_link").isNotNull(),
                                social_udf(
                                    lit("Vk"), lit(None), col("vk_link"), lit(None)
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("NAME"), col("LAST_NAME"), col("`SECOND_NAME`")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                            phone_udf(col("WORK_PHONE")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("EMAIL")), email_udf(col("LOGIN")))
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("WORK_DEPARTMENT").isNotNull()
                    | col("WORK_POSITION").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    trim(
                                        concat_ws(
                                            " ",
                                            col("WORK_DEPARTMENT"),
                                            col("WORK_POSITION"),
                                        )
                                    ),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("PERSONAL_CITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("PERSONAL_CITY"),
                                        col("PERSONAL_ZIP"),
                                        when(
                                            col("PERSONAL_STREET").isNotNull(),
                                            concat(lit("ул. "), col("PERSONAL_STREET")),
                                        ).otherwise(None),
                                    ),
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("LAST_LOGIN"),
                        col("DATE_REGISTER"),
                        col("LAST_ACTIVITY_DATE"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "address",
                "socials",
                "works",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df.groupBy(["emails", "phones"]).agg(
            array_compact(flatten(collect_set(col("names")))).alias("names"),
            array_compact(flatten(collect_set(col("works")))).alias("works"),
            array_compact(flatten(collect_set(col("address")))).alias("address"),
            array_compact(flatten(collect_set(col("socials")))).alias("socials"),
            first(col("sex"), ignorenulls=True).alias("sex"),
            first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
