from pyspark import StorageLevel

from pyspark.sql.functions import col, lit, array_compact, array_distinct, array
from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, birth_date_udf, raw_metadata_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0430"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0430/raw/Wagner Group Full.csv",
            sep=";",
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%m/%d/%Y"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Личный номер"),
                    col("Личный номер"),
                    lit("Позывной"),
                    col("Позывной"),
                    lit("ШО"),
                    col("ШО"),
                    lit("Дата прибытия"),
                    col("Дата прибытия"),
                    lit("Дата начала СБЗ"),
                    col("Дата начала СБЗ"),
                    lit("Дата перехода в 200"),
                    col("Дата перехода в 200"),
                    lit("Дата продления контракта"),
                    col("Дата продления контракта"),
                    lit("Примечания"),
                    col("Примечания"),
                ),
            )
            .select("names", "birth_date", "raw_metadata")
        )

        df = df.filter(col("names").isNotNull())

        df = (
            df.withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn(
                "raw_metadata",
                array_compact(array_distinct(array(col("raw_metadata")))),
            )
            .select("names", "birth_date", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
