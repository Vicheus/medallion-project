from pyspark.sql.types import StructType, StructField, StringType, IntegerType

vehicle_schema = StructType(
    [
        StructField("type", IntegerType(), False),
        StructField("model", StringType(), True),
        StructField("year", IntegerType(), True),
        StructField("color", StringType(), True),
        StructField("number", StringType(), True),
        StructField("vin", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
