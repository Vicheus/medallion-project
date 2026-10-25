from pyspark.sql.types import StringType, StructType, StructField

work_date_schema = StringType()
work_address_schema = StringType()
work_post_schema = StringType()
work_company_schema = StringType()
work_schema = StructType(
    [
        StructField("post", StringType(), True),
        StructField("date_start", StringType(), True),
        StructField("date_end", StringType(), True),
        StructField("company", StringType(), True),
        StructField("address", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
work_with_docs_schema = StructType(
    [
        StructField("post", StringType(), True),
        StructField("date_start", StringType(), True),
        StructField("date_end", StringType(), True),
        StructField("company", StringType(), True),
        StructField("address", StringType(), True),
        StructField("ru_inn", StringType(), True),
        StructField("ru_ogrn", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
