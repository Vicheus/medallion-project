from pyspark.sql.functions import (
    when,
    col,
    array,
    array_distinct,
    array_compact,
)
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
)
from pyspark import StorageLevel


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0508"
    output_file_count: int = 3

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0508/raw/rbt_ru_2022.csv",
                header=True,
                sep=";",
            )
            .withColumn("names", name_udf(col("Фамилия Имя")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("e-mail")))
            .select("names", "phones", "emails")
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(),
                    array_compact(array_distinct(array(col("emails")))),
                ).otherwise(None),
            )
        )
        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )
        df = df.select("names", "phones", "emails")
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
