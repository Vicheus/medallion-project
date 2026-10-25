from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    struct,
    regexp_extract,
    concat_ws,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    sex_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
    birth_date_udf,
)
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0478"

    def parser(self):
        df_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0478/raw/users.csv",
            sep=";",
            header=True,
        )

        vk_pattern = r"http://vk.com/([a-zA-Z0-9_]+)"

        df_1 = (
            df_1.withColumn(
                "names",
                name_parts_udf(col("NAME"), col("LAST_NAME"), col("SECOND_NAME")),
            )
            .withColumn("sex", sex_udf(col("PERSONAL_GENDER")))
            .withColumn(
                "birth_date", birth_date_udf(col("PERSONAL_BIRTHDAY"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("LOGIN")), email_udf(col("EMAIL")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("PERSONAL_PHONE"))))),
            )
            .withColumn("social_link", col("PERSONAL_WWW"))
            .withColumn("vk_id", regexp_extract("PERSONAL_WWW", vk_pattern, 1))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("PERSONAL_STATE"),
                        col("PERSONAL_CITY"),
                        col("PERSONAL_STREET"),
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("LOGIN").isNotNull() & col("PASSWORD").isNotNull(),
                    array(
                        struct(
                            lit("Строительная Академия ТЕХНОНИКОЛЬ").alias("title"),
                            lit("https://academy.tn.ru").alias("link"),
                            col("LOGIN").alias("login"),
                            col("PASSWORD").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull() & (col("vk_id") != ""),
                                social_udf(
                                    lit("Vk"),
                                    col("vk_id"),
                                    col("social_link"),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("LAST_LOGIN"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("PERSONAL_NOTES"), col("PERSONAL_NOTES")),
            )
            .withColumn("works", array())
            .withColumn("documents", array())
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "actuality",
                "socials",
                "works",
                "documents",
                "raw_metadata",
            )
        )

        df_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0478/raw/users2.csv",
            sep=";",
            header=True,
        )

        df_2_users = (
            df_2.withColumn(
                "names",
                name_udf(col("UF_REG_FIO")),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", array())
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("UF_OLDPHONE"))))),
            )
            .withColumn("address", lit(None))
            .withColumn("accounts", array())
            .withColumn("socials", array())
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn("documents", array())
            .withColumn(
                "works",
                when(
                    col("UF_REG_DOLJNOST").isNotNull()
                    | col("UF_COMPANY_NAME").isNotNull(),
                    array(
                        work_udf(
                            col("UF_REG_DOLJNOST"),
                            lit(None),
                            lit(None),
                            col("UF_COMPANY_NAME"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "actuality",
                "socials",
                "works",
                "documents",
                "raw_metadata",
            )
        )

        df_3_companies = (
            df_2.withColumn(
                "names",
                name_udf(col("UF_COMPANY_NAME")),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", array())
            .withColumn("phones", array())
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("UF_REG_UR_ADDR"))),
            )
            .withColumn("accounts", array())
            .withColumn("socials", array())
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("UF_REG_INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("UF_REG_INN"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                            when(
                                col("UF_REG_KPP").isNotNull(),
                                document_udf(
                                    lit("кпп"),
                                    col("UF_REG_KPP"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn("works", array())
            .select(
                "names",
                "sex",
                "birth_date",
                "emails",
                "phones",
                "accounts",
                "address",
                "actuality",
                "socials",
                "works",
                "documents",
                "raw_metadata",
            )
        )

        df = df_1.unionAll(df_2_users).unionAll(df_3_companies)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    col("address").isNotNull(),
                    array_compact(array_distinct(array(col("address")))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array_distinct(array(col("raw_metadata")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
