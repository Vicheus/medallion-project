from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    greatest,
)
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0200"

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), nullable=True),
                StructField("email", StringType(), nullable=True),
                StructField("phone", StringType(), nullable=True),
                StructField("first_name", StringType(), nullable=True),
                StructField("last_name", StringType(), nullable=True),
                StructField("father_name", StringType(), nullable=True),
                StructField("password_hash", StringType(), nullable=True),
                StructField("auth_key", StringType(), nullable=True),
                StructField("password_reset_token", StringType(), nullable=True),
                StructField("role", StringType(), nullable=True),
                StructField("created_at", StringType(), nullable=True),
                StructField("rate_allowance_updated_at", StringType(), nullable=True),
                StructField("rate_allowance", IntegerType(), nullable=True),
                StructField("photo", StringType(), nullable=True),
                StructField("birthday", StringType(), nullable=True),
                StructField("gender", StringType(), nullable=True),
                StructField("phone_org", IntegerType(), nullable=True),
                StructField("phone_org_dop", StringType(), nullable=True),
                StructField("phone_mob", StringType(), nullable=True),
                StructField("region_id", IntegerType(), nullable=True),
            ]
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0200/raw/premiya_preprocessed.csv",
            sep="\t",
            schema=schema,
            header=False,
        ).replace("\\N", None)

        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("father_name")),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("phone")),
                            phone_udf(col("phone_org")),
                            phone_udf(col("phone_mob")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created_at"), col("rate_allowance_updated_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "phones", "emails", "sex", "birth_date", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()

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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .select("names", "phones", "emails", "sex", "birth_date", "actuality")
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.drop_duplicates()

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
