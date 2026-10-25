from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0254"

    def parser(self):
        df_user = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0254/raw/akson_ru.txt",
                sep="\t",
                header=True,
            )
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(coalesce(col("FullName"), col("FullName2"))))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("Phone")), phone_udf(col("Phone2")))
                    )
                ),
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "works",
                when(
                    col("Company").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("Company"),
                            address_udf(col("Address2")),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("documents", array())
            .select("names", "phones", "address", "emails", "works", "documents")
        )

        df_companies = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0254/raw/akson_ru.txt",
                sep="\t",
                header=True,
            )
            .filter(col("Company").isNotNull())
            .withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("Company")))))
            )
            .withColumn("phones", array())
            .withColumn("address", address_udf(col("Address2")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("works", array())
            .withColumn(
                "documents",
                when(
                    col("INN2").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("INN2").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("INN2"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "address", "emails", "works", "documents")
        )

        df = df_user.unionAll(df_companies)
        df = df.drop_duplicates(["names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
