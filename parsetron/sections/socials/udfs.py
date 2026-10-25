from pyspark.sql.functions import udf

from .validators.social import social
from .schemas import social_schema

social_udf = udf(social, social_schema)
