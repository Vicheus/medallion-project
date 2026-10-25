from pyspark.sql.functions import udf

from .validators.device_date import device_date
from .validators.device import device
from .schemas import device_date_schema, device_schema

device_date_udf = udf(device_date, device_date_schema)
device_udf = udf(device, device_schema)
