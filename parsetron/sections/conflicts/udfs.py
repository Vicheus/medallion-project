from pyspark.sql.functions import udf

from .validators.conflicts import conflict
from .schemas import conflict_schema

conflict_udf = udf(conflict, conflict_schema)
