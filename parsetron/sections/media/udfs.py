from parsetron.sections.media.media import media
from pyspark.sql.functions import udf
from .schemas import media_schema

media_udf = udf(media, media_schema)
