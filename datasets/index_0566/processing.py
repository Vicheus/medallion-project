from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    collect_set,
    regexp_replace,
    slice,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0566"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_schedule = (
            self.read(
                path="/home/user/Documents/data/index_0566/raw/santalmed.com_history.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("date"),
                    col("date"),
                    lit("procedure"),
                    regexp_replace(col("c4"), ";", " "),
                ),
            )
            .groupBy(["code"])
            .agg(
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                )
            )
            .select("code", "raw_metadata")
        )

        df = (
            self.read(
                path="/home/user/Documents/data/index_0566/raw/santalmed_patients.csv",
                sep=";",
                header=True,
            )
            .withColumn("code", regexp_replace(col("code"), " ", ""))
            .join(df_schedule, "code", "left")
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d")))
            .withColumn("address", address_udf(col("city")))
            .select(
                "names",
                "sex",
                "birth_date",
                "address",
                "phones",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(col("raw_metadata")) > 30, slice("raw_metadata", 1, 30)
                ).otherwise(col("raw_metadata")),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
