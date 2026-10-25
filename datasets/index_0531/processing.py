from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    relations_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    raw_metadata_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
)
from parsetron.sections.document.udfs import document_udf

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
    regexp_replace,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0531"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0531/raw/grantains.ru/users.csv",
            sep=";",
            header=True,
        ).replace("<blank>", None)
        df = (
            df.withColumn(
                "names",
                name_parts_udf(
                    col("insurer_name"),
                    col("insurer_surname"),
                    col("insurer_middle_name"),
                ),
            )
            .withColumn(
                "insured_name",
                name_parts_udf(
                    col("insured_name"),
                    col("insured_surname"),
                    col("insured_middle_name"),
                ),
            )
            .withColumn(
                "beneficiary_name",
                name_parts_udf(
                    col("beneficiary_name"),
                    col("beneficiary_surname"),
                    col("beneficiary_middle_name"),
                ),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("insured_birthday"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", sex_udf(col("insured_sex")))
            .withColumn("phones", phone_udf(col("phone_number")))
            .withColumn("emails", email_udf(col("insurer_email")))
            .withColumn(
                "address_with_type",
                address_with_type_udf(col("insurer_address_full"), lit(1)),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(array(address_udf(col("insurer_address_full"))))
                ),
            )
            .withColumn(
                "addresses",
                normalize_address_batch_udf(array(col("address_with_type"))),
            )
            .withColumn(
                "relations",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("insured_name").isNotNull(),
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        col("insured_name"),
                                        birth_date_udf(
                                            col("insured_birthday"), lit("%d.%m.%Y")
                                        ),
                                        lit(""),
                                    )
                                ),
                            ).otherwise(None),
                            when(
                                col("beneficiary_name").isNotNull(),
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        col("beneficiary_name"),
                                        birth_date_udf(
                                            col("beneficiary_birthday"), lit("%d.%m.%Y")
                                        ),
                                        lit(""),
                                    )
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("insurer_passport_series").isNotNull()
                    & col("insurer_passport_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("insurer_passport_series").isNotNull()
                                & col("insurer_passport_number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat_ws(
                                        "",
                                        col("insurer_passport_series"),
                                        col("insurer_passport_number"),
                                    ),
                                    col("insurer_passport_issue"),
                                    lit(None),
                                    col("insurer_passport_given_by"),
                                    regexp_replace(
                                        col("insurer_passport_division"), "[^0-9]", ""
                                    ),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("date_start"),
                    col("date_start"),
                    lit("date_end"),
                    col("date_end"),
                    lit("risk_name"),
                    col("risk_name"),
                    lit("risk_sum"),
                    col("risk_sum"),
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date_start"), lit("%d.%m.%Y"))
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "relations",
                "emails",
                "phones",
                "address",
                "addresses",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df = df.drop_duplicates(["names", "birth_date"])
        df = df.cache()

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "address",
                when(
                    size(array_compact(array_distinct(col("address")))) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(
                    size(array_compact(array_distinct(col("addresses")))) > 0,
                    array_compact(array_distinct(col("addresses"))),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    size(array_compact(array_distinct(col("relations")))) > 0,
                    array_compact(array_distinct(col("relations"))),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(array_distinct(col("documents")))) > 0,
                    array_compact(array_distinct(col("documents"))),
                ).otherwise(None),
            )
            .withColumn(
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
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
