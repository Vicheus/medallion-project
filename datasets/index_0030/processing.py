from pyspark.sql.functions import (
    col,
    when,
    array,
    concat_ws,
    lit,
    expr,
    array_distinct,
    array_compact,
    struct,
    coalesce,
)
from pyspark import StorageLevel

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    email_udf,
    sex_udf,
    phones_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: int = 5
    dataset_code_name: str = "index_0030"
    calc_completeness: bool = False

    def parser(self):

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0030/raw/oriflame-ru.json"
        )

        df = (
            df.replace("NULL", None)
            .withColumn(
                "birth_date", birth_date_udf(col("BIRTH_DATE"), lit("%Y.%m.%d"))
            )
            .withColumn("sex", sex_udf(col("GENDER")))
            .withColumn(
                "phones",
                phones_udf(
                    array_distinct(
                        expr("transform(TELEPHONES, item -> item.TELEPHONE_NUMBER)")
                    )
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "names", name_udf(concat_ws(" ", col("FIRST_NAME"), col("LAST_NAME")))
            )
            .withColumn(
                "address",
                array_distinct(
                    expr(
                        "transform(ADDRESSES, item -> concat_ws(', ', item.REGION, item.CITY, item.ZIPCODE, item.STREET_ADDRESS))"
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("PASSPORT_NUMBER").isNotNull() | col("TAX_CODE").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("PASSPORT_NUMBER").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("PASSPORT_NUMBER"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("TAX_CODE").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("TAX_CODE"),
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
                    col("V_KONTAKTE_ID").isNotNull() | col("FACEBOOK_ID").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("V_KONTAKTE_ID").isNotNull(),
                                struct(
                                    lit("ВКонтакте").alias("title"),
                                    col("V_KONTAKTE_ID").alias("id"),
                                ),
                            ).otherwise(None),
                            when(
                                col("FACEBOOK_ID").isNotNull(),
                                struct(
                                    lit("Facebook").alias("title"),
                                    col("FACEBOOK_ID").alias("id"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("SIGN_UP_DATE"), col("TERMINATION_DATE")),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
        )

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "sex",
            "birth_date",
            "address",
            "phones",
            "documents",
            "socials",
            "actuality",
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
