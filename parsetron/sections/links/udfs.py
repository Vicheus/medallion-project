from pyspark.sql.functions import udf

from .validators.link import link
from .schemas import link_schema

link_udf = udf(link, link_schema)
