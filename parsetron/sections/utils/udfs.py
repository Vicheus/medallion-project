import re

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from parsetron.sections.base.validators.base import base_raw_validation

base_raw_validation_udf = udf(base_raw_validation, StringType())


def regexp_replace_all_udf(regex: dict[str, str]):
    def regexp_replace_all(value: str):
        if not value or not regex:
            return value
        for pattern, replacement in regex.items():
            value = re.sub(pattern, replacement, value)
        return value

    return udf(regexp_replace_all, StringType())
