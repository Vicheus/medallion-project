from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    address_from_parts_udf,
    raw_metadata_udf,
)
from parsetron.sections.educations.udfs import education_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0497"
    output_file_count: int = 10

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0497/raw/trudvsem_ru_2025.txt",
                sep="|",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("patronymic"))
            )
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "addresses",
                address_from_parts_udf(
                    lit(3),
                    lit(None),
                    lit(None),
                    lit(None),
                    col("city"),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                    lit(None),
                ),
            )
            .withColumn(
                "educations",
                when(
                    col("education").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                lit(None),
                                col("education"),
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
                "raw_metadata",
                raw_metadata_udf(
                    lit("position"),
                    col("position"),
                    lit("salary"),
                    col("salary"),
                    lit("schedule"),
                    col("schedule"),
                    lit("skills"),
                    col("skills"),
                    lit("experience"),
                    col("experience"),
                    lit("employment_type"),
                    col("employment_type"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "addresses",
                "phones",
                "emails",
                "educations",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(col("addresses").isNotNull(), array(col("addresses"))).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
