from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0247"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0247/raw/rusnod_users.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("FullName")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("Email")), email_udf(col("Login")))
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("address", address_udf(col("Address")))
            .withColumn("birth_date", birth_date_udf(col("Year"), lit("%d.%m.%Y")))
            .withColumn(
                "socials",
                when(
                    col("VK").isNotNull()
                    | col("FB").isNotNull()
                    | col("TW").isNotNull()
                    | col("Skype").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("VK").isNotNull() & col("VK").like("%vk.com%"),
                                struct(
                                    lit("ВКонтакте").alias("title"),
                                    lit(None).alias("id"),
                                    col("VK").alias("link"),
                                ),
                            ).otherwise(None),
                            when(
                                col("FB").isNotNull()
                                & col("FB").like("%facebook.com%"),
                                struct(
                                    lit("Facebook").alias("title"),
                                    lit(None).alias("id"),
                                    col("FB").alias("link"),
                                ),
                            ).otherwise(None),
                            when(
                                col("TW").isNotNull() & col("TW").like("%twitter.com%"),
                                struct(
                                    lit("Twitter").alias("title"),
                                    lit(None).alias("id"),
                                    col("TW").alias("link"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Skype").isNotNull(),
                                struct(
                                    lit("Skype").alias("title"),
                                    col("Skype").alias("id"),
                                    lit(None).alias("link"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("NickName").isNotNull() & col("Password").isNotNull(),
                    array(
                        struct(
                            lit("Rusnod.ru").alias("title"),
                            lit("https://rusnod.ru").alias("link"),
                            col("NickName").alias("login"),
                            col("Password").alias("password_hash"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("Created"), col("LastUpdated")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("About"), col("About"), lit("Site"), col("Site")),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "birth_date",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
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
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
