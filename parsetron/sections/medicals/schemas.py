from pyspark.sql.types import StructType, IntegerType, StructField, StringType

medicals_schema = StructType(
    [
        StructField("diagnosis", StringType(), True),
        StructField("date_injury", StringType(), True),
        StructField("place_injury", StringType(), True),
        StructField("date_hospital", StringType(), True),
        StructField("severity", IntegerType(), True),
        StructField("medical_org", StringType(), True),
        StructField("evacuation_route", StringType(), True),
        StructField("date_evacuation", StringType(), True),
        StructField("primary_documents", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
