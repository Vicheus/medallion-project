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
    collect_list,
    first,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    email_udf,
    birth_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0575"
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0575/raw/Eyekraft.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("fullname_ru")))
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%d/%m/%Y")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address_ru")))
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
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .select("names", "birth_date", "phones", "emails", "address", "documents")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_distinct(array_compact(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_distinct(array_compact(collect_list(col("address")))).alias(
                    "address"
                ),
                array_distinct(
                    array_compact(flatten(collect_list(col("documents"))))
                ).alias("documents"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .select("names", "birth_date", "phones", "emails", "address", "documents")
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
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
