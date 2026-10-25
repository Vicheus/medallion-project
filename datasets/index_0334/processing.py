from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, regexp_replace

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    phone_udf,
    birth_date_udf,
    email_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0334"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0334/raw/rosakhutor.com_05_2023.txt",
            sep="\t",
            header=True,
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("Почта").isNotNull(),
                    name_udf(
                        regexp_replace(
                            col("ФИО"),
                            regexp_replace(
                                col("Почта"),
                                r"([\.\*\+\?\^\$\(\)\[\]\{\}\|\\])",
                                r"\\\1",
                            ),
                            "",
                        )
                    ),
                ).otherwise(name_udf(col("ФИО"))),
            )
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y.%m.%d"))
            )
            .select("names", "birth_date", "emails", "phones", "address")
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
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
