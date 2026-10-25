from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    name_udf,
)
from parsetron.utils.translit import transliterate_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0159"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0159/raw/sravni.ru_db/sravni.ru_db.txt",
                sep="|",
                header=True,
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "name_transliterated",
                transliterate_udf(col("names"), lit("ru"), lit(False), lit(True)),
            )
            .withColumn(
                "names",
                array_distinct(
                    array_compact(
                        array(col("names"), name_udf(col("name_transliterated")))
                    )
                ),
            )
            .select("names", "phones", "birth_date")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.withColumn(
            "names", when(size(col("names")) > 0, col("names")).otherwise(None)
        ).withColumn(
            "phones",
            when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
