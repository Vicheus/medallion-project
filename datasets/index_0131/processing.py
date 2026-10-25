from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    flatten,
    coalesce,
    array,
    array_distinct,
    array_compact,
    regexp_replace,
    max,
    concat,
    size,
    first,
    collect_set,
    greatest,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = True
    dataset_code_name: str = "index_0131"
    output_file_count: int = 500

    def parser(self):
        schema_person_1 = StructType(
            [
                StructField("core_person_document_id", StringType(), True),
                StructField("type_id", StringType(), True),
                StructField("src_id", StringType(), True),
                StructField("doc_no", StringType(), True),
                StructField("series_code", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("birthday_dt", StringType(), True),
                StructField("create_dttm", StringType(), True),
                StructField("modify_dttm", StringType(), True),
                StructField("action_ind", StringType(), True),
                StructField("citizenship_id", StringType(), True),
                StructField("gender_id", StringType(), True),
                StructField("person_id", StringType(), True),
                StructField("issue_dt", StringType(), True),
                StructField("issue_place_desc", StringType(), True),
                StructField("birth_place_desc", StringType(), True),
                StructField("birth_date_integrity", StringType(), True),
                StructField("last_name_lat", StringType(), True),
                StructField("first_name_lat", StringType(), True),
                StructField("middle_name_lat", StringType(), True),
                StructField("birth_country_id", StringType(), True),
                StructField("snils_code", StringType(), True),
                StructField("birth_place_region_desc", StringType(), True),
                StructField("birth_place_area_desc", StringType(), True),
                StructField("birth_place_city_desc", StringType(), True),
                StructField("birth_place_locality_desc", StringType(), True),
                StructField("authority_code", StringType(), True),
                StructField("valid_to_dt", StringType(), True),
                StructField("extended_to_dt", StringType(), True),
            ]
        )

        schema_person_2 = StructType(
            [
                StructField("unknown_column_1", StringType(), True),
                StructField("unknown_column_2", StringType(), True),
                StructField("person_id", StringType(), True),
                StructField("unknown_column_3", StringType(), True),
                StructField("unknown_column_4", StringType(), True),
                StructField("issue_place_desc", StringType(), True),
                StructField("unknown_column_5", StringType(), True),
                StructField("address", StringType(), True),
                StructField("unknown_column_6", StringType(), True),
                StructField("unknown_column_7", StringType(), True),
                StructField("unknown_column_8", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("birthday_dt", StringType(), True),
                StructField("unknown_column_9", StringType(), True),
                StructField("gender_id", StringType(), True),
                StructField("birth_place_desc", StringType(), True),
                StructField("unknown_column_10", StringType(), True),
                StructField("unknown_column_11", StringType(), True),
                StructField("unknown_column_12", StringType(), True),
                StructField("unknown_column_13", StringType(), True),
            ]
        )

        schema_docs = StructType(
            [
                StructField("person_id", StringType(), True),
                StructField("doc_no", StringType(), True),
                StructField("series_code", StringType(), True),
                StructField("unknown_column_1", StringType(), True),
                StructField("issue_dt", StringType(), True),
            ]
        )

        schema_address = StructType(
            [
                StructField("core_person_address_id", StringType(), True),
                StructField("invalid", StringType(), True),
                StructField("person_id", StringType(), True),
                StructField("person_state_id", StringType(), True),
                StructField("address_id", StringType(), True),
                StructField("address_type_id", StringType(), True),
                StructField("create_user", StringType(), True),
                StructField("from_dt", StringType(), True),
                StructField("to_dt", StringType(), True),
                StructField("invalid_dt", StringType(), True),
                StructField("user_invalid", StringType(), True),
                StructField("new_address_id", StringType(), True),
                StructField("unstructured", StringType(), True),
                StructField("sono_id", StringType(), True),
                StructField("src_id", StringType(), True),
                StructField("create_dttm", StringType(), True),
                StructField("modify_dttm", StringType(), True),
                StructField("action_ind", StringType(), True),
                StructField("eff_dt", StringType(), True),
                StructField("exp_dt", StringType(), True),
                StructField("person_document_id", StringType(), True),
                StructField("nsi_address_id", StringType(), True),
                StructField("address_status_id", StringType(), True),
                StructField("system_id", StringType(), True),
                StructField("update_needed", StringType(), True),
                StructField("department_id", StringType(), True),
                StructField("source_core_person_address_id", StringType(), True),
                StructField("source_system_id", StringType(), True),
            ]
        )

        df_persons_1 = self.read(
            path="/media/user/Samsung T7/Databases/MVD_REESTR/persons/dd*.csv",
            sep="\t",
            schema=schema_person_1,
            header=False,
        ).replace(";", None)

        print(f"""Raw count persons 1: {df_persons_1.count()}""")

        df_persons_1 = (
            df_persons_1.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_parts_udf(
                                col("first_name_lat"),
                                col("last_name_lat"),
                                col("middle_name_lat"),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birthday_dt"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "sex",
                sex_udf(
                    when(col("gender_id") == "2398891111755027761", "male").otherwise(
                        "female"
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (col("doc_no").isNotNull())
                                & (col("series_code").isNotNull()),
                                document_udf(
                                    lit(None),
                                    concat(col("series_code"), col("doc_no")),
                                    col("issue_dt"),
                                    coalesce(col("valid_to_dt"), col("extended_to_dt")),
                                    col("issue_place_desc"),
                                    col("authority_code"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(lit(None)),
                            when(
                                (col("snils_code").isNotNull()),
                                document_udf(
                                    lit("снилс"),
                                    col("snils_code"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(lit(None)),
                        )
                    )
                ),
            )
            .withColumn(
                "create_dttm", regexp_replace(col("create_dttm"), "+03", "+0300")
            )
            .withColumn(
                "modify_dttm", regexp_replace(col("modify_dttm"), "+03", "+0300")
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("create_dttm"), col("modify_dttm")),
                    lit("%Y-%m-%d %H:%M:%S%z"),
                ),
            )
            .select("person_id", "names", "birth_date", "sex", "documents")
        )

        df_persons_1.persist(StorageLevel.DISK_ONLY)

        df_addresses = (
            self.read(
                path="/media/user/Samsung T7/Databases/MVD_REESTR/addresses/ddd*.csv",
                sep="\t",
                schema=schema_address,
                header=False,
            )
            .replace(";", None)
            .withColumn("address", address_udf(col("unstructured")))
            .groupBy("person_id")
            .agg(collect_set(address_udf(col("unstructured"))).alias("address"))
            .select("person_id", "address")
        )

        df_addresses.persist(StorageLevel.DISK_ONLY)

        df_1 = df_persons_1.join(df_addresses, "person_id", "left").select(
            "person_id", "names", "birth_date", "sex", "address", "documents"
        )

        df_persons_2 = self.read(
            path="/media/user/Samsung T7/Databases/MVD_REESTR/reg_2/d*.csv",
            sep="\t",
            schema=schema_person_2,
            header=False,
        ).replace(";", None)

        df_persons_2.persist(StorageLevel.DISK_ONLY)

        print(f"""Raw count persons 2: {df_persons_2.count()}""")

        df_persons_2_docs = (
            self.read(
                path="/media/user/Samsung T7/Databases/MVD_REESTR/reg_2/persons_docs.csv",
                sep="\t",
                schema=schema_docs,
                header=False,
            )
            .replace(";", None)
            .withColumn(
                "documents",
                when(
                    (col("doc_no").isNotNull()) & (col("series_code").isNotNull()),
                    document_udf(
                        lit(None),
                        concat(col("series_code"), col("doc_no")),
                        col("issue_dt"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("%Y-%m-%d"),
                    ),
                ).otherwise(lit(None)),
            )
            .groupBy("person_id")
            .agg(collect_set(col("documents")).alias("documents"))
            .select("person_id", "documents")
        )

        df_persons_2_docs.persist(StorageLevel.DISK_ONLY)

        df_2 = (
            df_persons_2.join(df_persons_2_docs, "person_id", "left")
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birthday_dt"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "sex",
                sex_udf(
                    when(col("gender_id") == "2398891111755027761", "male").otherwise(
                        "female"
                    )
                ),
            )
            .withColumn("address", array(address_udf(col("address"))))
            .withColumn("actuality", lit(None))
            .filter(col("birth_date").isNull())
            .select(
                "person_id",
                "names",
                "birth_date",
                "sex",
                "address",
                "documents",
                "actuality",
            )
        )

        df_2.persist(StorageLevel.DISK_ONLY)

        df = df_1.unionAll(df_2).coalesce(500)

        df.persist(StorageLevel.DISK_ONLY)

        df = (
            df.groupby(col("names")[0], col("birth_date"))
            .agg(
                first(col("sex")).alias("sex"),
                max(col("actuality")).alias("actuality"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(array_distinct(flatten(collect_set(col("names"))))).alias(
                    "names"
                ),
            )
            .select("names", "sex", "birth_date", "documents", "address")
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .select("names", "documents", "address", "birth_date", "sex")
        )

        df = df.filter(
            col("names").isNotNull() & (col("address").isNotNull())
            | col("documents").isNotNull()
        ).coalesce(500)

        df.persist(StorageLevel.DISK_ONLY).coalesce(500)

        df.groupBy("names", "birth_date").count().orderBy(
            col("count"), ascending=False
        ).limit(5).show()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
