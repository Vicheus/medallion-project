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
    regexp_replace,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0235"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0235/raw/club_foto_ru_preprocessed.csv",
                sep="\t",
                header=True,
            )
            .replace("\\N", None)
            .withColumn("names", name_udf(regexp_replace(col("user_name"), "-", "")))
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("user_email")),
                            email_udf(col("user_email_reserve")),
                        )
                    )
                ),
            )
            .withColumn(
                "address",
                when(col("user_from").isNotNull(), address_udf(col("user_from"))),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("date_of_birth"), lit("%Y-%m-%d"))
            )
            .withColumn("ip_address", ip_address_udf(col("user_ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(col("user_lastlogin")).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("user_password").isNotNull(),
                    array(
                        struct(
                            lit("Клуб и форум фотографов Club-Foto.ru").alias("title"),
                            lit("https://www.club-foto.ru").alias("link"),
                            col("login").alias("login"),
                            col("user_password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("user_lastlogin"), col("user_last_update"), col("regdate")
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("user_website"),
                    col("user_website"),
                    lit("user_occ"),
                    col("user_occ"),
                    lit("self_portrait_text"),
                    col("self_portrait_text"),
                    lit("equip_body"),
                    col("equip_body"),
                    lit("equip_lens"),
                    col("equip_lens"),
                ),
            )
            .select(
                "names",
                "emails",
                "address",
                "birth_date",
                "accounts",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
