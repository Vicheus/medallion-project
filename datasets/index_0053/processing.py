from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    concat,
    array_compact,
    array_distinct,
    size,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0053"
    output_file_count: int = 10

    def parser(self):
        schema = StructType(
            [
                StructField("registred_subject_id", StringType(), True),
                StructField("actual_subject_id", StringType(), True),
                StructField("status", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("sex", StringType(), True),
                StructField("birthday", StringType(), True),
                StructField("birthplace", StringType(), True),
                StructField("phone_mobile", StringType(), True),
                StructField("passport_series", StringType(), True),
                StructField("passport_number", StringType(), True),
                StructField("passport_date", StringType(), True),
                StructField("passport_issuer", StringType(), True),
                StructField("passport_subdivision", StringType(), True),
                StructField("registred_city", StringType(), True),
                StructField("registred_street", StringType(), True),
                StructField("registred_house", StringType(), True),
                StructField("registred_flat", StringType(), True),
                StructField("registred_postal", StringType(), True),
                StructField("actual_city", StringType(), True),
                StructField("actual_street", StringType(), True),
                StructField("actual_house", StringType(), True),
                StructField("actual_flat", StringType(), True),
                StructField("actual_postal", StringType(), True),
                StructField("INN", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0053/raw/preprocessing/zaymer.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df = (
            df.replace("NULL", None)
            .replace("null", None)
            .replace("Null", None)
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("phones", phone_udf(col("phone_mobile")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("registred_city").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("registred_city"),
                                        when(
                                            col("registred_postal") != "",
                                            col("registred_postal"),
                                        ).otherwise(None),
                                        when(
                                            col("registred_street") != "",
                                            concat(
                                                lit("ул. "), col("registred_street")
                                            ),
                                        ).otherwise(None),
                                        when(
                                            col("registred_house") != "",
                                            concat(lit("д. "), col("registred_house")),
                                        ).otherwise(None),
                                        when(
                                            col("registred_flat") != "",
                                            concat(lit("кв. "), col("registred_flat")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("actual_city").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("actual_city"),
                                        when(
                                            col("actual_postal") != "",
                                            col("actual_postal"),
                                        ).otherwise(None),
                                        when(
                                            col("actual_street") != "",
                                            concat(lit("ул. "), col("actual_street")),
                                        ).otherwise(None),
                                        when(
                                            col("actual_house") != "",
                                            concat(lit("д. "), col("actual_house")),
                                        ).otherwise(None),
                                        when(
                                            col("actual_flat") != "",
                                            concat(lit("кв. "), col("actual_flat")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array(
                    when(
                        col("passport_series").isNotNull()
                        & col("passport_number").isNotNull(),
                        document_udf(
                            lit("паспорт гражданина рф"),
                            concat(
                                col("passport_series"), col("passport_number")
                            ).alias("serial"),
                            col("passport_date").alias("date_issue"),
                            lit(None).alias("date_expire"),
                            col("passport_issuer").alias("authority"),
                            col("passport_subdivision").alias("authority_code"),
                            lit("%Y-%m-%d"),
                        ),
                    ),
                    when(
                        col("INN").isNotNull(),
                        document_udf(
                            lit("инн"),
                            col("INN").alias("serial"),
                            lit(None).alias("date_issue"),
                            lit(None).alias("date_expire"),
                            lit(None).alias("authority"),
                            lit(None).alias("authority_code"),
                        ),
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
        )
        df = df.select("names", "sex", "address", "phones", "birth_date", "documents")
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
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

        df.show(n=100, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
