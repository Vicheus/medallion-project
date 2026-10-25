from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    coalesce,
    array_distinct,
    array_compact,
    array,
    collect_set,
    max,
    expr,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0481"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0481/raw/taxsee/splitted/*/*.json"
        ).replace("NULL", None)

        df_data = df.selectExpr("explode(data) as record").select("record.*")
        print(df_data.count())

        df = df.selectExpr("inline(data)")
        df.printSchema()
        df.show(n=20)

        df = df.filter(
            ~col("C_CLFIS").isin(["Иванов Иван Иванович", "Иван Иванов Иванович"])
        )

        df = (
            df.withColumn("names", name_udf(col("C_CLFIS")))
            .withColumn("phones", phone_udf(col("C_NAME")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("C_DATE_LAST"), col("C_DATE_OPEN")),
                    lit("%Y-%m-%dT%H:%M:%S.%f"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("C_BASE"),
                    col("C_BASE"),
                    lit("C_PAY_CODE"),
                    col("C_PAY_CODE"),
                    lit("C_SALDO"),
                    col("C_SALDO"),
                    lit("C_TYPE_ACC"),
                    col("C_TYPE_ACC"),
                ),
            )
            .select("ID_BASE", "names", "phones", "raw_metadata", "actuality")
        )

        df = (
            df.groupBy(["ID_BASE", "names", "phones"])
            .agg(
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .select("names", "phones", "raw_metadata", "actuality")
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
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 10)"))
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
