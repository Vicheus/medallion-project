from pyspark.sql.types import StructType, StructField, StringType

link_schema = StructType(
    [
        StructField("title", StringType(), False),
        StructField("link", StringType(), False),
        StructField("comment", StringType(), True),
    ]
)
