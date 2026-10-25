from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0521"
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0521/raw/helix.ru_2023/helix.ru_2023.txt",
                sep=",",
            )
            .withColumn(
                "names",
                name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество")),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d %H:%m:%s")),
            )
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("sex", sex_udf(col("Пол")))
            .select("names", "birth_date", "sex", "emails")
        )

        df = df.withColumn(
            "names",
            when(col("names").isNotNull(), array(col("names"))).otherwise(None),
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
