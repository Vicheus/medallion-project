from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.educations.udfs import education_udf

from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    normalize_address_batch_udf,
    address_with_type_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0506"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0506/raw/repetit.ru.csv",
                sep="|",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("FullName")))
            .withColumn(
                "birth_date", birth_date_udf(col("BirthDate"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "educations",
                when(
                    col("Education").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                col("Education"),
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
            .withColumn("address", address_udf(col("Address")))
            .withColumn(
                "addresses",
                normalize_address_batch_udf(
                    array(address_with_type_udf(col("address"), lit(2)))
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "address",
                "addresses",
                "educations",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

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
                "addresses",
                when(size(col("addresses")) > 0, col("addresses")).otherwise(None),
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
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
