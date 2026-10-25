from pyspark.sql.functions import (
    col,
    split,
    size,
    round,
    when,
    array_compact,
    array,
    concat_ws,
    collect_list,
    count,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    phone_udf,
    names_udf,
    validate_name_is_person_or_organisation_udf,
)
from parsetron.utils.cosine_similarity import array_distinct_cosine_similarity_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0077"
    output_file_count: int = 10
    output_files_url: str = "s3a://parsetron/output/index_0077"

    def parser(self):

        df = self._spark.read.csv(
            path="s3a://parsetron/index_0077/Numbuster.csv.gz", sep=";", header=True
        )

        repeated_numbers_df = (
            df.groupBy("phone")
            .agg(count("*").alias("count"))
            .filter(col("count") > 50)
            .select("phone")
        )
        repeated_numbers = [
            row["phone"] for row in repeated_numbers_df.select("phone").collect()
        ]

        df = self.read(
            path="s3a://parsetron/index_0077/Numbuster.csv.gz", sep=";", header=True
        ).repartition(25)

        df = (
            df.filter(col("phone").isNotNull() & col("name").isNotNull())
            .groupBy(["phone"])
            .agg(concat_ws(", ", collect_list("name")).alias("name"))
        )

        df = df.withColumn("tags_arr", split(col("name"), ",")).filter(
            (size(col("tags_arr")) < 50) & ~col("phone").isin(repeated_numbers)
        )

        df = (
            df.withColumn(
                "names_from_tags",
                validate_name_is_person_or_organisation_udf(
                    names_udf(split(col("name"), ","))
                ),
            )
            .withColumn(
                "names_quality_score",
                round((size(col("names_from_tags")) / size(col("tags_arr"))), 2),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "names", array_distinct_cosine_similarity_udf(col("names_from_tags"))
            )
        )

        df = df.cache()

        df = df.filter(
            (size(col("tags_arr")) <= 3) & (size(col("names_from_tags")) > 0)
            | ((size(col("tags_arr")) > 3) & (size(col("tags_arr")) <= 20))
            & (col("names_quality_score") >= 0.3)
            | ((size(col("tags_arr")) >= 20) & (col("names_quality_score") >= 0.5))
        )

        df = df.withColumn(
            "names",
            when(
                col("names").isNotNull() & (size(array_compact(col("names"))) > 0),
                array_compact(col("names")),
            ).otherwise(None),
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        print(f"""Count with names > 50: {df.filter(size(col("names"))> 50).count()}""")
        print(
            f"""Count with names > 100: {df.filter(size(col("names"))> 100).count()}"""
        )
        print(
            f"""Count with names > 300: {df.filter(size(col("names"))> 300).count()}"""
        )
        print(
            f"""Count with names > 500: {df.filter(size(col("names"))> 500).count()}"""
        )
        print(
            f"""Count with names > 1000: {df.filter(size(col("names"))> 1000).count()}"""
        )

        df = df.select("names", "phones")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
