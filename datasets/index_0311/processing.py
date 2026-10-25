from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    concat,
    size,
    split,
)

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phones_udf,
    emails_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0311"
    output_file_count: int = 5

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0311/raw/preprocessing/output.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("birth_place", address_udf(col("birth_place")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("birth_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("emails", emails_udf(split(col("emails"), ",")))
            .withColumn("phones", phones_udf(split(col("phones"), ",")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address_1")),
                            address_udf(col("address_2")),
                            address_udf(col("address_3")),
                            address_udf(col("address_4")),
                            address_udf(col("address_5")),
                            address_udf(col("address_6")),
                            address_udf(col("address_7")),
                            address_udf(col("address_8")),
                            address_udf(col("address_9")),
                            address_udf(col("address_10")),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
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
                            ).otherwise(None),
                            when(
                                col("inn_1").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn_1"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn_2").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn_2"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn_3").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn_3"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("passport_num_1").isNotNull()
                                & col("passport_series_1").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("passport_series_1"), col("passport_num_1")
                                    ),
                                    col("passport_issued_at_1"),
                                    lit(None),
                                    col("passport_issuer_1"),
                                    col("passport_issuer_code_1"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("passport_num_2").isNotNull()
                                & col("passport_series_2").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("passport_series_2"), col("passport_num_2")
                                    ),
                                    col("passport_issued_at_2"),
                                    lit(None),
                                    col("passport_issuer_2"),
                                    col("passport_issuer_code_2"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("passport_num_3").isNotNull()
                                & col("passport_series_3").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("passport_series_3"), col("passport_num_3")
                                    ),
                                    col("passport_issued_at_3"),
                                    lit(None),
                                    col("passport_issuer_3"),
                                    col("passport_issuer_code_3"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "vehicles",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (
                                    col("vehicle_reg_num_1").isNotNull()
                                    & (col("vehicle_reg_num_1") != "")
                                )
                                | (
                                    col("vehicle_vin_num_1").isNotNull()
                                    & (col("vehicle_vin_num_1") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_1"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_1"),
                                    col("vehicle_vin_num_1"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_2").isNotNull()
                                    & (col("vehicle_reg_num_2") != "")
                                )
                                | (
                                    col("vehicle_vin_num_2").isNotNull()
                                    & (col("vehicle_vin_num_2") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_2"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_2"),
                                    col("vehicle_vin_num_2"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_3").isNotNull()
                                    & (col("vehicle_reg_num_3") != "")
                                )
                                | (
                                    col("vehicle_vin_num_3").isNotNull()
                                    & (col("vehicle_vin_num_3") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_3"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_3"),
                                    col("vehicle_vin_num_3"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_4").isNotNull()
                                    & (col("vehicle_reg_num_4") != "")
                                )
                                | (
                                    col("vehicle_vin_num_4").isNotNull()
                                    & (col("vehicle_vin_num_4") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_4"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_4"),
                                    col("vehicle_vin_num_4"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_5").isNotNull()
                                    & (col("vehicle_reg_num_5") != "")
                                )
                                | (
                                    col("vehicle_vin_num_5").isNotNull()
                                    & (col("vehicle_vin_num_5") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_5"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_5"),
                                    col("vehicle_vin_num_5"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_6").isNotNull()
                                    & (col("vehicle_reg_num_6") != "")
                                )
                                | (
                                    col("vehicle_vin_num_6").isNotNull()
                                    & (col("vehicle_vin_num_6") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_6"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_6"),
                                    col("vehicle_vin_num_6"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_7").isNotNull()
                                    & (col("vehicle_reg_num_7") != "")
                                )
                                | (
                                    col("vehicle_vin_num_7").isNotNull()
                                    & (col("vehicle_vin_num_7") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_7"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_7"),
                                    col("vehicle_vin_num_7"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_8").isNotNull()
                                    & (col("vehicle_reg_num_8") != "")
                                )
                                | (
                                    col("vehicle_vin_num_8").isNotNull()
                                    & (col("vehicle_vin_num_8") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_8"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_8"),
                                    col("vehicle_vin_num_8"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_9").isNotNull()
                                    & (col("vehicle_reg_num_9") != "")
                                )
                                | (
                                    col("vehicle_vin_num_9").isNotNull()
                                    & (col("vehicle_vin_num_9") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_9"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_9"),
                                    col("vehicle_vin_num_9"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                (
                                    col("vehicle_reg_num_10").isNotNull()
                                    & (col("vehicle_reg_num_10") != "")
                                )
                                | (
                                    col("vehicle_vin_num_10").isNotNull()
                                    & (col("vehicle_vin_num_10") != "")
                                ),
                                vehicle_udf(
                                    lit(1),
                                    col("vehicle_model_10"),
                                    lit(None),
                                    lit(None),
                                    col("vehicle_reg_num_10"),
                                    col("vehicle_vin_num_10"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .select(
                "names",
                "birth_date",
                "birth_place",
                "phones",
                "emails",
                "address",
                "documents",
                "vehicles",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
