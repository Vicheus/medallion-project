from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    split,
    array_compact,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phones_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0541"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0541/raw/parsed_statement.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("СТРАХОВАТЕЛЬ")))
            .withColumn(
                "phones",
                phones_udf(
                    split(col("ТЕЛЕФОН СТРАХОВАТЕЛЯ"), ","),
                    lit(self.dataset_country_code),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("КОНСУЛЬТАНТ"),
                    col("КОНСУЛЬТАНТ"),
                    lit("СТРАХОВАЯ КОМПАНИЯ"),
                    col("СТРАХОВАЯ КОМПАНИЯ"),
                    lit("ПРОГРАММА СТРАХОВАНИЯ"),
                    col("ПРОГРАММА СТРАХОВАНИЯ"),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("ДАТА ЗАЯВЛЕНИЯ"), lit("%d.%m.%Y"))
            )
            .select("names", "phones", "raw_metadata", "actuality")
        )

        df.show(n=20, truncate=False)

        df = df.dropDuplicates(["phones", "names"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
