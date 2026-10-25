from pyspark.sql.types import StringType, StructType, StructField, IntegerType

education_date_schema = StringType()
education_level_schema = IntegerType()
education_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("level", IntegerType(), True),
        StructField("country", StringType(), True),
        StructField("date_start", StringType(), True),
        StructField("date_end", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
