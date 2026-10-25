from typing import Optional
from parsetron.sections.base.validators.date import base_date_validation


def ticket_order_datetime(
    string: str, date_format: str = "%Y-%m-%d %H:%M:%S"
) -> Optional[str]:
    return base_date_validation(
        string, date_format, result_date_format="%d.%m.%Y %H:%M"
    )
