from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, first, collect_set, size

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0215"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0215/raw/premiumbonus.ru/users.csv",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .select("names", "phones", "emails", "sex", "birth_date")
        )

        df = df.groupBy(["names", "phones"]).agg(
            collect_set(col("emails")).alias("emails"),
            first(col("sex"), ignorenulls=True).alias("sex"),
            first(col("birth_date"), ignorenulls=True).alias("birth_date"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
