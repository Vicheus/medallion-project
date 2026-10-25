from pyspark.sql.functions import udf

from .validators.ownership import ownership
from .schemas import ownership_schema

ownership_udf = udf(ownership, ownership_schema)
