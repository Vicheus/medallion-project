from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    concat,
    regexp_extract,
    slice,
    split,
    regexp_replace,
    from_unixtime,
    collect_list,
    max,
    flatten,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0615"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0615/raw/abonent_rialcom.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "clean_name",
                concat_ws(
                    " ",
                    slice(split(regexp_replace("full_name", r"\s+", " "), " "), 1, 3),
                ),
            )
            .withColumn("last_change_date", from_unixtime(col("last_change_date")))
            .withColumn(
                "mobile_telephone", regexp_replace(col("mobile_telephone"), ";", ",")
            )
            .withColumn("mobile_telephones", split(col("mobile_telephone"), ","))
            .withColumn(
                "mobile_telephone_1",
                when(size(col("mobile_telephones")) > 0, col("mobile_telephones")[0]),
            )
            .withColumn(
                "mobile_telephone_2",
                when(size(col("mobile_telephones")) > 1, col("mobile_telephones")[1]),
            )
            .withColumn("names", name_udf(col("clean_name")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("juridical_address")),
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("actual_address"),
                                    when(
                                        col("building").isNotNull(),
                                        concat(lit("д. "), col("building")),
                                    ).otherwise(None),
                                    when(
                                        col("flat_number").isNotNull(),
                                        concat(lit("кв. "), col("flat_number")),
                                    ).otherwise(None),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("work_telephone")),
                            phone_udf(col("mobile_telephone_1")),
                            phone_udf(col("mobile_telephone_2")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("series", regexp_extract("comments", r"^(\d{4})", 1))
            .withColumn("number", regexp_extract("comments", r"^\d{4}\s+(\d{6})", 1))
            .withColumn(
                "issued_by",
                regexp_extract(
                    "comments", r"^\d{4}\s+\d{6}\s+(.*)\s+\d{2}\.\d{2}\.\d{4}$", 1
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("series").isNotNull() & col("number").isNotNull(),
                            document_udf(
                                lit("паспорт гражданина рф"),
                                concat(col("series"), col("number")).alias("serial"),
                                lit(None).alias("date_issue"),
                                lit(None).alias("date_expire"),
                                col("issued_by").alias("authority"),
                                lit(None).alias("authority_code"),
                                lit("%d.%m.%Y"),
                            ),
                        ),
                        when(
                            col("tax_number").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("tax_number").alias("serial"),
                                lit(None).alias("date_issue"),
                                lit(None).alias("date_expire"),
                                lit(None).alias("authority"),
                                lit(None).alias("authority_code"),
                                lit("%d.%m.%Y"),
                            ),
                        ),
                        when(
                            col("kpp_number").isNotNull(),
                            document_udf(
                                lit("кпп"),
                                col("kpp_number").alias("serial"),
                                lit(None).alias("date_issue"),
                                lit(None).alias("date_expire"),
                                lit(None).alias("authority"),
                                lit(None).alias("authority_code"),
                                lit("%d.%m.%Y"),
                            ),
                        ),
                    )
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    struct(
                        lit("Интернет провайдер Риалком").alias("title"),
                        lit("http://rialcom.ru").alias("link"),
                        col("login").alias("login"),
                        col("password").alias("password"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("last_change_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "address",
                "phones",
                "emails",
                "documents",
                "accounts",
                "actuality",
                "mobile_telephone_1",
            )
        )

        df = (
            df.groupBy(["names", "mobile_telephone_1"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_list(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_list(col("phones"))))
                ).alias("phones"),
                array_compact(array_distinct(collect_list(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_list(col("accounts")))).alias(
                    "accounts"
                ),
                array_compact(
                    array_distinct(flatten(collect_list(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "address",
                "phones",
                "emails",
                "documents",
                "accounts",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
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
