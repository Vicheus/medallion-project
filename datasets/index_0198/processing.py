from pyspark.sql.functions import (
    col,
    size,
    when,
    array_compact,
    array,
    lit,
    array_distinct,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    phone_udf,
    name_udf,
    email_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0198"

    def parser(self):

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0198/raw/raw/users.csv",
            sep=";",
            header=True,
        )

        df = (
            df.withColumn("names", name_udf(col("Покупатель_Полное_Имя")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("Телефон")),
                            phone_udf(col("Покупатель_Логин")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("E-mail")), email_udf(col("Покупатель_Логин"))
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Кол-во полностью оплаченных заказов"),
                    col("Кол-во полностью оплаченных заказов"),
                    lit("Кол-во частично оплаченных заказов"),
                    col("Кол-во частично оплаченных заказов"),
                    lit("Сумма полученных оплат"),
                    col("Сумма полученных оплат"),
                ),
            )
        )
        df = df.cache()

        df = (
            df.groupBy(["Покупатель_Логин"])
            .agg(
                array_compact(collect_set(col("names"))).alias("names"),
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
            )
            .select("names", "phones", "emails", "raw_metadata")
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
