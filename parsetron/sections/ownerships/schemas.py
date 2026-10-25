from pyspark.sql.types import StructType, IntegerType, StructField, StringType

ownership_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("type", IntegerType(), True),
        StructField("date", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
