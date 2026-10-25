from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phones_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0491"
    validate_invalid_groupping: bool = True

    def parser(self):
        df1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/01_48263.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ВЛАДЕЛЕЦ")))
            .withColumn("birth_date", birth_date_udf(col("ownerbd"), lit("%d.%m.%Y")))
            .withColumn("phones", array_compact(array(phone_udf(col("ТЕЛЕФОН")))))
            .withColumn("address", address_udf(col("АДРЕС")))
            .withColumn(
                "vehicles",
                when(
                    (
                        col("ВИН").isNotNull()
                        | col("ГРЗ").isNotNull()
                        | col("МАРКА").isNotNull()
                        | col("МОДЕЛЬ").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        concat_ws(" ", col("МАРКА"), col("МОДЕЛЬ")),
                        col("ГОД").cast("int"),
                        lit(None),
                        col("ГРЗ"),
                        col("ВИН"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn("documents", array())
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("Л/С"), col("Л/С")),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/02_30000.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("ФИО")))
            .withColumn("birth_date", birth_date_udf(col("Дата Рожд"), lit("%d.%m.%Y")))
            .withColumn("phones", array_compact(array(phone_udf(col("Телефон")))))
            .withColumn("address", lit(None))
            .withColumn(
                "vehicles",
                when(
                    (
                        col("Вин").isNotNull()
                        | col("ГосНомер").isNotNull()
                        | col("Марка").isNotNull()
                        | col("Модель").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        concat_ws(" ", col("Марка"), col("Модель")),
                        lit(None),
                        lit(None),
                        col("ГосНомер"),
                        col("Вин"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("ЛС"), col("ЛС")),
            )
            .withColumn("documents", array())
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/03_35339.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Владелец")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("phones", array_compact(array(phone_udf(col("Телефон")))))
            .withColumn("address", address_udf(col("Адрес")))
            .withColumn(
                "vehicles",
                when(
                    (col("VIN").isNotNull() | col("НоMер авто").isNotNull()),
                    vehicle_udf(
                        lit(1),
                        lit(None),
                        lit(None),
                        lit(None),
                        col("НоMер авто"),
                        col("VIN"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Паспорт").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Паспорт"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df4 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/04_7461.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата Рождения"), lit("%d/%m/%Y"))
            )
            .withColumn("phones", array_compact(array(phone_udf(col("телефон")))))
            .withColumn("address", lit(None))
            .withColumn(
                "vehicles",
                when(
                    (
                        col("VIN").isNotNull()
                        | col("ГосНомер").isNotNull()
                        | col("Марка_Модель").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        col("Марка_Модель"),
                        lit(None),
                        lit(None),
                        col("ГосНомер"),
                        col("VIN"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", lit(None))
            .withColumn("documents", array())
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df5 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/07_14719.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("birth_date", birth_date_udf(col("дата рожд"), lit("%d/%m/%Y")))
            .withColumn("phones", array_compact(array(phone_udf(col("тел")))))
            .withColumn("address", lit(None))
            .withColumn(
                "vehicles",
                when(
                    (
                        col("vin").isNotNull()
                        | col("Гос номер").isNotNull()
                        | col("МаркаМодель").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        col("МаркаМодель"),
                        lit(None),
                        lit(None),
                        col("Гос номер"),
                        col("vin"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("лс"), col("лс")),
            )
            .withColumn("documents", array())
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df6 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0491/raw/osago_20/08_56324.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn("birth_date", birth_date_udf(col("Дата Рожд"), lit("%d/%m/%Y")))
            .withColumn(
                "phones", phones_udf(array(col("тел 1"), col("тел 2"), col("тел 3")))
            )
            .withColumn("address", lit(None))
            .withColumn(
                "vehicles",
                when(
                    (
                        col("full-model").isNotNull()
                        | col("gosnom").isNotNull()
                        | col("vin").isNotNull()
                    ),
                    vehicle_udf(
                        lit(1),
                        col("full-model"),
                        lit(None),
                        lit(None),
                        col("gosnom"),
                        col("vin"),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(lit("insurant"), col("insurant")),
            )
            .withColumn("documents", array())
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df = df1.unionAll(df2).unionAll(df3).unionAll(df4).unionAll(df5).unionAll(df6)

        df_with_b_date = df.filter(
            (col("names").isNotNull()) & (col("birth_date").isNotNull())
        )
        df_without_b_date = (
            df.filter((col("birth_date").isNull()))
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("vehicles", array_compact(array(col("vehicles"))))
            .withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df_with_b_date = (
            df_with_b_date.filter(
                (col("names").isNotNull()) & (col("birth_date").isNotNull())
            )
            .groupBy(["names", "birth_date"])
            .agg(
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("vehicles")))).alias(
                    "vehicles"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
            )
            .select(
                "names",
                "birth_date",
                "address",
                "phones",
                "vehicles",
                "documents",
                "raw_metadata",
            )
        )

        df = df_with_b_date.unionAll(df_without_b_date)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
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
                | col("vehicles").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
