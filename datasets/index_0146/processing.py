from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat_ws,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0146"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0146/raw/rpn.gov.ru_28K.csv",
            sep="|",
            header=True,
        )

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("patronymic"))
            )
            .withColumn("phones", phone_udf("tel"))
            .withColumn("emails", email_udf("email"))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("address_index"), col("address_line"))),
            )
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull()
                    | col("inn").isNotNull()
                    | col("snils").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    col("passport_issue_date"),
                                    lit(None),
                                    col("passport_issuer"),
                                    lit(None),
                                    lit("%Y-%M-%d"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
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
                        )
                    ),
                ).otherwise(None),
            )
            .select("names", "emails", "phones", "address", "documents")
        )

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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df = df.select("names", "emails", "address", "phones", "documents")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
