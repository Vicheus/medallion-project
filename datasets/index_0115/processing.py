from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    collect_set,
    regexp_extract,
    array_compact,
    flatten,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    birth_date_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0115"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,documents,address"
    calc_completeness: bool = False

    def parser(self):
        passport_regex = r"(\d{4} \d{6})"
        passport_issued_at_regex = r"(\d{2}\.\d{2}\.\d{4})"

        schema_1 = StructType(
            [
                StructField("unknown_field_1", StringType(), True),
                StructField("unknown_field_2", StringType(), True),
                StructField("unknown_field_3", StringType(), True),
                StructField("unknown_field_4", StringType(), True),
                StructField("unknown_field_5", StringType(), True),
                StructField("unknown_field_6", StringType(), True),
                StructField("unknown_field_7", StringType(), True),
                StructField("unknown_field_8", StringType(), True),
                StructField("raw_data", StringType(), True),
                StructField("system_number", StringType(), True),
                StructField("unknown_field_9", StringType(), True),
            ]
        )
        df_pipe = self.read(
            path="/media/user/SAMSUNG/Databases/index_0115/raw/preprocessed/pipe_separated_rows.csv",
            sep="|",
            header=False,
            schema=schema_1,
        )
        df_pipe = (
            df_pipe.withColumn(
                "name",
                regexp_extract(col("raw_data"), r"^(.*?)\s\d{2}\.\d{2}\.\d{4}", 1),
            )
            .withColumn(
                "birth_date",
                regexp_extract(col("raw_data"), r"(\d{2}\.\d{2}\.\d{4})", 1),
            )
            .withColumn("snils", regexp_extract(col("raw_data"), r"(\d{11})$", 1))
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d-%m-%Y"))
            )
            .withColumn(
                "documents",
                when(
                    col("snils").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("snils"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("names", array(col("names")))
            .withColumn("phones", array())
            .withColumn("address", array())
            .select("names", "birth_date", "phones", "documents", "address")
        )

        df_comma = self.read(
            path="/media/user/SAMSUNG/Databases/index_0115/raw/preprocessed/comma_separated_rows_with_names.csv",
            sep=",",
            header=True,
        )
        df_comma = (
            df_comma.withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("patronymic"))
            )
            .withColumn("phones", phone_udf("phone"))
            .withColumn(
                "birth_date", birth_date_udf(col("dateofbirth"), lit("%d-%m-%Y"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "passport_number", regexp_extract("passport", passport_regex, 1)
            )
            .withColumn(
                "passport_issued_at",
                regexp_extract("passport", passport_issued_at_regex, 1),
            )
            .withColumn(
                "documents",
                when(
                    col("passport_number").isNotNull()
                    | col("inn").isNotNull()
                    | col("snils").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport_number"),
                                    col("passport_issued_at"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%M.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn").isNotNull(),
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
                            when(
                                col("snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("snils"),
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
        )
        df_comma = (
            df_comma.filter(~col("names").rlike("Llt|Ltl|Tlt|Lt|L|t"))
            .groupby(["names", "birth_date"])
            .agg(
                when(
                    size(array_compact(collect_set("phones"))) > 0,
                    array_compact(collect_set("phones")),
                )
                .otherwise(None)
                .alias("phones"),
                when(
                    size(array_compact(collect_set("address"))) > 0,
                    array_compact(collect_set("address")),
                )
                .otherwise(None)
                .alias("address"),
                when(
                    size(flatten(collect_set("documents"))) > 0,
                    flatten(collect_set("documents")),
                )
                .otherwise(None)
                .alias("documents"),
            )
            .withColumn("names", array(col("names")))
            .select("names", "birth_date", "phones", "documents", "address")
        )

        df = df_comma.unionAll(df_pipe)

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
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
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
