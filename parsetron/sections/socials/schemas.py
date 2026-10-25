from pyspark.sql.types import StructType, StructField, StringType

social_schema = StructType(
    [
        StructField("title", StringType(), False),
        StructField("id", StringType(), True),
        StructField("link", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
