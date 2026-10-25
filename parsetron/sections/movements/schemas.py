from pyspark.sql.types import StructType, IntegerType, StructField, StringType

movement_schema = StructType(
    [
        StructField(
            "from",
            StructType(
                [
                    StructField("datetime", StringType(), True),
                    StructField("country", StringType(), True),
                    StructField("city", StringType(), True),
                    StructField("code", StringType(), True),
                ]
            ),
            True,
        ),
        StructField(
            "to",
            StructType(
                [
                    StructField("datetime", StringType(), True),
                    StructField("country", StringType(), True),
                    StructField("city", StringType(), True),
                    StructField("code", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("code_type", StringType(), True),
        StructField("ticket_order_datetime", StringType(), True),
        StructField("seat", StringType(), True),
        StructField("ticket_number", StringType(), True),
        StructField("trip_number", StringType(), True),
        StructField("class", StringType(), True),
        StructField("type", IntegerType(), True),
        StructField("comment", StringType(), True),
        StructField("ticket_issuer", StringType(), True),
        StructField("transport_company_name", StringType(), True),
        StructField("transport_company_code", StringType(), True),
    ]
)
movement_time_schema = StringType()
movement_date_schema = StringType()
movement_datetime_schema = StringType()
ticket_order_datetime_schema = StringType()
movement_code_schema = StringType()
