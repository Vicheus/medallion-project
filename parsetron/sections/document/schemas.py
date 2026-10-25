from pyspark.sql.types import (
    StructType,
    IntegerType,
    StructField,
    StringType,
    ArrayType,
)

document_schema = StructType(
    [
        StructField("type", IntegerType(), True),
        StructField("serial", StringType(), False),
        StructField("country", StringType(), True),
        StructField("date_issue", StringType(), True),
        StructField("date_expire", StringType(), True),
        StructField("authority", StringType(), True),
        StructField("authority_code", StringType(), True),
    ]
)
identify_documents_features_schema = ArrayType(
    StructType(
        [
            StructField("document_series", StringType(), True),
            StructField("document_issued_at", StringType(), True),
            StructField("document_issued_by", StringType(), True),
            StructField("document_issued_by_code", StringType(), True),
        ]
    )
)
identify_document_features_schema = StructType(
    [
        StructField("document_series", StringType(), True),
        StructField("document_issued_at", StringType(), True),
        StructField("document_issued_by", StringType(), True),
        StructField("document_issued_by_code", StringType(), True),
    ]
)
