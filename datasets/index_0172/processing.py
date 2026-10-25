from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, coalesce, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0172"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0172/raw/usersAll.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf("full_name"))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("birth_date1", birth_date_udf("birth_date", lit("%Y-%M-%d")))
            .withColumn("birth_date2", birth_date_udf("birth_date", lit("%d.%M.%Y")))
            .withColumn("birth_date", coalesce(col("birth_date1"), col("birth_date2")))
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull() | (col("passport") != ""),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull() | (col("passport") != ""),
                                document_udf(
                                    lit(None),
                                    col("passport"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "phones", "documents", "emails", "address")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
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
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
