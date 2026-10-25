from pyspark.sql.types import StructType, ArrayType, StructField, StringType

incidence_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("date", StringType(), True),
        StructField("insurance", StringType(), True),
        StructField("participants", ArrayType(StringType()), True),
        StructField("comment", StringType(), True),
    ]
)
incidence_date_schema = StringType()
