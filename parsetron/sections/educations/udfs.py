from pyspark.sql.functions import udf

from .validators.education_level import education_level
from .validators.education import education
from .validators.education_date import education_date
from .schemas import education_date_schema, education_level_schema, education_schema

education_level_udf = udf(education_level, education_level_schema)
education_udf = udf(education, education_schema)
education_date_udf = udf(education_date, education_date_schema)
