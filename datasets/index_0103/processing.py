from pyspark import StorageLevel
from pyspark.sql.functions import concat_ws, when, col, lit, array, array_compact, size

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0103"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0103/raw/work_2022.csv",
            sep="|",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("Город"), col("Метро")))
            )
            .withColumn(
                "educations",
                when(
                    col("Образование").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                lit(None),
                                col("Образование"),
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
                "works",
                when(
                    (col("Профессия").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                col("Профессия"),
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
                "actuality",
                actuality_date_udf(col("Дата резюме"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "sex",
                "address",
                "works",
                "educations",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )
        df = df.select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "sex",
            "address",
            "works",
            "educations",
            "actuality",
        )
        df.show(n=100, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
