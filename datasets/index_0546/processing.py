from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, struct, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0546"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0546/raw/tеnchаt.ru-@StormBaseAdapter.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("birth_date", birth_date_udf(col("bdate"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf((col("address"))))
            .withColumn(
                "documents",
                when(
                    (col("inn").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("inn").isNotNull()),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    col("instagram_username").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("instagram_username").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    col("instagram_username"),
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
                    col("company").isNotNull() | col("job_title").isNotNull(),
                    array_compact(
                        array(
                            work_udf(
                                col("job_title"),
                                lit(None),
                                lit(None),
                                col("company"),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("tenchat_username").isNotNull() | col("tenchat_id").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                lit("TenChat").alias("title"),
                                lit("https://tenchat.ru/").alias("link"),
                                col("tenchat_username").alias("username"),
                                col("tenchat_id").alias("id"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("subscribers_count"),
                    col("subscribers_count"),
                    lit("description"),
                    col("description"),
                    lit("work_status"),
                    col("work_status"),
                    lit("education"),
                    col("education"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "socials",
                "works",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
