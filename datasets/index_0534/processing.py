from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    raw_metadata_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0534"
    calc_completeness: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0534/raw/info_hit_ru.csv",
            sep=";",
        )

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), lit(None)),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("area"),
                    col("area"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "raw_metadata",
            )
        )

        df = df.drop_duplicates(["phones", "emails"])

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
