from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    regexp_replace,
    array_distinct,
    array_compact,
    size,
    concat,
    collect_set,
    first,
    max,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0619"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0619/raw/leads.csv",
            sep=",",
            header=True,
        ).replace("NULL", None)

        df = (
            df.withColumn("snils", regexp_replace(col("snils"), "0|500", ""))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone1")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                        )
                    )
                ),
            )
            .withColumn(
                "addresses",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address1")),
                            address_udf(col("address2")),
                            address_udf(col("address3")),
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
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("passport_serial").isNotNull()
                                & col("passport_number").isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat(
                                        col("passport_serial"), col("passport_number")
                                    ),
                                    col("issued_at"),
                                    col("valid_to"),
                                    col("issued_by"),
                                    col("issued_by_code"),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("work_post").isNotNull() | col("work_place").isNotNull()),
                    array(
                        work_udf(
                            col("work_post"),
                            lit(None),
                            lit(None),
                            col("work_place"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "addresses",
                "documents",
                "works",
                "actuality",
                "snils",
            )
        )

        df_with_snils = df.filter(col("snils").isNotNull() & (col("snils") != ""))
        df_without_snils = (
            df.filter(col("snils").isNull() | (col("snils") == ""))
            .withColumn("names", array_compact(array("names")))
            .withColumn("emails", array_compact(array("emails")))
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "addresses",
                "documents",
                "works",
                "actuality",
            )
        )

        df_with_snils = (
            df_with_snils.groupBy(["snils"])
            .agg(
                array_compact(collect_set(col("names"))).alias("names"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(flatten(collect_set(col("phones")))).alias("phones"),
                array_compact(flatten(collect_set(col("addresses")))).alias(
                    "addresses"
                ),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
                array_compact(flatten(collect_set("works"))).alias("works"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "addresses",
                "documents",
                "works",
                "actuality",
            )
        )

        df = df_with_snils.unionAll(df_without_snils)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "addresses",
                when(size(col("addresses")) > 0, col("addresses")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
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
