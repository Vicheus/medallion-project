from pyspark.sql.functions import (
    col,
    split,
    size,
    round,
    when,
    array_compact,
    array,
    array_size,
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
    dataset_code_name: str = "index_0028"
    output_file_count: int = 50

    def parser(self):

        df = self._spark.read.csv(
            path="s3a://parsetron/index_0028/raw/GetContact_2021_59kk.csv",
            sep="|",
            header=True,
            encoding="windows-1251",
        )

        repeated_numbers_df = (
            df.groupBy("number")
            .agg(count("*").alias("count"))
            .filter(col("count") > 50)
            .select("number")
        )
        repeated_numbers = [
            row["number"] for row in repeated_numbers_df.select("number").collect()
        ]

        df = (
            self._spark.read.csv(
                path="s3a://parsetron/index_0028/raw/GetContact_2021_59kk.csv",
                sep="|",
                header=True,
                encoding="windows-1251",
            )
            .withColumn("tags_arr", split(col("tags"), ","))
            .filter(
                (size(col("tags_arr")) < 50) & ~col("number").isin(repeated_numbers)
            )
        )

        df = (
            df.withColumn("tags_arr", split(col("tags"), ","))
            .withColumn(
                "names_from_tags",
                when(
                    (array_size(col("tags_arr")) >= 30),
                    validate_name_is_person_or_organisation_udf(
                        names_udf(col("tags_arr"))
                    ),
                ).otherwise(names_udf(col("tags_arr"))),
            )
            .withColumn(
                "names_quality_score",
                round((size(col("names_from_tags")) / size(col("tags_arr"))), 2),
            )
            .withColumn("phones", phone_udf(col("number")))
            .withColumn(
                "names", array_distinct_cosine_similarity_udf(col("names_from_tags"))
            )
        )

        df = df.cache()

        df = df.filter(
            (size(col("tags_arr")) <= 3) & (size(col("names_from_tags")) > 0)
            | ((size(col("tags_arr")) > 3) & (size(col("tags_arr")) <= 30))
            & (col("names_quality_score") >= 0.3)
            | ((size(col("tags_arr")) >= 30) & (col("names_quality_score") >= 0.5))
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

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df = df.select("names", "phones")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
