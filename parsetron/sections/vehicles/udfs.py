from pyspark.sql.functions import udf

from .validators.vehicle import vehicle
from .schemas import vehicle_schema

vehicle_udf = udf(vehicle, vehicle_schema)
