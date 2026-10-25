from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat,
    regexp_replace,
    flatten,
    max,
    collect_set,
    first,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0310"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0310/raw/aviamed.ru - @StormAndDataBase.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("FULLNAME")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PHONE1")),
                            phone_udf(col("PHONE2")),
                            phone_udf(col("PHONE3")),
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("BDATE"), lit("%Y-%m-%d %H:%M:%S.%f"))
            )
            .withColumn("sex", sex_udf(col("POL")))
            .withColumn("address", address_udf(col("ADDRFULL")))
            .withColumn("emails", email_udf(col("CLMAIL")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("MODIFYDATE"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("PASPSER").isNotNull() & col("PASPNUM").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat(col("PASPSER"), col("PASPNUM")).alias(
                                        "serial"
                                    ),
                                    col("PASPDATE").alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    col("PASPPLACE").alias("authority"),
                                    regexp_replace(
                                        col("PASPDEPCODE"), r"[^0-9]", ""
                                    ).alias("authority_code"),
                                    lit("%Y-%m-%d %H:%M:%S.%f"),
                                ),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("PROFPOST").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("PROFPOST"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "emails",
                "address",
                "works",
                "actuality",
                "documents",
            )
        )

        df = (
            df.groupby(["names", "birth_date"])
            .agg(
                array_compact(array_distinct(flatten(collect_set("documents")))).alias(
                    "documents"
                ),
                array_compact(array_distinct(flatten(collect_set("works")))).alias(
                    "works"
                ),
                array_compact(array_distinct(flatten(collect_set("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(collect_set("emails"))).alias("emails"),
                array_compact(array_distinct(collect_set("address"))).alias("address"),
                first(col("sex")).alias("sex"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "emails",
                "address",
                "works",
                "actuality",
                "documents",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
