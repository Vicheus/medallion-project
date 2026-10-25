from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    collect_set,
    to_date,
    year,
    month,
    dayofmonth,
    when,
    lpad,
    concat_ws,
)

from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    birth_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0255"

    def parser(self):
        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0255/raw/dom.ru-spb/spb_clients.csv",
                sep="\t",
                header=True,
                encoding="windows-1251",
            )
            .withColumn("names", name_udf(col("CLIENT_NAME")))
            .withColumn("parsed_birth_date", to_date("BIRTHDATE", "dd.MM.yy"))
            .withColumn(
                "year_fixed_birth_date",
                when(
                    year("parsed_birth_date") > 2000, year("parsed_birth_date") - 100
                ).otherwise(year("parsed_birth_date")),
            )
            .withColumn(
                "formatted_birth_date",
                concat_ws(
                    "-",
                    lpad(dayofmonth("parsed_birth_date").cast("string"), 2, "0"),
                    lpad(month("parsed_birth_date").cast("string"), 2, "0"),
                    "year_fixed_birth_date",
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("formatted_birth_date"), lit("%d-%m-%Y")),
            )
            .withColumn(
                "documents",
                when(
                    (col("KPP").isNotNull() | col("INN").isNotNull()),
                    array_compact(
                        array(
                            when(
                                (col("KPP").isNotNull()),
                                document_udf(
                                    lit("кпп"),
                                    col("KPP"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                (col("INN").isNotNull()),
                                document_udf(
                                    lit("инн"),
                                    col("INN"),
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
                "raw_metadata",
                raw_metadata_udf(
                    lit("ADDRESS_COMMENT"),
                    col("ADDRESS_COMMENT"),
                    lit("BIK"),
                    col("BIK"),
                    lit("SETTLEMENT_ACCOUNT"),
                    col("SETTLEMENT_ACCOUNT"),
                    lit("CORRESPONDENT_ACCOUNT"),
                    col("CORRESPONDENT_ACCOUNT"),
                    lit("BANK_NAME"),
                    col("BANK_NAME"),
                    lit("REG_DOCUMENT"),
                    col("REG_DOCUMENT"),
                    lit("DIRECTOR_NAME"),
                    col("DIRECTOR_NAME"),
                    lit("CONTACT_FIO"),
                    col("CONTACT_FIO"),
                    lit("BANK_NAME"),
                    col("BANK_NAME"),
                ),
            )
            .select(
                "CLIENT_ID",
                "names",
                "formatted_birth_date",
                "birth_date",
                "documents",
                "raw_metadata",
            )
        )

        df_clients.show()

        df_clients.persist(StorageLevel.DISK_ONLY).count()

        schema = StructType(
            [
                StructField("ID", StringType(), True),
                StructField("unknown_column1", StringType(), True),
                StructField("CLIENT_ID", StringType(), True),
                StructField("PHONE", StringType(), True),
                StructField("unknown_column2", StringType(), True),
                StructField("unknown_column3", StringType(), True),
                StructField("unknown_column4", StringType(), True),
                StructField("unknown_column5", StringType(), True),
                StructField("unknown_column6", StringType(), True),
                StructField("unknown_column7", StringType(), True),
                StructField("unknown_column8", StringType(), True),
            ]
        )
        df_phones = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0255/raw/dom.ru-spb/spb_phones.csv",
                sep="\t",
                header=False,
                schema=schema,
                encoding="windows-1251",
            )
            .withColumn("phones", phone_udf(col("PHONE")))
            .groupBy(["CLIENT_ID"])
            .agg(
                array_distinct(array_compact(collect_set(col("phones")))).alias(
                    "phones"
                )
            )
            .select("CLIENT_ID", "phones")
        )

        df_phones.persist(StorageLevel.DISK_ONLY).count()

        df = df_clients.join(df_phones, "CLIENT_ID", "left").select(
            "names", "birth_date", "phones", "documents", "raw_metadata"
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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
