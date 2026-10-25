from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    expr,
    array_compact,
    struct,
    regexp_extract,
    concat,
    concat_ws,
    array_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0540"

    def parser(self):
        month_expr = expr(
            """
            CASE
                WHEN approve_date LIKE 'январь%' THEN '01'
                WHEN approve_date LIKE 'февраль%' THEN '02'
                WHEN approve_date LIKE 'март%' THEN '03'
                WHEN approve_date LIKE 'апрель%' THEN '04'
                WHEN approve_date LIKE 'май%' THEN '05'
                WHEN approve_date LIKE 'июнь%' THEN '06'
                WHEN approve_date LIKE 'июль%' THEN '07'
                WHEN approve_date LIKE 'август%' THEN '08'
                WHEN approve_date LIKE 'сентябрь%' THEN '09'
                WHEN approve_date LIKE 'октябрь%' THEN '10'
                WHEN approve_date LIKE 'ноябрь%' THEN '11'
                WHEN approve_date LIKE 'декабрь%' THEN '12'
            END
        """
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0540/raw/m-food_levelkitchen_p-food_sample.csv",
                sep=",",
                header=True,
            )
            .withColumn("approve_date", col("Срок действия"))
            .withColumn("month", month_expr)
            .withColumn("year", regexp_extract(col("approve_date"), r"(\d{4})", 1))
            .withColumn("card_mm_yyyy", concat(col("month"), expr("'.'"), col("year")))
            .withColumn("names", name_udf(col("Имя")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("E-Mail")))
            .withColumn("card_number", col("Карта"))
            .withColumn("ip", ip_address_udf(col("IP")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("Страна"), col("Город")))
            )
            .withColumn(
                "financials",
                when(
                    col("card_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("card_number").isNotNull(),
                                struct(
                                    col("Банк").alias("title"),
                                    col("card_number").alias("card_number"),
                                    col("card_mm_yyyy").alias("date_expire"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("Дата/время подтверждения"),
                                lit("%d.%m.%Y %H:%M:%S"),
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Дата/время подтверждения"), lit("%d.%m.%Y %H:%M:%S")
                ),
            )
            .select(
                "names", "phones", "emails", "address", "ips", "financials", "actuality"
            )
        )

        df.show(n=20, truncate=False)

        df = df.dropDuplicates(["phones", "emails", "names"])

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(array_distinct(col("ips")))) > 0,
                    array_compact(array_distinct(col("ips"))),
                ).otherwise(None),
            )
            .withColumn(
                "financials",
                when(
                    size(array_compact(array_distinct(col("financials")))) > 0,
                    array_compact(array_distinct(col("financials"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
