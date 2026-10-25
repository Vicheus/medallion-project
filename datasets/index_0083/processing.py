from pyspark.sql.functions import (
    when,
    col,
    array,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0083"

    def parser(self):
        df = self.read(path="Клиенты_НТВ.csv", sep=",", header=True)
        df = (
            df.withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("phones", phone_udf(col("Номер клиента")))
            .withColumn("address", address_udf(col("Город")))
        )

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

        df = df.select("names", "phones", "address")

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
