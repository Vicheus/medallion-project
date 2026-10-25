from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, array_compact

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0509"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/sib3ka.ru.txt",
            sep=",",
        )
        df = df.drop_duplicates(["ФИО", "Номер телефона"])

        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .select("names", "phones")
        )

        df.cache()

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

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
