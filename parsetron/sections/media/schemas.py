from pyspark.sql.types import (
    StringType,
    IntegerType,
    StructField,
    StructType,
)

media_schema = StructType(
    [
        StructField("ds_internal_id", StringType(), False),
        StructField("file_name", StringType(), False),
        StructField("raw_file_name", StringType(), False),
        StructField("file_type", IntegerType(), False),
        StructField("url", StringType(), False),
        StructField("description", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
