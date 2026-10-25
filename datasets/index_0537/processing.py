from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    collect_set,
    size,
    max,
)

from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0537"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY
    validate_invalid_groupping: bool = True

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0537/raw/customers.csv",
                sep=";",
                header=True,
            )
            .replace("-", None)
            .withColumn("names", name_udf(col("Имя клиента")))
            .withColumn(
                "phones", phone_udf(col("Телефон"), lit(self.dataset_country_code))
            )
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Последнее обращение"), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("names", "phones", "emails", "actuality")
        )

        df = df.filter(col("phones").isNotNull())

        df = df.groupBy(["phones"]).agg(
            array_distinct(array_compact(collect_set(col("names")))).alias("names"),
            array_distinct(array_compact(collect_set(col("emails")))).alias("emails"),
            max("actuality").alias("actuality"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
