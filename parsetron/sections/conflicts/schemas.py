from pyspark.sql.types import StructType, IntegerType, StructField, StringType

conflict_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("country", StringType(), True),
        StructField("region", StringType(), True),
        StructField("type", IntegerType(), True),
        StructField("severity", IntegerType(), True),
        StructField("date_start", StringType(), True),
        StructField("date_end", StringType(), True),
    ]
)
