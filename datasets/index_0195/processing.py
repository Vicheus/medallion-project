from pyspark import StorageLevel
from pyspark.sql.functions import (
    array_compact,
    when,
    col,
    lit,
    array,
    struct,
    greatest,
    regexp_replace,
    size,
    length,
)
from pyspark.sql.types import StructType, StringType, StructField

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.socials.settings import Titles
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0195"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY
    output_file_count: int = 50
    calc_completeness: bool = False

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("email", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("name", StringType(), True),
                StructField("password", StringType(), True),
                StructField("country", StringType(), True),
                StructField("currency", StringType(), True),
                StructField("role", StringType(), True),
                StructField("activity", StringType(), True),
                StructField("time_registration", StringType(), True),
                StructField("birthday", StringType(), True),
                StructField("passport", StringType(), True),
                StructField("address", StringType(), True),
                StructField("passport_by", StringType(), True),
                StructField("partner_key", StringType(), True),
                StructField("last_ip", StringType(), True),
                StructField("last_ip_country", StringType(), True),
                StructField("tg_id", StringType(), True),
                StructField("timezone", StringType(), True),
                StructField("hash_id", StringType(), True),
                StructField("note", StringType(), True),
                StructField("poker_nickname", StringType(), True),
                StructField("firstdeposit_time", StringType(), True),
                StructField("bk_type", StringType(), True),
                StructField("deposits_calc_count", StringType(), True),
                StructField("deposits_calc_time", StringType(), True),
                StructField("regulated_domain_id", StringType(), True),
                StructField("tenant_id", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0080/raw/cleaned.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df = df.filter(
            (col("country") != "ua")
            & (col("last_ip_country") != "ua")
            & (~col("phone").like("38%"))
            & (~col("phone").like("+38%"))
            & (col("phone").isNotNull())
            & (col("phone").like("37%") | col("phone").like("+37%"))
        )

        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn("id", regexp_replace(col("id"), r"\(", ""))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones", phone_udf(col("phone"), lit(self.dataset_country_code.value))
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("ip", ip_address_udf(col("last_ip")))
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull(),
                    document_udf(
                        lit(None),
                        col("passport"),
                        lit(None),
                        lit(None),
                        col("passport_by"),
                        lit(None),
                        lit("%d.%m.%Y"),
                        lit(self.dataset_country_code.value),
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("tg_id").isNotNull()
                    & (col("tg_id") != "")
                    & (length(col("tg_id")) > 2),
                    array_compact(
                        array(
                            when(
                                col("tg_id").isNotNull() & (col("tg_id") != ""),
                                social_udf(
                                    lit(Titles.Telegram),
                                    col("tg_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array_compact(array(struct(col("ip").alias("ip")))),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                lit("1Win").alias("title"),
                                lit("https://www.p218.ru/").alias("link"),
                                col("email").alias("login"),
                                col("password").alias("password_hash"),
                                col("id").alias("id"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("time_registration"), col("deposits_calc_time")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("note"),
                    col("note"),
                    lit("poker_nickname"),
                    col("poker_nickname"),
                    lit("firstdeposit_time"),
                    col("firstdeposit_time"),
                    lit("bk_type"),
                    col("bk_type"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "socials",
                "accounts",
                "documents",
                "birth_date",
                "ips",
                "actuality",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
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
                "documents",
                when(col("documents").isNotNull(), array(col("documents"))).otherwise(
                    None
                ),
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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
