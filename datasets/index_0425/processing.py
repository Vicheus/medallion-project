from pyspark import StorageLevel
from parsetron.settings import DATASET_COUNTRY_CODE

from pyspark.sql.functions import (
    when,
    col,
    size,
    array,
    lit,
    array_compact,
    array_distinct,
    flatten,
    concat_ws,
    max,
    collect_set,
)
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    email_udf,
    address_udf,
    phone_udf,
    actuality_date_udf,
    birth_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0425"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df_companies_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/companies_1.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("birth_date", lit(None))
            .withColumn("address", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("emails", lit(None))
            .withColumn(
                "documents",
                when(
                    col("iin").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("iin").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("iin"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", lit(None))
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/companies_2.csv",
                sep=",",
            )
            .withColumn("names", name_udf(col("Наименование предприятия")))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("Регион"), col("Город/Район"))),
            )
            .withColumn("phones", lit(None))
            .withColumn("emails", lit(None))
            .withColumn(
                "documents",
                when(
                    col("БИН/ИИН").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("БИН/ИИН").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("БИН/ИИН"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Списочная численность работников чел (ЛК на ЭБТ)"),
                    col("Списочная численность работников чел (ЛК на ЭБТ)"),
                    lit("Финансовый год"),
                    col("Финансовый год"),
                    lit("Профессия"),
                    col("Профессия"),
                    lit("Мера"),
                    col("Мера"),
                    lit("Количество рабочих мест ед"),
                    col("Количество рабочих мест ед"),
                    lit("Количество трудоустроенных"),
                    col("Количество трудоустроенных"),
                    lit("Общая сумма договора тг"),
                    col("Общая сумма договора тг"),
                    lit("Общая сумма договора тг"),
                    col("Общая сумма договора тг"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    col("Дата подписания работодателем (отказа)"),
                    lit("%d.%m.%Y H:%M:%S"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/companies_3.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("namepol")))
            .withColumn("birth_date", lit(None))
            .withColumn("address", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("emails", lit(None))
            .withColumn(
                "documents",
                when(
                    col("iin").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("iin").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("iin"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("date_beg"), col("date_beg"), lit("date_end"), col("date_end")
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies_4 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/companies_4.csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("namepol")))
            .withColumn("birth_date", lit(None))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "phones", phone_udf(col("phonek"), lit(self.dataset_country_code.value))
            )
            .withColumn("emails", email_udf(col("emailk")))
            .withColumn(
                "documents",
                when(
                    col("rnn").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("rnn").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("rnn"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("god_beg"), col("god_beg"))
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_companies = (
            df_companies_1.unionAll(df_companies_2)
            .unionAll(df_companies_3)
            .unionAll(df_companies_4)
        )

        df_companies = (
            df_companies.groupBy(["names"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max("actuality").alias("actuality"),
                max("birth_date").alias("birth_date"),
            )
            .withColumn("works", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df_persons_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/persons_1.csv",
                sep=";",
            )
            .withColumn(
                "names", name_parts_udf(col("namek"), col("familyk"), col("otchk"))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("phonek"), lit(self.dataset_country_code.value)
                            )
                        )
                    )
                ),
            )
            .withColumn("emails", lit(None))
            .withColumn("documents", array())
            .withColumn("raw_metadata", lit(None))
            .withColumn(
                "works",
                when(
                    col("namekr").isNotNull() & (col("namekr") != ""),
                    work_udf(
                        lit(None),
                        lit(None),
                        lit(None),
                        col("namekr").alias("company"),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df_persons_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/persons_2.csv",
                sep=";",
            )
            .withColumn("names", name_parts_udf(col("IM"), col("FAM"), col("IM")))
            .withColumn(
                "birth_date", birth_date_udf(col("DATERG"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("address", address_udf(col("ADDRESS")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("TEL"), lit(self.dataset_country_code.value)),
                            phone_udf(
                                col("MOBIL"), lit(self.dataset_country_code.value)
                            ),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "documents",
                when(
                    col("IIN").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("IIN").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("IIN"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("HABITSOFW"), col("HABITSOFW"), lit("DOCUMENT"), col("DOCUMENT")
                ),
            )
            .withColumn("works", lit(None))
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df_persons_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0425/raw/preprocessed/persons_3.csv",
                sep=";",
            )
            .withColumn("names", name_parts_udf(col("im"), col("fam"), col("ot")))
            .withColumn(
                "birth_date", birth_date_udf(col("daterg"), lit("%Y-%m-%d %H:%M:%S"))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn("phones", array())
            .withColumn("emails", lit(None))
            .withColumn(
                "documents",
                when(
                    col("IIN").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("IIN").isNotNull(),
                                    document_udf(
                                        lit("инн"),
                                        col("IIN"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                        lit(self.dataset_country_code.value),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("raw_metadata", raw_metadata_udf(lit("daterg"), col("daterg")))
            .withColumn("works", lit(None))
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df_persons = df_persons_1.unionAll(df_persons_2).unionAll(df_persons_3)

        df_persons = (
            df_persons.groupBy(["names"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(array_distinct(collect_set(col("works")))).alias("works"),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max("actuality").alias("actuality"),
                max("birth_date").alias("birth_date"),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_persons.unionAll(df_companies)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )
        df = df.select(
            "names",
            "birth_date",
            "emails",
            "phones",
            "address",
            "documents",
            "works",
            "raw_metadata",
            "actuality",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("phones").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
