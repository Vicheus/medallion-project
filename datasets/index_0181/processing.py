from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    concat_ws,
    concat,
    collect_set,
    size,
    array,
    greatest,
    max,
)

from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0181"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0181/raw/rozza_by/rozza.by/*.csv",
                sep=",",
                header=True,
            )
            .filter(
                (col("Имя") != "Клиент")
                & (col("Имя") != " Имя")
                & (col("Имя") != "клиент")
            )
            .withColumn("names", name_udf(col("Имя")))
            .withColumn(
                "phones",
                phone_udf(col("Телефон"), lit(self.dataset_country_code.value)),
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        lit("Минск"),
                        when(
                            col("Улица") != "", concat(lit("ул. "), col("Улица"))
                        ).otherwise(None),
                        when(
                            col("Дом") != "", concat(lit("дом "), col("Дом"))
                        ).otherwise(None),
                        when(
                            col("Подъезд") != "", concat(lit("под. "), col("Подъезд"))
                        ).otherwise(None),
                        when(
                            col("Этаж") != "", concat(lit("под. "), col("Этаж"))
                        ).otherwise(None),
                        when(
                            col("Квартира") != "", concat(lit("эт. "), col("Квартира"))
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("Создан"), col("Последний заказ")), lit("%Y-%m-%d")
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Комментарий"),
                    col("Комментарий"),
                    lit("Канал продаж"),
                    col("Канал продаж"),
                    lit("Филиал"),
                    col("Филиал"),
                ),
            )
            .select("names", "address", "emails", "phones", "actuality", "raw_metadata")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.groupBy(col("phones"))
            .agg(
                collect_set(col("names")).alias("names"),
                collect_set(col("emails")).alias("emails"),
                collect_set(col("address")).alias("address"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
                max("actuality").alias("actuality"),
            )
            .select("names", "address", "emails", "phones", "actuality", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
