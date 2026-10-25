from pyspark.sql.types import StructType, IntegerType, StructField, StringType

force_schema = StructType(
    [
        StructField("tag_number", StringType(), True),
        StructField("unit_code", StringType(), True),
        StructField("unit_name", StringType(), True),
        StructField("callsign", StringType(), True),
        StructField("rank", StringType(), True),
        StructField("position", StringType(), True),
        StructField("mos_code", StringType(), True),
        StructField("category", IntegerType(), True),
        StructField("date_start", StringType(), True),
        StructField("date_end", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
