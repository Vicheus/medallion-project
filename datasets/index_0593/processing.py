from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    size,
    regexp_extract,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0593"
    calc_completeness: bool = True

    def parser(self):
        df_1 = (
            self.read(
                path="/home/user/Documents/data/index_0593/raw/днком/150к.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(
                    col("first_name"), col("last_name"), col("patronymic_name")
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", when(col("sex") == "true", "m").otherwise("f"))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("document_number").isNotNull(),
                            document_udf(
                                lit(None),
                                col("document_number"),
                                col("document_issue_date"),
                                lit(None),
                                col("document_issuerer"),
                                lit(None),
                                lit("%Y-%m-%d"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%dT%H:%M:%S.%f")),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "documents",
                "actuality",
            )
        )

        df_2 = (
            self.read(
                path="/home/user/Documents/data/index_0593/raw/днком/150к (2).csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%d.%m.%Y")))
            .withColumn("sex", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("passport").isNotNull(),
                            document_udf(
                                lit(None),
                                col("passport"),
                                lit(None),
                                lit(None),
                                col("passport_issuerer"),
                                lit(None),
                                lit("%Y-%m-%d"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn("actuality", actuality_date_udf(col("data"), lit("%Y-%m-%d")))
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "documents",
                "actuality",
            )
        )

        df_3 = (
            self.read(
                path="/home/user/Documents/data/index_0593/raw/днком/База пациентов_из_xls.csv",
                sep="|",
                header=True,
            )
            .withColumn("names", name_udf(col("fio")))
            .withColumn("phones", phone_udf(col("tel")))
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%d.%m.%Y")))
            .withColumn("sex", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("address", lit(None))
            .withColumn("documents", array())
            .withColumn(
                "actuality",
                actuality_date_udf(
                    regexp_extract(
                        col("comment"),
                        r"Дата первого визита:\s*(\d{2}\.\d{2}\.\d{4})",
                        1,
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "emails",
                "phones",
                "address",
                "documents",
                "actuality",
            )
        )

        df = df_1.unionAll(df_2).unionAll(df_3)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
