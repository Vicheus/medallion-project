from pyspark.sql.types import StructType, IntegerType, StructField, StringType

award_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("type", IntegerType(), True),
        StructField("date", StringType(), True),
        StructField("country", StringType(), True),
        StructField("authority", IntegerType(), True),
        StructField("serial", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
