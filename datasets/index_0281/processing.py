from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    split,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    emails_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0281"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df_sale_account_admin = (
            self.read(
                path="/home/user/Documents/data/index_0281/raw/avtovelomoto.by/sale_account_admin_output.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("Пользователь")))
            .withColumn("emails", emails_udf(split(col("emails"), " ")))
            .withColumn("actuality", lit(None))
            .withColumn("phones", lit(None))
            .select("names", "emails", "phones", "actuality")
        )

        df_sale_buyers = (
            self.read(
                path="/home/user/Documents/data/index_0281/raw/avtovelomoto.by/sale_buyers.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("Покупатель")))
            .withColumn("emails", array_compact(array(email_udf(col("E-mail")))))
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата регистрации"), lit("%d.%m.%Y %H:%M:%S")),
            )
            .withColumn(
                "phones",
                phone_udf(col("Телефон"), lit(self.dataset_country_code.value)),
            )
            .select("names", "emails", "phones", "actuality")
        )

        df = df_sale_account_admin.unionAll(df_sale_buyers)

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
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
