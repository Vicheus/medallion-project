from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    array_distinct,
    split,
    collect_set,
    flatten,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    raw_metadata_udf,
    email_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0404"
    output_file_count: int = 20
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0404/raw/all_contacts.json"
        )

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("name")), name_udf(col("contactName")))
                    )
                ),
            )
            .withColumn("phones", phone_udf(split(col("chatId"), "@")[0]))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("category"),
                    col("category"),
                    lit("description"),
                    col("description"),
                    lit("lastSeen"),
                    col("lastSeen"),
                ),
            )
            .select("names", "phones", "emails", "raw_metadata")
        )

        df = df.filter(col("phones").isNotNull())

        df = df.repartition(self.output_file_count)

        df = (
            df.groupby(["phones"])
            .agg(
                array_compact(collect_set("emails")).alias("emails"),
                array_compact(flatten(collect_set("names"))).alias("names"),
                array_compact(collect_set("raw_metadata")).alias("raw_metadata"),
            )
            .withColumn("phones", array(col("phones")))
            .select("names", "phones", "emails", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
