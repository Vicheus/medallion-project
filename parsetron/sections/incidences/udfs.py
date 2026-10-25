from pyspark.sql.functions import udf

from .validators.incidence import incidence
from .validators.incidence_date import incidence_date
from .schemas import incidence_schema, incidence_date_schema

incidence_udf = udf(incidence, incidence_schema)
incidence_date_udf = udf(incidence_date, incidence_date_schema)
