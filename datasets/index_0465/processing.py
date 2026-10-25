from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    size,
    array_compact,
    array_distinct,
    concat_ws,
    array,
)
from parsetron import Parsetron

from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    raw_metadata_udf,
    phone_udf,
    address_udf,
    birth_date_udf,
    actuality_date_udf,
    relations_udf,
    sex_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0465"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0465/raw/nlstar_com_2022/managers.txt",
            sep="\t",
            header=True,
        )

        df_persons = (
            df.withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("name2"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("phone2")))
                    )
                ),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("zipcode"),
                        col("country"),
                        col("region"),
                        col("city"),
                        col("street"),
                        col("house"),
                        col("room"),
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("bdate"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("co_marriage_date"),
                    col("co_marriage_date"),
                    lit("co_marriage_number"),
                    col("co_marriage_number"),
                    lit("co_marriage_deal"),
                    col("co_marriage_deal"),
                    lit("sponsor_id"),
                    col("sponsor_id"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_change"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "relations",
                when(
                    col("co_surname").isNotNull(),
                    array(
                        when(
                            col("co_surname").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_parts_udf(
                                        col("co_name"),
                                        col("co_surname"),
                                        col("co_name2"),
                                    ),
                                    birth_date_udf(col("co_birthday"), lit("%Y-%m-%d")),
                                    lit("супруг\супруга"),
                                )
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "relations",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_persons2 = (
            df.withColumn(
                "names",
                name_parts_udf(col("co_name"), col("co_surname"), col("co_name2")),
            )
            .withColumn("emails", email_udf(col("co_mail")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("co_phone")), phone_udf(col("co_phone2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("co_address")))
            .withColumn(
                "birth_date", birth_date_udf(col("co_birthday"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("co_sex")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("co_marriage_date"),
                    col("co_marriage_date"),
                    lit("co_marriage_number"),
                    col("co_marriage_number"),
                    lit("co_marriage_deal"),
                    col("co_marriage_deal"),
                    lit("sponsor_id"),
                    col("sponsor_id"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("date_change"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("co_passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("co_passport"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d %H:%M:%S"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "relations",
                when(
                    col("co_surname").isNotNull(),
                    array(
                        when(
                            col("co_surname").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    name_parts_udf(
                                        col("name"), col("surname"), col("name2")
                                    ),
                                    birth_date_udf(col("bdate"), lit("%Y-%m-%d")),
                                    lit("супруг\супруга"),
                                )
                            ),
                        ).otherwise(None)
                    ),
                ).otherwise(array()),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "relations",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_persons.unionAll(df_persons2)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "relations",
                when(size(col("relations")) > 0, col("relations")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("address").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
