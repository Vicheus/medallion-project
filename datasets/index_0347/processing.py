from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    concat_ws,
    array,
    array_distinct,
    array_compact,
    size,
    split,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    names_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0347"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0347/raw/клиенты_photographer_ru.csv",
                sep=",",
                header=True,
            )
            .filter(~col("Электронная почта").contains("@bigmir.net"))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        names_udf(
                            array(
                                col("Имя (0)"),
                                col("Имя (1)"),
                                concat_ws(" ", col("Имя (первое)"), col("Фамилия")),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Электронная почта")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("ip", ip_address_udf(split(col("IP адрес"), ",")[0]))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(struct(ip_address_udf(col("ip")).alias("ip"), lit(None))),
                ),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("Информация"), col("Информация"))
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "address",
                "emails",
                "phones",
                "ips",
                "raw_metadata",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
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
