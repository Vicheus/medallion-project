from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
    concat,
    concat_ws,
    split,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    phones_udf,
    emails_udf,
    address_udf,
    name_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0394"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0394/raw/carmoney.ru - @StormAndDataBase.csv",
            sep=",",
            header=True,
        )
        df = (
            df.withColumn("names", name_udf(col("full_name")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "documents",
                array(
                    when(
                        col("doc_series").isNotNull() & col("doc_number").isNotNull(),
                        document_udf(
                            lit(None),
                            concat_ws("", col("doc_series"), col("doc_number")),
                            col("doc_issue_date"),
                            lit(None),
                            col("doc_issued_by"),
                            col("doc_issued_by_code"),
                            lit("%Y-%m-%d"),
                        ),
                    ).otherwise(None)
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        concat(
                            array(phone_udf(col("work_phone"))),
                            phones_udf(split(col("phones"), ",")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(array_distinct(emails_udf(split(col("emails"), ",")))),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("company"),
                                    address_udf(col("company_address")),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
        )
        df = df.select(
            "names", "emails", "phones", "address", "birth_date", "documents", "works"
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = df.drop_duplicates()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
