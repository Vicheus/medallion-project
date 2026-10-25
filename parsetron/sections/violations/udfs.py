from pyspark.sql.functions import udf

from .validators.violation import violation
from .schemas import violation_schema

violation_udf = udf(violation, violation_schema)
