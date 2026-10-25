from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    size,
    split,
    regexp_replace,
    array_compact,
    try_element_at,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phones_udf,
    emails_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails,documents,addresses"
    dataset_code_name: str = "index_0471"

    def parser(self):
        df = (
            self.read(
                path="/media/worker/SAMSUNG/Databases/index_0471/raw/rosstrah_all.csv",
                sep="\t",
                header=True,
            )
            .withColumn(
                "names",
                array_distinct(
                    array(
                        name_udf(col("name")),
                        name_parts_udf(
                            col("first_name"), col("last_name"), col("patronymic")
                        ),
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%m.%Y")))
            .withColumn("birth_place", address_udf(col("birthplaces")))
            .withColumn("phones", phones_udf(split(col("phones"), ";")))
            .withColumn("emails", emails_udf(split(col("emails"), ";")))
            # Паспорта
            .withColumn("passport_array", split(col("passport_numbers"), r"\s*;\s*"))
            .withColumn("inns_array", split(col("inns"), r"\s*;\s*"))
            .withColumn(
                "passport_1",
                when(
                    try_element_at(col("passport_array"), lit(1)).isNotNull()
                    & (try_element_at(col("passport_array"), lit(1)) != ""),
                    document_udf(
                        lit("паспорт гражданина рф"),
                        try_element_at(col("passport_array"), lit(1)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "passport_2",
                when(
                    try_element_at(col("passport_array"), lit(2)).isNotNull()
                    & (try_element_at(col("passport_array"), lit(2)) != ""),
                    document_udf(
                        lit("паспорт гражданина рф"),
                        try_element_at(col("passport_array"), lit(2)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "passport_3",
                when(
                    try_element_at(col("passport_array"), lit(3)).isNotNull()
                    & (try_element_at(col("passport_array"), lit(3)) != ""),
                    document_udf(
                        lit("паспорт гражданина рф"),
                        try_element_at(col("passport_array"), lit(3)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            # ИНН
            .withColumn(
                "inn_1",
                when(
                    try_element_at(col("inns_array"), lit(1)).isNotNull()
                    & (try_element_at(col("inns_array"), lit(1)) != ""),
                    document_udf(
                        lit("инн"),
                        try_element_at(col("inns_array"), lit(1)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "inn_2",
                when(
                    try_element_at(col("inns_array"), lit(2)).isNotNull()
                    & (try_element_at(col("inns_array"), lit(2)) != ""),
                    document_udf(
                        lit("инн"),
                        try_element_at(col("inns_array"), lit(2)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "inn_3",
                when(
                    try_element_at(col("inns_array"), lit(3)).isNotNull()
                    & (try_element_at(col("inns_array"), lit(3)) != ""),
                    document_udf(
                        lit("инн"),
                        try_element_at(col("inns_array"), lit(3)),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            # Адреса - аналогично документам
            .withColumn("addresses_array", split(col("addresses"), r"\s*;\s*"))
            .withColumn(
                "address_1",
                when(
                    try_element_at(col("addresses_array"), lit(1)).isNotNull()
                    & (try_element_at(col("addresses_array"), lit(1)) != ""),
                    address_udf(
                        regexp_replace(
                            try_element_at(col("addresses_array"), lit(1)),
                            r"^(fact:|delivery:|reg:)",
                            "",
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "address_2",
                when(
                    try_element_at(col("addresses_array"), lit(2)).isNotNull()
                    & (try_element_at(col("addresses_array"), lit(2)) != ""),
                    address_udf(
                        regexp_replace(
                            try_element_at(col("addresses_array"), lit(2)),
                            r"^(fact:|delivery:|reg:)",
                            "",
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "address_3",
                when(
                    try_element_at(col("addresses_array"), lit(3)).isNotNull()
                    & (try_element_at(col("addresses_array"), lit(3)) != ""),
                    address_udf(
                        regexp_replace(
                            try_element_at(col("addresses_array"), lit(3)),
                            r"^(fact:|delivery:|reg:)",
                            "",
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("insurer_inns"),
                    col("insurer_inns"),
                    lit("insurer_names"),
                    col("insurer_names"),
                    lit("employers"),
                    col("employers"),
                    lit("occupations"),
                    col("occupations"),
                    lit("bank_accounts"),
                    col("bank_accounts"),
                    lit("date_from"),
                    col("date_from"),
                    lit("date_to"),
                    col("date_to"),
                    lit("tags"),
                    col("tags"),
                    lit("sources"),
                    col("sources"),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date_to"), lit("%d.%m.%Y"))
            )
            # Собираем документы
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("snils").isNotNull(),
                            document_udf(
                                lit("снилс"),
                                col("snils"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        ).otherwise(None),
                        col("passport_1"),
                        col("passport_2"),
                        col("passport_3"),
                        col("inn_1"),
                        col("inn_2"),
                        col("inn_3"),
                    )
                ),
            )
            # Собираем адреса
            .withColumn(
                "addresses",
                array_compact(
                    array(col("address_1"), col("address_2"), col("address_3"))
                ),
            )
        )

        df = df.select(
            "names",
            "birth_date",
            "birth_place",
            "addresses",
            "phones",
            "emails",
            "documents",
            "raw_metadata",
            "actuality",
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "addresses",
                when(size(col("addresses")) > 0, col("addresses")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .filter(
                col("names").isNotNull()
                & (
                    col("documents").isNotNull()
                    | col("emails").isNotNull()
                    | col("phones").isNotNull()
                    | col("addresses").isNotNull()
                )
            )
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
