from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    split,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0339"
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0339/raw/Клиенты_acko_ru_09_2023_2.csv",
                sep=",",
                header=True,
            )
            .filter(
                ~col("ФИО").isin(
                    [
                        "Chery Tiggo",
                        "Chevrolet Cruze",
                        "Chevrolet Lacetti",
                        "Chevrolet Niva",
                        "Kia Spectra",
                        "Nissan Almera",
                        "Renault Logansr",
                        "Renault Sandero",
                        "Subaru Impreza",
                        "Toyota Corolla",
                        "Toyota Toyo Ace",
                        "А А А",
                        "А А П",
                        "Ааа Аа А",
                        "Ааа Аа Ааа",
                        "Ааааааа Аааааа Ааааа",
                    ]
                )
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d-%M-%Y"))
            )
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn("document_number", split(col("Паспорт"), ",")[0])
            .withColumn("document_date", split(col("Паспорт"), ",")[1])
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("document_number").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("document_number"),
                                    col("document_date"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("VIN").isNotNull() & (col("Номер автомобиля") != "")),
                    vehicle_udf(
                        lit(1),
                        col("Модель автомобиля"),
                        lit(None),
                        lit(None),
                        col("Номер автомобиля"),
                        col("VIN"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "vehicles",
            )
        )

        df_without_birth_date = (
            df.filter(col("birth_date").isNull())
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(col("vehicles").isNotNull(), array(col("vehicles"))).otherwise(
                    None
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "vehicles",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df_with_birth_date = (
            df.filter(col("birth_date").isNotNull())
            .groupBy(col("names"), col("birth_date"))
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("address"))).alias("address"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(collect_set(col("vehicles"))).alias("vehicles"),
                array_compact(flatten(collect_set(col("documents")))).alias(
                    "documents"
                ),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "vehicles",
            )
        )

        df = df_with_birth_date.unionAll(df_without_birth_date)

        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
