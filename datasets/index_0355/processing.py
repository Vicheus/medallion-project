from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    trim,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    sex_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0355"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0355/raw/пользователи_Youla.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("sex", sex_udf(trim(col("Пол"))))
            .select("names", "address", "sex", "phones")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
