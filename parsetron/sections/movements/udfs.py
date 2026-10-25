from pyspark.sql.functions import udf

from .validators.movement import movement
from .validators.movement_date import movement_date
from .validators.movement_time import movement_time
from .validators.movement_datetime import movement_datetime
from .validators.ticket_order_datetime import ticket_order_datetime
from .validators.movement_code import (
    get_movement_airport_code_by_name,
    get_movement_airport_iata_code_by_slavic_code,
    get_movement_airport_city_by_slavic_code,
    get_movement_airport_city_by_IATA_code,
)
from .schemas import (
    movement_schema,
    movement_date_schema,
    movement_time_schema,
    movement_datetime_schema,
    ticket_order_datetime_schema,
    movement_code_schema,
)

movement_udf = udf(movement, movement_schema)
movement_date_udf = udf(movement_date, movement_date_schema)
movement_time_udf = udf(movement_time, movement_time_schema)
movement_datetime_udf = udf(movement_datetime, movement_datetime_schema)
ticket_order_datetime_udf = udf(ticket_order_datetime, ticket_order_datetime_schema)
get_movement_airport_code_by_name_udf = udf(
    get_movement_airport_code_by_name, movement_code_schema
)
get_movement_airport_iata_code_by_slavic_code_udf = udf(
    get_movement_airport_iata_code_by_slavic_code, movement_code_schema
)
get_movement_airport_city_by_slavic_code_udf = udf(
    get_movement_airport_city_by_slavic_code, movement_code_schema
)
get_movement_airport_city_by_IATA_code_udf = udf(
    get_movement_airport_city_by_IATA_code, movement_code_schema
)
