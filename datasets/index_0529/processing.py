from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    relations_udf,
    names_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf

from pyspark import StorageLevel
from pyspark.sql.functions import (
    udf,
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    from_unixtime,
)
from pyspark.sql.types import StringType


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0529"
    calc_completeness: bool = False

    def parser(self):
        def decode_unicode(s):
            if s is None:
                return None
            try:
                # first unescape \\uXXXX → \uXXXX
                s1 = s.encode("utf-8").decode("unicode_escape")
                # second pass for double-escaped data
                return s1.encode("latin1").decode("unicode_escape")
            except Exception:
                return s

        decode_unicode_udf = udf(decode_unicode, StringType())

        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0529/raw/ubu_ru_700k_2021/www.ubu.ru.csv",
            sep=",",
            header=True,
        ).replace("<blank>", None)
        df = (
            df.withColumn("normal_address", address_udf(decode_unicode_udf("ur_addr")))
            .withColumn("post_address", address_udf(decode_unicode_udf("post_addr")))
            .withColumn(
                "normal_address_with_type",
                address_with_type_udf(col("normal_address"), lit(1)),
            )
            .withColumn(
                "post_address_with_type",
                address_with_type_udf(col("post_address"), lit(1)),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(array(col("normal_address"), col("post_address")))
                ),
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array(
                        col("normal_address_with_type"), col("post_address_with_type")
                    )
                ),
            )
        )
        df.select("ur_addr", "post_addr", "normal_address", "post_address").show(
            n=20, truncate=False
        )

        df = df.cache()

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        names_udf(
                            array(
                                decode_unicode_udf("ur_fname"),
                                decode_unicode_udf("ur_name"),
                                decode_unicode_udf("first_name"),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "contact_person", name_udf(decode_unicode_udf("contact_person"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("age"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn("relations", relations_udf(col("contact_person")))
            .withColumn(
                "socials",
                when(
                    col("fb_id").isNotNull() | col("vk_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                social_udf(
                                    lit("Vkontakte"),
                                    col("vk_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("fb_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("fb_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    (col("kpp").isNotNull() | col("inn").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("kpp").isNotNull()),
                                document_udf(
                                    lit("кпп"),
                                    col("kpp"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
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
                "accounts",
                array(
                    struct(
                        lit("ubu.ru").alias("title"),
                        lit("https://ubu.ru/").alias("link"),
                        col("login").alias("login"),
                        col("pass").alias("password_hash"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("last_login"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            ip_address_udf(col("ip")).alias("ip"),
                            ip_date_udf(
                                from_unixtime(col("last_login"), "yyyy-MM-dd HH:mm:ss"),
                                lit("%Y-%m-%d %H:%M:%S"),
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "relations",
                "emails",
                "phones",
                "address",
                "addresses",
                "socials",
                "documents",
                "ips",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(
                    size(array_compact(array_distinct(col("address")))) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(array_distinct(col("socials")))) > 0,
                    array_compact(array_distinct(col("socials"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(array_distinct(col("documents")))) > 0,
                    array_compact(array_distinct(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(array_distinct(col("ips")))) > 0,
                    array_compact(array_distinct(col("ips"))),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(
                    size(array_compact(array_distinct(col("names")))) > 0,
                    array_compact(array_distinct(col("names"))),
                ).otherwise(None),
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
                "relations",
                when(col("relations").isNotNull(), array(col("relations"))).otherwise(
                    None
                ),
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
