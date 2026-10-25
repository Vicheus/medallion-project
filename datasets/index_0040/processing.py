from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    regexp_extract,
    size,
    array_compact,
)
from pyspark.sql.types import StructField, StructType, StringType

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
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0040"

    def parser(self):
        schema = StructType(
            [
                StructField("date", StringType(), nullable=True),
                StructField("last_name", StringType(), nullable=True),
                StructField("first_name", StringType(), nullable=True),
                StructField("middle_name", StringType(), nullable=True),
                StructField("gender", StringType(), nullable=True),
                StructField("birthday", StringType(), nullable=True),
                StructField("adress", StringType(), nullable=True),
                StructField("passport", StringType(), nullable=True),
                StructField("email", StringType(), nullable=True),
                StructField("phone", StringType(), nullable=True),
            ]
        )
        passport_pattern = (
            r"(\d{4}\s\d{6}),\sвыдан\s(\d{2}\.\d{2}\.\d{4})\s(.+?)\s(\d{6})$"
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0040/raw/Esia_Gosuslugi_2022_2,4kk.csv",
            sep=";",
            schema=schema,
            header=False,
        ).replace("NULL", None)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn(
                "passport_number_sequence",
                regexp_extract("passport", passport_pattern, 1),
            )
            .withColumn(
                "passport_date_issued", regexp_extract("passport", passport_pattern, 2)
            )
            .withColumn(
                "passport_authority_location",
                regexp_extract("passport", passport_pattern, 3),
            )
            .withColumn(
                "passport_authority_code",
                regexp_extract("passport", passport_pattern, 4),
            )
            .withColumn("address", address_udf(col("adress")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%m.%Y")))
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport_number_sequence"),
                                    col("passport_date_issued"),
                                    lit(None),
                                    col("passport_authority_location"),
                                    col("passport_authority_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
            )
        )
        df = df.select(
            "names", "emails", "phones", "address", "documents", "sex", "birth_date"
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
        )

        df.show(truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
