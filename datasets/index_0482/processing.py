from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    coalesce,
    array_compact,
    array,
    element_at,
    split,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
    actuality_date_udf,
    raw_metadata_udf,
    email_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0482"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails,documents"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0482/raw/splitted/*/*.json"
        ).replace("NULL", None)

        df = df.selectExpr("explode(result.data) as record").select("record.*")
        print(df.count())

        df.printSchema()
        df.show(n=20)

        df = (
            df.withColumn("names", name_udf(col("C_FIO")))
            .withColumn("address", address_udf(col("C_ADDRESS")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("C_BIRTH"), lit("%Y-%m-%dT%H:%M:%S.%f")),
            )
            .withColumn("phones", phone_udf(col("C_PHONE3")))
            .withColumn("emails", email_udf(col("C_EMAIL")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("C_DATE_UPDATE"), col("C_DATE_START")),
                    lit("%Y-%m-%dT%H:%M:%S.%f"),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("C_PASPORT_N").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("C_PASPORT_N").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("C_PASPORT_N"),
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
            .withColumn(
                "vehicles",
                when(
                    (col("C_AUTO").isNotNull() & (col("C_AUTO") != "")),
                    vehicle_udf(
                        lit(1),
                        col("C_AUTO"),
                        lit(None),
                        lit(None),
                        element_at(split(col("C_AUTO"), " "), -1),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("C_INFO_DISP_SHOW"),
                    col("C_INFO_DISP_SHOW"),
                    lit("C_BASE"),
                    col("C_BASE"),
                    lit("C_AUTO_CLASS"),
                    col("C_AUTO_CLASS"),
                    lit("C_DV_CAME"),
                    col("C_DV_CAME"),
                    lit("C_SEGMENT"),
                    col("C_SEGMENT"),
                    lit("C_STATUS_NAME"),
                    col("C_STATUS_NAME"),
                    lit("C_TYPE_SHOW"),
                    col("C_TYPE_SHOW"),
                    lit("C_DATE_VALIDITY_DOC"),
                    col("C_DATE_VALIDITY_DOC"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "vehicles",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(col("vehicles").isNotNull(), array(col("vehicles"))).otherwise(
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
