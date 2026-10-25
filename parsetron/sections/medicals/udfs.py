from pyspark.sql.functions import udf

from .validators.medicals import medicals
from .schemas import medicals_schema

medicals_udf = udf(medicals, medicals_schema)
