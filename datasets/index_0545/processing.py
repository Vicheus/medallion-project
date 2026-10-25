from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    array_compact,
    array_distinct,
    array,
    regexp_replace,
)
from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0545"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0545/raw/parsed/profiles.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phone_from_whatsapp_link",
                regexp_replace(col("whatsapp"), "https://wa.me/", ""),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone_from_whatsapp_link")),
                        )
                    )
                ),
            )
            .withColumn("address", address_udf(col("geo_city")))
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("telegram").isNotNull() & (col("telegram") != ""),
                            social_udf(
                                lit("Telegram"), lit(None), col("telegram"), lit(None)
                            ),
                        ).otherwise(None),
                        when(
                            col("whatsapp").isNotNull() & (col("whatsapp") != ""),
                            social_udf(
                                lit("WhatsApp"), lit(None), col("whatsapp"), lit(None)
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("page_title"),
                    col("page_title"),
                    lit("Юридический статус:"),
                    col("Юридический статус:"),
                    lit("Образование:"),
                    col("Образование:"),
                    lit("Стаж работы:"),
                    col("Стаж работы:"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_activity"), lit("%Y-%m-%dT%H:%M:%S%z")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "socials",
                "raw_metadata",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names", "phones", "emails"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
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
