from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    array_compact,
    array_distinct,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0039"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0039/raw/ESIA_24_02_2021.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn(
                "names",
                name_parts_udf(
                    col("'firstname'"), col("'lastname'"), col("'middlename'")
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("'addressconstantregistration'")),
                            address_udf(col("'addresshome'")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("'phonemobile'")),
                            phone_udf(col("'phonework'")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("'email'")))
            .withColumn("sex", sex_udf(col("'gender'")))
            .withColumn(
                "birth_date", birth_date_udf(col("'birthday'"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "documents",
                when(
                    col("'snils'").isNotNull()
                    | col("'inn'").isNotNull()
                    | col("'documentnumber'").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("'documentnumber'").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat_ws(
                                        "",
                                        col("'documentseries'"),
                                        col("'documentnumber'"),
                                        col("'issuedate'"),
                                        lit(None),
                                        when(
                                            col("'issueauthority'") != "VERIFIED",
                                            col("'issueauthority'"),
                                        ).otherwise(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ),
                            ).otherwise(None),
                            when(
                                col("'inn'").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("'inn'"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("'snils'").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("'snils'"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("'esiaid'").isNotNull(),
                    array(
                        struct(
                            lit("Госуслуги").alias("title"),
                            lit("https://esia.gosuslugi.ru").alias("link"),
                            col("'esiaid'").alias("id"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("'createdts'"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("apd_application"),
                    df["'apd_application'"],
                    lit("esiaid"),
                    df["'esiaid'"],
                    lit("creatorclient"),
                    df["'creatorclient'"],
                ),
            )
        )

        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "accounts",
            "documents",
            "sex",
            "birth_date",
            "actuality",
            "raw_metadata",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
