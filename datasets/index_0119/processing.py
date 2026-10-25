from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, lit, greatest, regexp_replace
from pyspark.sql.types import StructType, StringType

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
    dataset_code_name: str = "index_0119"
    calc_completeness: bool = False
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails"

    def parser(self):
        schema = (
            StructType()
            .add("id", StringType(), True)
            .add("owner_id", StringType(), True)
            .add("name", StringType(), True)
            .add("surname", StringType(), True)
            .add("second_name", StringType(), True)
            .add("birthday", StringType(), True)
            .add("gender", StringType(), True)
            .add("phone", StringType(), True)
            .add("email", StringType(), True)
            .add("region_external_id", StringType(), True)
            .add("city_external_id", StringType(), True)
            .add("source", StringType(), True)
            .add("created_at", StringType(), True)
            .add("updated_at", StringType(), True)
            .add("push_active", StringType(), True)
        )
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0119/raw/aptekiPlus.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df.show(n=1000, truncate=False)

        df = (
            df.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("name"), col("surname"), col("second_name"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%M-%d")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "updated_at", regexp_replace(col("updated_at"), "\+03", "+0300")
            )
            .withColumn(
                "created_at", regexp_replace(col("created_at"), "\+03", "+0300")
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("created_at"), col("updated_at")),
                    lit("%Y-%m-%d %H:%M:%S%z"),
                ),
            )
            .select("names", "emails", "phones", "sex", "birth_date", "actuality")
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
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.select("names", "emails", "phones", "sex", "birth_date", "actuality")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
