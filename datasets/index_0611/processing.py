from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
    regexp_replace,
    concat_ws,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    raw_metadata_udf,
    relations_udf,
    birth_date_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0611"
    validate_invalid_groupping: bool = True
    calc_completeness: bool = True

    def parser(self):
        df1 = (
            self.read(
                path="/media/user/T7/datasets/index_0611/raw/*.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "name_1",
                name_udf(regexp_extract("ФИО 1", r"^(.*?)\s+\d{4}-\d{2}-\d{2}", 1)),
            )
            .withColumn(
                "birth_date_1",
                birth_date_udf(
                    regexp_extract("ФИО 1", r"(\d{4}-\d{2}-\d{2})", 1), lit("%Y-%m-%d")
                ),
            )
            .withColumn("phone_1", phone_udf(col("ТЕЛ 1")))
            .withColumn(
                "vehicle_number1", regexp_replace(col("Номер авто 1"), "Г.Р.З.", "")
            )
            .withColumn(
                "name_2",
                name_udf(regexp_extract("ФИО 2", r"^(.*?)\s+\d{4}-\d{2}-\d{2}", 1)),
            )
            .withColumn(
                "birth_date_2",
                birth_date_udf(
                    regexp_extract("ФИО 2", r"(\d{4}-\d{2}-\d{2})", 1), lit("%Y-%m-%d")
                ),
            )
            .withColumn("phone_2", phone_udf(col("ТЕЛ 1")))
            .withColumn(
                "vehicle_number2", regexp_replace(col("Номер авто 1"), "Г.Р.З.", "")
            )
            .withColumn("МАРКА 1", regexp_replace(col("МАРКА 1"), "марка", ""))
            .withColumn("МАРКА 2", regexp_replace(col("МАРКА 2"), "марка", ""))
        )
        df1_1 = (
            df1.filter(col("name_1") != "Неустановлено Неустановлено Неустановлено")
            .withColumn("names", col("name_1"))
            .withColumn("birth_date", col("birth_date_1"))
            .withColumn("phones", col("phone_1"))
            .withColumn(
                "vehicles",
                when(
                    (col("vehicle_number1").isNotNull() & (col("МАРКА 1") != "")),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("МАРКА 1"),
                            lit(None),
                            lit(None),
                            col("vehicle_number1"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "relations",
                relations_udf(
                    concat_ws(
                        " ",
                        col("name_2"),
                        col("birth_date_2"),
                        col("phone_2"),
                        lit("Участник ДТП"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Место ДТП"),
                    col("Место ДТП"),
                    lit("СТРАХ 1"),
                    col("СТРАХ 1"),
                    lit("ПОВРЕЖД 1"),
                    col("ПОВРЕЖД 1"),
                ),
            )
            .select(
                "names", "birth_date", "phones", "vehicles", "relations", "raw_metadata"
            )
        )

        df1_2 = (
            df1.filter(col("name_2") != "Неустановлено Неустановлено Неустановлено")
            .withColumn("names", col("name_2"))
            .withColumn("birth_date", col("birth_date_2"))
            .withColumn("phones", col("phone_2"))
            .withColumn(
                "vehicles",
                when(
                    (col("vehicle_number2").isNotNull() & (col("МАРКА 2") != "")),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("МАРКА 2"),
                            lit(None),
                            lit(None),
                            col("vehicle_number2"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "relations",
                relations_udf(
                    concat_ws(
                        " ",
                        col("name_1"),
                        col("birth_date_1"),
                        col("phone_1"),
                        lit("Участник ДТП"),
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Место ДТП"),
                    col("Место ДТП"),
                    lit("СТРАХ 2"),
                    col("СТРАХ 2"),
                    lit("ПОВРЕЖД 2"),
                    col("ПОВРЕЖД 2"),
                ),
            )
            .select(
                "names", "birth_date", "phones", "vehicles", "relations", "raw_metadata"
            )
        )

        df = (
            df1_1.unionAll(df1_2)
            .groupBy(["names", "birth_date"])
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(flatten(collect_set(col("vehicles")))).alias("vehicles"),
                array_compact(collect_set(col("relations"))).alias("relations"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
            )
            .select(
                "names", "birth_date", "phones", "vehicles", "relations", "raw_metadata"
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("relations").isNotNull()
                | col("vehicles").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
