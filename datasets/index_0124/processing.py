from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0124"

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("email", StringType(), True),
                StructField("email2", StringType(), True),
                StructField("unknown_field_1", StringType(), True),
                StructField("birth_date", StringType(), True),
                StructField("username", StringType(), True),
                StructField("unknown_date", StringType(), True),
                StructField("city", StringType(), True),
                StructField("job_place", StringType(), True),
                StructField("job", StringType(), True),
                StructField("unknown_field_2", StringType(), True),
                StructField("link", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0124/raw/synergyregions_ru_11_2019.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"
        facebook_pattern = r"http://www.facebook.com/([a-zA-Z0-9_]+)"

        df = (
            df.replace("NULL", None)
            .withColumn("vk_link", regexp_extract("link", vk_pattern, 1))
            .withColumn("facebook_link", regexp_extract("link", facebook_pattern, 1))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "emails", array(email_udf(col("email")), email_udf(col("email2")))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn(
                "works",
                array(
                    when(
                        col("job").isNotNull() | col("job_place").isNotNull(),
                        work_udf(
                            col("job"),
                            lit(None),
                            lit(None),
                            col("job_place"),
                            lit(None),
                            lit(None),
                        ),
                    ).otherwise(None)
                ),
            )
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
                            ).otherwise(None),
                            when(
                                col("facebook_link").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    lit(None),
                                    col("facebook_link"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("unknown_date"), lit("%Y-%m-%d %H:%M:%S%z")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "socials",
                "works",
                "birth_date",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
        )

        df = df.dropDuplicates()

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names", "emails", "phones", "socials", "works", "birth_date", "actuality"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
