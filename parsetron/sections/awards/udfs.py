from pyspark.sql.functions import udf

from .validators.award import award
from .schemas import award_schema

award_udf = udf(award, award_schema)
