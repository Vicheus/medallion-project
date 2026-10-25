from pyspark.sql.types import StructType, StructField, StringType

ip_address_schema = StringType()
ip_address_date_schema = StringType()

ip_schema = StructType(
    [
        StructField("ip", StringType(), True),
        StructField("date", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
