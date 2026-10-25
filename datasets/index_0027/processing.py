from pyspark.sql.functions import when, col, lit, array, array_compact, size
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    birth_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0027"
    output_file_count: int = 20

    def parser(self):
        df_juridical = self.read(
            path="/media/user/SAMSUNG/Databases/index_0027/raw/preprocessed/Юр. лица 2023.06.csv",
            sep=",",
            header=True,
        )
        print(f"df_juridical size: {df_juridical.count()}")
        df_juridical = df_juridical.drop_duplicates(["Название", "ИНН"])
        print(f"df_juridical deduplicated size: {df_juridical.count()}")

        df_juridical = (
            df_juridical.withColumn("names", name_udf(col("Название")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("birth_date", lit(None))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Дата ИП"),
                    df_juridical["Дата ИП"],
                    lit("ОСП"),
                    df_juridical["ОСП"],
                    lit("ИспПр-во"),
                    df_juridical["ИспПр-во"],
                    lit("Причина"),
                    df_juridical["Причина"],
                    lit("Долг"),
                    df_juridical["Долг"],
                ),
            )
            .select("names", "address", "birth_date", "documents", "raw_metadata")
        )

        df_physical = self.read(
            path="/media/user/SAMSUNG/Databases/index_0027/raw/preprocessed/Физ. лица 2023.06.csv",
            sep=",",
            header=True,
        )
        print(f"df_physical size: {df_physical.count()}")
        df_physical = df_physical.drop_duplicates(["ФИО", "ИНН", "СНИЛС", "Паспорт"])

        df_physical = (
            df_physical.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull()
                    | col("СНИЛС").isNotNull()
                    | col("Паспорт").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("СНИЛС").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("СНИЛС"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Паспорт").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Паспорт"),
                                    col("Дата выдачи"),
                                    lit(None),
                                    col("Кем выдан"),
                                    col("Код подразд"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Дата ИП"),
                    df_physical["Дата ИП"],
                    lit("ОСП"),
                    df_physical["ОСП"],
                    lit("Причина"),
                    df_physical["Причина"],
                    lit("Долг"),
                    df_physical["Долг"],
                ),
            )
            .select("names", "address", "birth_date", "documents", "raw_metadata")
        )

        df = df_juridical.unionAll(df_physical)

        df = df.repartition(self.output_file_count)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("documents").isNotNull()))

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
