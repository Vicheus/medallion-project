from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    concat,
    array_compact,
    size,
    collect_set,
    flatten,
    collect_list,
    array_distinct,
    first,
    coalesce,
    struct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    children_udf,
    actuality_date_udf,
    address_from_parts_udf
)


class ProjectParsetron(Parsetron):
    dataset_code_name: str = "index_0003"
    important_columns_for_filtering: str = "address,phones,emails"
    calc_completeness: bool = False
    write_filtered_rows: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0003/raw/sportmaster-full/sportmaster-part1.txt",
            sep="\t",
            header=True,
        )

        df = (df
        .withColumn(
            "address_str",
            address_udf(
                concat_ws(
                    ", ",
                    when(col("ADDR_CITY").isNotNull(), col("ADDR_CITY")).otherwise(
                        None
                    ),
                    when(col("ADDR_STREET").isNotNull(), col("ADDR_STREET")).otherwise(
                        None
                    ),
                    when(
                        col("ADDR_HOUSE").isNotNull(),
                        concat(lit("д. "), col("ADDR_HOUSE")),
                    ).otherwise(None),
                    when(
                        col("ADDR_KORP").isNotNull(),
                        concat(lit("к. "), col("ADDR_KORP")),
                    ).otherwise(None),
                    when(
                        col("ADDR_STROEN").isNotNull(),
                        concat(lit("стр. "), col("ADDR_STROEN")),
                    ).otherwise(None),
                    when(
                        col("ADDR_KV").isNotNull(), concat(lit("кв. "), col("ADDR_KV"))
                    ).otherwise(None),
                )
            ),
        ).withColumn("address", address_udf(col("address_str"))).withColumn(
            "addresses",
            address_from_parts_udf(
                lit(1),
                lit(None),
                lit(None),
                lit(None),
                col('ADDR_CITY'),
                col('ADDR_STREET'),
                col('ADDR_HOUSE'),
                lit(None),
                col('ADDR_KV'),
                lit(None),
                col('ADDR_KORP'))))
        df = (
            df.withColumn(
                "names",
                name_udf(
                    concat_ws(
                        " ",
                        when(col("LAST_NAME").isNotNull(), col("LAST_NAME")).otherwise(
                            None
                        ),
                        when(
                            col("FIRST_NAME").isNotNull(), col("FIRST_NAME")
                        ).otherwise(None),
                        when(
                            col("MIDDLE_NAME").isNotNull(), col("MIDDLE_NAME")
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("SEX")))
            .withColumn("birth_date", birth_date_udf(col("BIRTHDAY")))
            .withColumn(
                "phones",
                array_compact(
                    array(phone_udf(col("MOBILE_PHONE")), phone_udf(col("HOME_PHONE")))
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn("children", children_udf(col("HAVE_KIDS")))
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("sportmaster app").alias("title"),
                        col("CLIENT_REG_CODE").alias("id"),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("DAT_RECOGNIZE"), col("DAT_PROCESS")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )

        df = df.groupBy(["CLIENT_REG_CODE", "names"]).agg(
            array_distinct(flatten(collect_list("phones"))).alias("phones"),
            collect_set("emails").alias("emails"),
            first(coalesce("sex")).alias("sex"),
            first(coalesce("birth_date")).alias("birth_date"),
            first(coalesce("children")).alias("children"),
            collect_set("address").alias("address"),
            first(coalesce("accounts")).alias("accounts"),
            first(coalesce("actuality")).alias("actuality"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )
        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "birth_date",
            "sex",
            "children",
            "accounts",
            "actuality",
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.dropDuplicates()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
