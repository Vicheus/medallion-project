from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    BooleanType,
    ArrayType,
    DoubleType,
    DateType,
)

name_schema = StringType()
names_schema = ArrayType(StringType())
sex_schema = IntegerType()
address_schema = StringType()
addresses_schema = ArrayType(StringType())
extract_address_schema = StringType()
birth_date_schema = StringType()
death_date_schema = StringType()
multiple_date_formats_schema = StringType()
email_schema = StringType()
emails_schema = ArrayType(StringType())
phone_schema = StringType()
phones_schema = ArrayType(StringType())
children_schema = BooleanType()
validate_name_is_person_or_organisation_schema = ArrayType(StringType())
relations_schema = StringType()
address_with_type_schema = StructType(
    [
        StructField("address", StringType(), True),
        StructField("address_type", IntegerType(), False),
    ]
)
addresses_with_type_schema = ArrayType(address_with_type_schema)
normalized_address_schema = StructType(
    [
        StructField("type", IntegerType(), True),
        StructField("raw", StringType(), False),
        StructField("address", StringType(), True),
        StructField(
            "location",
            StructType(
                [
                    StructField("region_type", StringType(), True),
                    StructField("region_value", StringType(), True),
                    StructField("settlement_region_type", StringType(), True),
                    StructField("settlement_region_value", StringType(), True),
                    StructField("settlement_type", StringType(), True),
                    StructField("settlement_value", StringType(), True),
                    StructField("street_type", StringType(), True),
                    StructField("street_value", StringType(), True),
                    StructField("house", StringType(), True),
                    StructField("flat", StringType(), True),
                    StructField("floor", StringType(), True),
                    StructField("office", StringType(), True),
                    StructField("corpus", StringType(), True),
                    StructField("coordinates", ArrayType(DoubleType()), True),
                    StructField("coord_detalization_lvl", IntegerType(), True),
                ]
            ),
            True,
        ),
    ]
)

normalized_addresses_schema = ArrayType(normalized_address_schema)
actuality_date_schema = DateType()
relationship_schema = IntegerType()
raw_metadata_schema = StringType()
normalize_kz_letters_schema = StringType()
