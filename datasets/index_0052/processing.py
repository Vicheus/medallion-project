from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    greatest,
)
from pyspark.sql.types import StructType, StructField, StringType

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
    dataset_code_name: str = "index_0052"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "address,emails,phones,documents"

    def parser(self):

        schema = StructType(
            [
                StructField("Last Name", StringType(), True),
                StructField("First Name", StringType(), True),
                StructField("Patronymic", StringType(), True),
                StructField("Type", StringType(), True),
                StructField("Identifier", StringType(), True),
                StructField("SNILS", StringType(), True),
                StructField("Gender", StringType(), True),
                StructField("Date of Birth", StringType(), True),
                StructField("Date of Death", StringType(), True),
                StructField("Note", StringType(), True),
                StructField("Insurance Organization", StringType(), True),
                StructField("Insurance Organization OGRN", StringType(), True),
                StructField("Internal Insurance Organization", StringType(), True),
                StructField("Organization Location", StringType(), True),
                StructField("Organization Location Index", StringType(), True),
                StructField("Insurance Policy Type", StringType(), True),
                StructField("Insurance Policy Number", StringType(), True),
                StructField("Email", StringType(), True),
                StructField("Home Phone", StringType(), True),
                StructField("Mobile Phone", StringType(), True),
                StructField("Notify By", StringType(), True),
                StructField("Temporary Registration Address", StringType(), True),
                StructField("Actual Residence Address", StringType(), True),
                StructField("Permanent Registration Address", StringType(), True),
                StructField("Insurance Policy Issue Date", StringType(), True),
                StructField("Insurance Policy Expiry Date", StringType(), True),
                StructField("Phone Update Date", StringType(), True),
                StructField("Address Update Date", StringType(), True),
                StructField("Update Date", StringType(), True),
            ]
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0052/raw/emias.csv",
            sep=";",
            header=True,
            schema=schema,
        )

        df = (
            df.withColumn("id", col("Identifier"))
            .withColumn(
                "names",
                name_parts_udf(col("First Name"), col("Last Name"), col("Patronymic")),
            )
            .withColumn("sex", sex_udf(col("Gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("Date of Birth"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            address_udf(col("Permanent Registration Address")),
                            address_udf(col("Temporary Registration Address")),
                            address_udf(col("Actual Residence Address")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("Home Phone")), phone_udf(col("Mobile Phone"))
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("SNILS").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("SNILS").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("SNILS"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                            when(
                                col("Insurance Policy Number").isNotNull(),
                                document_udf(
                                    lit("номер страхового полиса"),
                                    col("Insurance Policy Number"),
                                    col("Insurance Policy Issue Date"),
                                    col("Insurance Policy Expiry Date"),
                                    col("Insurance Organization"),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("Phone Update Date"),
                        col("Address Update Date"),
                        col("Update Date"),
                    ),
                    lit("%Y-%m-%d"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Date of Death"),
                    df["Date of Death"],
                    lit("Note"),
                    df["Note"],
                    lit("Insurance Organization OGRN"),
                    df["Insurance Organization OGRN"],
                    lit("Internal Insurance Organization"),
                    df["Internal Insurance Organization"],
                    lit("Organization Location"),
                    df["Organization Location"],
                    lit("Organization Location Index"),
                    df["Organization Location Index"],
                    lit("Insurance Policy Type"),
                    df["Insurance Policy Type"],
                ),
            )
        )

        df = df.select(
            "names",
            "address",
            "emails",
            "phones",
            "documents",
            "sex",
            "birth_date",
            "actuality",
            "raw_metadata",
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
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
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
