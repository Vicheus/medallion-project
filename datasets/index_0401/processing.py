from pyspark import StorageLevel

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

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE

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
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0401"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        citizenship_blr = ["BY", "BLR"]
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0022/raw/sirena-pboarded_raw.json"
        )
        df = df.filter(col("_source.citizenship").isin(citizenship_blr))

        df.show(n=20, truncate=False)

        df = (
            df.withColumn("names", name_udf(col("_source.full_name")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("_source.birth_date"), lit("%Y-%m-%dT%H:%M:%S.%fZ")),
            )
            .withColumn(
                "phones",
                phone_udf(
                    col("_source.phone_number"), lit(self.dataset_country_code.value)
                ),
            )
            .withColumn("emails", email_udf(col("_source.email")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("_source.passport").isNotNull()
                            & (
                                (col("_source.citizenship") == "RU")
                                | (col("_source.citizenship") == "RUS")
                            ),
                            document_udf(
                                lit(None),
                                col("_source.passport"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "movements",
                array_compact(
                    array(
                        movement_udf(
                            movement_datetime_udf(
                                col("_source.departure_date"),
                                lit("%Y-%m-%dT%H:%M:%S.%fZ"),
                            ),
                            lit(None),
                            lit(None),
                            col("_source.departure_point"),
                            lit(None),
                            lit(None),
                            lit(None),
                            col("_source.arrival_point"),
                            lit("IATA"),
                            ticket_order_datetime_udf(
                                col("_source.booking_date"),
                                lit("%Y-%m-%dT%H:%M:%S.%fZ"),
                            ),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(2),
                            lit(None),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("_source.booking_date"), lit("%Y-%m-%dT%H:%M:%S.%fZ")
                ),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("names") != ""))
        df.cache()

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
                flatten(collect_set("documents")).alias("documents"),
                collect_set("emails").alias("emails"),
                collect_set("phones").alias("phones"),
                flatten(collect_set("movements")).alias("movements"),
                max("actuality").alias("actuality"),
            )
            .withColumn("names", array(col("names")))
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "documents",
                "movements",
                "actuality",
            )
        )

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                first("birth_date").alias("birth_date"),
                max("actuality").alias("actuality"),
                flatten(collect_set("documents")).alias("documents"),
                collect_set("emails").alias("emails"),
                collect_set("phones").alias("phones"),
                flatten(collect_set("movements")).alias("movements"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "documents",
                "movements",
                "actuality",
            )
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                when(
                    size(array_compact(col("movements"))) > 0,
                    array_compact(col("movements")),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("movements").isNotNull()
            )
        )
        df = df.select(
            "names",
            "birth_date",
            "emails",
            "phones",
            "documents",
            "movements",
            "actuality",
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
