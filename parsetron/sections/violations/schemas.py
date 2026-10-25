from pyspark.sql.types import StructType, StructField, StringType

violation_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("date", StringType(), True),
        StructField("serial", StringType(), True),
        StructField("penalty_fare", StringType(), True),
        StructField("insurance", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
