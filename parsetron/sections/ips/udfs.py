from pyspark.sql.functions import udf

from .validators.ip_address import ip_address
from .validators.ip_address_date import ip_address_date
from .validators.ip import ip
from .schemas import ip_address_schema, ip_address_date_schema, ip_schema

ip_address_udf = udf(ip_address, ip_address_schema)
ip_date_udf = udf(ip_address_date, ip_address_date_schema)
ip_udf = udf(ip, ip_schema)
