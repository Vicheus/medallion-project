from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    first,
    flatten,
    collect_set,
    array_compact,
    max,
)
from pyspark import StorageLevel

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_datetime_udf,
    ticket_order_datetime_udf,
)
from parsetron.sections.main.udfs import (
    birth_date_udf,
    phone_udf,
    name_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0020"
    output_file_count: 5

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0020/raw/sirena_rail_tickets_raw/sirena_rail_tickets.csv",
            sep=",",
            header=True,
        )

        df = df.dropDuplicates(["TICKET"])
        df = df.filter(
            (col("PASS_NAME").isNotNull() & col("BIRTH_DATE").isNotNull())
            | (col("PASS_NAME").isNotNull() & col("PASS_DOC").isNotNull())
        )

        df_with_many_movements = (
            df.groupBy("PASS_DOC")
            .count()
            .filter((col("count") == 1))
            .select("PASS_DOC")
        )
        print(f"Size with many movements: {df_with_many_movements.count()}")

        doc_nums_with_many_movements = df_with_many_movements.rdd.flatMap(
            lambda x: x
        ).collect()
        print(f"Df size before filter out: {df.count()}")
        df = df.filter(df["PASS_DOC"].isin(doc_nums_with_many_movements))
        print(f"Df size after filter out: {df.count()}")

        df = (
            df.withColumn("names", name_udf(col("PASS_NAME")))
            .withColumn(
                "birth_date", birth_date_udf(col("BIRTH_DATE"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", phone_udf(col("PHONE")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("PASS_DOC").isNotNull(),
                            document_udf(
                                lit(None),
                                col("PASS_DOC"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "movements",
                array(
                    movement_udf(
                        movement_datetime_udf(
                            col("DEP_DATE"), lit("%Y-%m-%d %H:%M:%S")
                        ),
                        lit(None),
                        lit(None),
                        col("PORT_FROM"),
                        lit(None),
                        lit(None),
                        lit(None),
                        col("PORT_TO"),
                        lit("CODE"),
                        ticket_order_datetime_udf(
                            col("TKT_DATE"), lit("%Y-%m-%d %H:%M:%S")
                        ),
                        lit(None),
                        col("SEAT"),
                        col("TICKET"),
                        col("TRAIN"),
                        col("CLASS"),
                        lit(4),
                        lit(None),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("TKT_DATE"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )

        print(f"DF size: {df.count()}")
        print(
            f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}"
        )
        print(
            f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}"
        )

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .groupby(["names", "birth_date"])
            .agg(
                when(size(collect_set("phones")) > 0, collect_set("phones"))
                .otherwise(None)
                .alias("phones"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array(col("names")))
            .select(
                "names", "birth_date", "phones", "documents", "movements", "actuality"
            )
        )

        df_without_doc.show(n=1000, truncate=False)

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                first("birth_date").alias("birth_date"),
                max("actuality").alias("actuality"),
                when(size(collect_set("phones")) > 0, collect_set("phones"))
                .otherwise(None)
                .alias("phones"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
            )
            .select(
                "names", "birth_date", "phones", "documents", "movements", "actuality"
            )
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "movements",
                when(size(col("movements")) > 0, col("movements")).otherwise(None),
            )
        )

        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("movements").isNotNull()
            )
        )
        df = df.select(
            "names", "birth_date", "phones", "documents", "movements", "actuality"
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
