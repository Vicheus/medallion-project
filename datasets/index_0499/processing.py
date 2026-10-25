from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    split,
    transform,
    concat,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import name_udf, names_udf, phone_udf
from parsetron.sections.educations.udfs import education_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0499"
    output_file_count: int = 10
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0499/raw/kundelik.csv",
                sep="|",
                header=False,
            )
            .withColumn("names", name_udf(col("_c1")))
            .withColumn(
                "phones", phone_udf(col("_c6"), lit(self.dataset_country_code.value))
            )
            .withColumn(
                "educations",
                when(
                    col("_c5").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                col("_c5"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "relations",
                transform(
                    names_udf(split(col("_c3"), ",")),
                    lambda x: concat(x, lit(" Родитель")),
                ),
            )
            .select("names", "phones", "educations", "relations")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
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
                "relations",
                when(col("relations").isNotNull(), array(col("relations"))).otherwise(
                    None
                ),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("educations").isNotNull()
                | col("relations").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
