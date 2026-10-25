from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
    flatten,
    collect_set,
    max,
    regexp_extract,
    expr
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, birth_date_udf, phone_udf, actuality_date_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_gibdd_spb"
    calc_completeness: bool = False
    output_file_count: int = 10
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(path="/media/user/SAMSUNG/Databases/index_0500/raw/gibdd/ГИБДД СПБ 2018-2019 Excel 1,2КК./Excel/*.csv", sep=";", header=True)
            
        
        df_companies = df.filter(col('Наименование предприятия').isNotNull() & col('ФИО').isNull())
        df_persons = df.filter(col('ФИО').isNotNull())
        
        df_persons = (
            df_persons
            .withColumn('names', name_udf(regexp_extract(col('ФИО'), r'^(\S+\s+\S+\s+\S+)', 1)))
            .withColumn('birth_date', birth_date_udf(col('Дата рождения'), lit('%m/%d/%Y')))
            .withColumn(
                "documents",
                when(
                    col("Док удост лич пасп").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("Док удост лич пасп").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("Док удост лич пасп"),
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
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "vehicles",
                when(
                    col("Рег знак").isNotNull() | col("VIN").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                vehicle_udf(
                                    lit(1),
                                    col("Модель"),
                                    col("Год выпуска").cast("int"),
                                    col("Цвет"),
                                    col("Рег знак"),
                                    col("VIN"),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select("names", "birth_date", "phones", "vehicles", "documents")
        )

        df_persons = (
            df_persons
            .groupBy(col("documents")[0]["serial"])
            .agg(
                array_compact(array_distinct(collect_set("names"))).alias("names"),
                array_compact(array_distinct(collect_set("phones"))).alias("phones"),
                array_compact(array_distinct(flatten(collect_set("vehicles")))).alias("vehicles"),
                array_compact(array_distinct(flatten(collect_set("documents")))).alias("documents"),
                max(col("birth_date")).alias("birth_date")
            )
            .select("names", "birth_date", "phones", "vehicles", "documents")
        )

        df_companies = (
            df_companies
            .withColumn('names', name_udf(col('Наименование предприятия')))
            .withColumn('birth_date', lit(None))
            .withColumn(
                "documents",
                when(
                    col("ИНН предприятия").isNotNull() | col("ОГРН предприятия").isNotNull() | col("КПП предприятия").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН предприятия").isNotNull(),
                                document_udf(
                                    lit('инн'),
                                    col("ИНН предприятия"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("ОГРН предприятия").isNotNull(),
                                document_udf(
                                    lit('огрн'),
                                    col("ОГРН предприятия"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("КПП предприятия").isNotNull(),
                                document_udf(
                                    lit('кпп'),
                                    col("КПП предприятия"),
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
            .withColumn("phones", phone_udf(col("Телефон предприятия")))
            .withColumn(
                "vehicles",
                when(
                    col("Рег знак").isNotNull() | col("VIN").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                vehicle_udf(
                                    lit(1),
                                    col("Модель"),
                                    col("Год выпуска").cast("int"),
                                    col("Цвет"),
                                    col("Рег знак"),
                                    col("VIN"),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select("names", "birth_date", "phones", "vehicles", "documents")
        )

        df_companies = (
            df_companies
            .groupBy(col("documents")[0]["serial"])
            .agg(
                array_compact(array_distinct(collect_set("names"))).alias("names"),
                array_compact(array_distinct(collect_set("phones"))).alias("phones"),
                array_compact(array_distinct(flatten(collect_set("vehicles")))).alias("vehicles"),
                array_compact(array_distinct(flatten(collect_set("documents")))).alias("documents"),
                max(col("birth_date")).alias("birth_date")
            )
            .select("names", "birth_date", "phones", "vehicles", "documents")
        )

        df = df_companies.unionAll(df_persons)

        df = (
            df
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "vehicles", when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None)
            )
            .withColumn(
                "documents", when(size(col("documents")) > 0, col("documents")).otherwise(None)
            )
            .withColumn("ips", expr("slice(vehicles, 1, 15)"))
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull() | col("vehicles").isNotNull() | col("documents").isNotNull()))

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
