from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    concat,
    array_distinct,
    array_compact,
    split,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    birth_date_udf,
    sex_udf,
    phones_udf,
    address_udf,
    name_parts_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0110"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0110/raw/inturistru.csv",
            sep="|",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(
                    col("TU_NAMERUS"), col("TU_FNAMERUS"), col("TU_SNAMERUS")
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("TU_BIRTHDAY"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .withColumn("sex", sex_udf(col("TU_SEX")))
            .withColumn("phones", phones_udf(split(col("TU_PHONE"), ",;\t")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("TU_POSTCITY").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("TU_POSTCITY"),
                                        when(
                                            col("TU_POSTINDEX") != "",
                                            col("TU_POSTINDEX"),
                                        ).otherwise(None),
                                        when(
                                            col("TU_POSTSTREET") != "",
                                            concat(lit("ул. "), col("TU_POSTSTREET")),
                                        ).otherwise(None),
                                        when(
                                            col("TU_POSTBILD") != "",
                                            concat(lit("д. "), col("TU_POSTBILD")),
                                        ).otherwise(None),
                                        when(
                                            col("TU_POSTFLAT") != "",
                                            concat(lit("кв. "), col("TU_POSTFLAT")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array(
                    when(
                        col("TU_PASPRUSER").isNotNull()
                        & col("TU_PASPRUNUM").isNotNull(),
                        document_udf(
                            lit("паспорт гражданина рф"),
                            concat(col("TU_PASPRUSER"), col("TU_PASPRUNUM")).alias(
                                "serial"
                            ),
                            col("TU_PASPRUDATE").alias("date_issue"),
                            lit(None).alias("date_expire"),
                            col("TU_PASPRUBYWHOM").alias("authority"),
                            lit(None).alias("authority_code"),
                            lit("%Y-%m-%d %H:%M:%S.%f"),
                        ),
                    ),
                    when(
                        col("TU_PASPORTTYPE").isNotNull()
                        & col("TU_PASPORTNUM").isNotNull(),
                        document_udf(
                            lit("заграничный паспорт гражданина рф"),
                            concat(col("TU_PASPORTTYPE"), col("TU_PASPORTNUM")).alias(
                                "serial"
                            ),
                            col("TU_PASPORTDATE").alias("date_issue"),
                            col("TU_PASPORTDATEEND").alias("date_expire"),
                            col("TU_PASPORTBYWHOM").alias("authority"),
                            lit(None).alias("authority_code"),
                            lit("%Y-%m-%d %H:%M:%S.%f"),
                        ),
                    ),
                    when(
                        col("TU_PASPORTTYPE").isNotNull()
                        & col("TU_PASPORTNUM").isNotNull(),
                        document_udf(
                            lit("заграничный паспорт гражданина рф"),
                            concat(col("TU_PASPORTTYPE"), col("TU_PASPORTNUM")).alias(
                                "serial"
                            ),
                            col("TU_PASPORTDATE").alias("date_issue"),
                            col("TU_PASPORTDATEEND").alias("date_expire"),
                            col("TU_PASPORTBYWHOM").alias("authority"),
                            lit(None).alias("authority_code"),
                            lit("%Y-%m-%d %H:%M:%S.%f"),
                        ),
                    ),
                    when(
                        col("TU_INSURPOLIS").isNotNull(),
                        document_udf(
                            lit("номер страхового полиса"),
                            col("TU_INSURPOLIS").alias("serial"),
                            lit(None).alias("date_issue"),
                            lit(None).alias("date_expire"),
                            lit(None).alias("authority"),
                            lit(None).alias("authority_code"),
                            lit("%Y-%m-%d %H:%M:%S.%f"),
                        ),
                    ),
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("TU_INSURSUM"), df["TU_INSURSUM"])
            )
            .select(
                "names",
                "phones",
                "documents",
                "address",
                "birth_date",
                "sex",
                "raw_metadata",
            )
        )

        df = df.drop_duplicates(
            ["names", "phones", "documents", "address", "birth_date", "sex"]
        )

        df = (
            df.withColumn(
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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("phones").isNotNull())
        )
        df = df.select(
            "names",
            "phones",
            "documents",
            "address",
            "birth_date",
            "sex",
            "raw_metadata",
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
