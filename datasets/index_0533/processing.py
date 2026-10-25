from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    actuality_date_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0533"
    calc_completeness: bool = True

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0533/raw/users.csv", sep=";"
        )

        df = (
            df.withColumn(
                "names",
                name_udf(col("FULL_NAME")),
            )
            .withColumn("birth_date", birth_date_udf(col("BIRTHDATE"), lit("%Y-%m-%d")))
            .withColumn("phones", phone_udf(col("PHONE")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("DATE_MODIFY"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "actuality",
            )
        )

        df = df.drop_duplicates(["phones"])

        df = df.withColumn(
            "names",
            when(
                col("names").isNotNull(), array_compact(array(col("names")))
            ).otherwise(None),
        ).withColumn(
            "phones",
            when(
                col("phones").isNotNull(), array_compact(array(col("phones")))
            ).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
