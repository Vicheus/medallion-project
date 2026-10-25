from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    split,
    replace,
    lit,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phones_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0007"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,phones"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0007/raw/ru_cdek_client_phone_38m_2022.csv",
            sep=",",
            header=True,
        )

        df = df.dropDuplicates(["name", "phones", "emails"])
        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn(
                "phones",
                phones_udf(
                    array_compact(
                        split(replace(col("phones"), lit("||"), lit(";")), ";")
                    )
                ),
            )
            .withColumn("emails", email_udf(col("emails")))
        )
        df = df.select("names", "emails", "phones")

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
