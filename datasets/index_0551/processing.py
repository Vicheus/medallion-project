from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    flatten,
    regexp_replace,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    phone_udf,
    birth_date_udf,
    address_udf,
    name_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    calc_completeness: bool = True
    dataset_code_name: str = "index_0551"
    validate_invalid_groupping: bool = True

    def parser(self):
        dash_sequence_pattern = r"\s+-{2,}\s+"

        df = (
            self.read(
                path="debitors_oooeos.ru.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array(
                        name_udf(regexp_replace(col("fio"), dash_sequence_pattern, " "))
                    )
                ),
            )
            .withColumn("address", array_compact(array(address_udf(col("address")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .select("names", "address", "phones", "birth_date")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        null_df = df.filter(col("birth_date").isNull())
        not_null_df = df.filter(col("birth_date").isNotNull())

        df = (
            not_null_df.groupBy("names", "birth_date")
            .agg(
                array_distinct(flatten(collect_list("phones"))).alias("phones"),
                array_distinct(flatten(collect_list("address"))).alias("address"),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .unionByName(null_df)
            .distinct()
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
