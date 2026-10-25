from pyspark.sql.types import StructType, StructField, StringType

device_date_schema = StringType()

device_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("user_agent", StringType(), True),
        StructField("date", StringType(), True),
        StructField("action", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
