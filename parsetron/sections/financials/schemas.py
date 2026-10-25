from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    ArrayType,
)

brute_force_card_schema = StructType(
    [
        StructField("card_number_masked", StringType(), True),
        StructField("card_hash", StringType(), False),
        StructField("hash_type", StringType(), True),
        StructField("numbers_to_brute_force", IntegerType(), True),
        StructField("symbol_to_replace", StringType(), True),
    ]
)
card_schema = StringType()
cards_schema = ArrayType(StringType())
yandex_money_number_schema = StringType()
date_issue_schema = StringType()
date_expire_schema = StringType()
invoice_number_schema = StringType()

financials_schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("card_number", StringType(), True),
        StructField("invoice_number", StringType(), True),
        StructField("date_issue", StringType(), True),
        StructField("date_expire", StringType(), True),
        StructField("comment", StringType(), True),
    ]
)
