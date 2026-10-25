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
    collect_set,
    max,
    regexp_replace,
    lower,
    expr,
)
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    raw_metadata_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0489"
    validate_invalid_groupping: bool = True
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "emails,phones,address"

    def parser(self):
        schema1 = (
            StructType()
            .add("id", StringType(), True)
            .add("col1", StringType(), True)
            .add("col2", StringType(), True)
            .add("order_id", StringType(), True)
            .add("order_date", StringType(), True)
            .add("address1", StringType(), True)
            .add("house", StringType(), True)
            .add("flat", StringType(), True)
            .add("package_number", StringType(), True)
            .add("col4", StringType(), True)
            .add("item", StringType(), True)
            .add("name", StringType(), True)
            .add("email", StringType(), True)
            .add("payment_type", StringType(), True)
            .add("additional_service1", StringType(), True)
            .add("additional_service2", StringType(), True)
            .add("col5", StringType(), True)
            .add("city", StringType(), True)
            .add("region", StringType(), True)
            .add("index", StringType(), True)
            .add("phone", StringType(), True)
            .add("col6", StringType(), True)
            .add("col7", StringType(), True)
            .add("col8", StringType(), True)
            .add("col9", StringType(), True)
            .add("col10", StringType(), True)
            .add("col11", StringType(), True)
            .add("col12", StringType(), True)
            .add("col13", StringType(), True)
            .add("col14", StringType(), True)
            .add("col15", StringType(), True)
            .add("col16", StringType(), True)
            .add("amount", StringType(), True)
            .add("col18", StringType(), True)
            .add("col19", StringType(), True)
            .add("col20", StringType(), True)
            .add("col21", StringType(), True)
            .add("col22", StringType(), True)
            .add("col23", StringType(), True)
            .add("col24", StringType(), True)
            .add("col25", StringType(), True)
            .add("col26", StringType(), True)
            .add("col27", StringType(), True)
            .add("col28", StringType(), True)
            .add("col29", StringType(), True)
            .add("col30", StringType(), True)
            .add("col31", StringType(), True)
            .add("col32", StringType(), True)
        )
        schema2 = (
            StructType()
            .add("id", StringType(), True)
            .add("col1", StringType(), True)
            .add("col2", StringType(), True)
            .add("created_at", StringType(), True)
            .add("updated_at", StringType(), True)
            .add("col3", StringType(), True)
            .add("city", StringType(), True)
            .add("col4", StringType(), True)
            .add("col5", StringType(), True)
            .add("col6", StringType(), True)
            .add("first_name", StringType(), True)
            .add("last_name", StringType(), True)
            .add("middle_name", StringType(), True)
            .add("index", StringType(), True)
            .add("col7", StringType(), True)
            .add("region", StringType(), True)
            .add("col8", StringType(), True)
            .add("street", StringType(), True)
            .add("col9", StringType(), True)
            .add("phone", StringType(), True)
            .add("col10", StringType(), True)
            .add("col11", StringType(), True)
            .add("col12", StringType(), True)
            .add("col13", StringType(), True)
            .add("col14", StringType(), True)
            .add("col15", StringType(), True)
        )
        df1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0489/raw/ru_puma_com_1.csv",
            sep=",",
            header=False,
            schema=schema1,
        )

        print(f"DISTINCT PHONES DF1: {df1.select(col('phone')).distinct().count()}")
        df2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0489/raw/ru_puma_com_2.csv",
                sep=",",
                header=False,
                schema=schema2,
            )
            .withColumn("first_name", regexp_replace(col("first_name"), ".", ""))
            .withColumn("last_name", regexp_replace(col("last_name"), ".", ""))
            .withColumn("middle_name", regexp_replace(col("middle_name"), ".", ""))
        )
        print(f"DISTINCT PHONES DF2: {df2.select(col('phone')).distinct().count()}")

        df1 = (
            df1.withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("address", address_udf(col("address1")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("order_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("item"),
                    col("item"),
                    lit("payment_type"),
                    col("payment_type"),
                    lit("additional_service1"),
                    col("additional_service1"),
                    lit("additional_service2"),
                    col("additional_service2"),
                    lit("amount"),
                    col("amount"),
                    lit("package_number"),
                    col("package_number"),
                ),
            )
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df2 = (
            df2.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("emails", lit(None))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(concat_ws(" ", col("region"), col("city"), col("street"))),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("raw_metadata", lit(None))
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df = df1.unionAll(df2)

        print(f"DF before filtering count: {df.count()}")

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(array_distinct(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(collect_set(col("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df = df.withColumn(
            "names",
            when(
                lower(col("names")).contains(".com")
                | lower(col("names")).contains(".ru"),
                lit(None),
            ).otherwise(col("names")),
        )
        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .select("names", "emails", "phones", "address", "raw_metadata", "actuality")
        )

        df = df.filter(size(col("address")) < 10).withColumn(
            "raw_metadata", expr("slice(raw_metadata, 1, 20)")
        )

        print(f"DF before second filter count: {df.count()}")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        print(f"DF count: {df.count()}")

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
