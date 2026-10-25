from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
)
from pyspark import StorageLevel

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    movement_datetime_udf,
    ticket_order_datetime_udf,
)
from parsetron.sections.main.udfs import birth_date_udf, phone_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0020_movements"
    output_file_count: 10

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0020/raw/sirena_rail_tickets_raw/sirena_rail_tickets.csv",
            sep=",",
            header=True,
        )

        print(f"""initial: {df.count()}""")
        df = df.dropDuplicates(["TICKET"])
        print(f"""after ticket dedup: {df.count()}""")

        df = (
            df.withColumn("names", array(name_udf(col("PASS_NAME"))))
            .withColumn(
                "birth_date", birth_date_udf(col("BIRTH_DATE"), lit("%Y-%m-%d"))
            )
            .withColumn("phones", array(phone_udf(col("PHONE"))))
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
                        movement_datetime_udf(col("DEP_DATE")),
                        lit(None),
                        lit(None),
                        col("PORT_FROM"),
                        movement_datetime_udf(col("ARR_DATE")),
                        lit(None),
                        lit(None),
                        col("PORT_TO"),
                        lit("CODE"),
                        ticket_order_datetime_udf(col("TKT_DATE")),
                        col("SEAT"),
                        col("TICKET"),
                        col("TRAIN"),
                        col("CLASS"),
                        lit(4),
                        lit(None),
                    )
                ),
            )
        )

        print(f"DF size: {df.count()}")
        print(
            f"DF with doc size: {df.filter(col('documents')[0]['serial'].isNotNull()).count()}"
        )
        print(
            f"DF without doc size: {df.filter(col('documents')[0]['serial'].isNull()).count()}"
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(array_distinct(col("names")))) > 0,
                    array_compact(array_distinct(col("names"))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(array_distinct(col("documents")))) > 0,
                    array_compact(array_distinct(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                when(
                    size(array_compact(array_distinct(col("movements")))) > 0,
                    array_compact(array_distinct(col("movements"))),
                ).otherwise(None),
            )
        )

        print(f"""after transformation: {df.count()}""")
        df = df.dropDuplicates()
        print(f"""after dedup2: {df.count()}""")

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
        print(f"""after last filter: {df.count()}""")
        df = df.select("names", "birth_date", "phones", "documents", "movements")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
