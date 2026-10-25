from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    concat,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    address_from_parts_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0001"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0001/raw/zoloto585.ru.csv",
            sep=", ",
            encoding="windows-1251",
            header=True,
        )

        df = df.dropDuplicates(["PartnerNumber", "PhoneNumber", "FIO"])
        df = (
            df.withColumn("names", name_udf(col("FIO")))
            .withColumn("sex", sex_udf(col("SEX")))
            .withColumn("birth_date", birth_date_udf(col("BirthDate"), lit("%Y-%m-%d")))
            .withColumn('address', address_udf(concat_ws(' ', col("PostalCode"), col("City"), col("Street"), col("HouseNumber"), col("RoomNumber"))))
            .withColumn('addresses', address_from_parts_udf(
                lit(1),
                col("PostalCode"),
                lit(None),
                lit(None),
                col("City"),
                col("Street"),
                col("HouseNumber"),
                lit(None),
                col("RoomNumber"),
                lit(None),
                col("Building"),
            ))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("PhoneNumber")))
            .withColumn(
                "documents",
                when(
                    col("PassportNumber").isNotNull(),
                    document_udf(
                        col("PassportType"),
                        col("PassportNumber"),
                        col("PassportValidFromDate"),
                        col("PassportValidToDate"),
                        col("PassportText"),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("DateOperation"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("LombardRating"),
                    df["LombardRating"],
                    lit("LombardFirstDealDate"),
                    df["LombardFirstDealDate"],
                    lit("LombardLastDealDate"),
                    df["LombardLastDealDate"],
                    lit("LastVidachaZaimDate"),
                    df["LastVidachaZaimDate"],
                    lit("LombardBalanceScore"),
                    df["LombardBalanceScore"],
                ),
            )
        )

        df = df.select(
            "names",
            "sex",
            "birth_date",
            "address",
            "emails",
            "phones",
            "documents",
            "actuality",
            "raw_metadata",
        )

        df.cache()

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(col("documents").isNotNull(), array(col("documents"))).otherwise(
                    None
                ),
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
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=10, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
