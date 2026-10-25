from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    flatten,
    size,
    concat_ws,
    concat,
    max,
    first,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    actuality_date_udf,
    birth_date_udf,
    address_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0565"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_people = (
            self.read(
                path="/home/user/Documents/data/index_0565/raw/time.0370.ru people table_clean.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .withColumn(
                "names",
                name_udf(
                    concat_ws(
                        " ",
                        col("first_name"),
                        col("last_name"),
                        col("middle_name"),
                    )
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("birth_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "address", address_udf(concat_ws(" ", col("city"), col("street")))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "doc_code",
                when(col("doc_type") == "0", 0)
                .when(col("doc_type") == "3", 5)
                .otherwise(None),
            )
            .withColumn(
                "documents",
                array_compact(
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
                                lit("%Y-%m-%d"),
                            ),
                        ).otherwise(None),
                        when(
                            col("doc_num").isNotNull(),
                            document_udf(
                                col("doc_type"),
                                concat(col("doc_series"), col("doc_num")),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("%d.%m.%Y"),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names", "birth_date", "address", "phones", "documents", "actuality"
            )
        )

        df_schedule = (
            self.read(
                path="/home/user/Documents/data/index_0565/raw/time.0370.ru schedule_period table_clean.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_udf(col("name")),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("address", lit(None))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("documents", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names", "birth_date", "address", "phones", "documents", "actuality"
            )
        )

        df = df_people.unionAll(df_schedule)

        df_with_phones = df.filter(col("phones").isNotNull())
        df_without_phones = df.filter(col("phones").isNull())

        df_with_phones = (
            df_with_phones.groupBy(["phones"])
            .agg(
                array_distinct(array_compact(collect_set(col("names")))).alias("names"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                array_distinct(array_compact(collect_set(col("address")))).alias(
                    "address"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names", "birth_date", "address", "phones", "documents", "actuality"
            )
        )

        df_without_phones = (
            df_without_phones.withColumn("names", array_compact(array(col("names"))))
            .withColumn("address", array_compact(array(col("address"))))
            .select(
                "names", "birth_date", "address", "phones", "documents", "actuality"
            )
        )

        df = df_with_phones.unionAll(df_without_phones)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("documents").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
