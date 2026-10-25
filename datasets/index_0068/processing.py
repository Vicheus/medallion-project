from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    regexp_replace,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0068"

    def parser(self):
        df = self.read(path="corbina-telecom_ru_utf8.csv", sep="|", header=True)

        doc_number_pattern = r"^\d+ \d+"
        doc_issue_date_pattern = r"\d{2}\.\d{2}\.\d{4}"

        df = (
            df.withColumn("names", name_udf(col("fio")))
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%m.%Y")))
            .withColumn(
                "doc_number",
                regexp_replace(
                    regexp_extract(col("document"), doc_number_pattern, 0), " ", ""
                ),
            )
            .withColumn(
                "doc_issue_date",
                regexp_extract(col("document"), doc_issue_date_pattern, 0),
            )
            .withColumn(
                "documents",
                when(
                    col("doc_number").isNotNull(),
                    document_udf(
                        lit(None),
                        col("doc_number"),
                        col("doc_issue_date"),
                        lit(None),
                        col("issued"),
                        lit(None),
                        lit("%d.%m.%Y"),
                    ),
                ),
            )
        )

        df = df.select(
            "names", "emails", "phones", "birth_date", "address", "documents"
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
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
                when(col("documents").isNotNull(), array(col("documents"))).otherwise(
                    None
                ),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
