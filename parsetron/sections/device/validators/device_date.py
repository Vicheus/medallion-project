from typing import Optional
from parsetron.sections.base.validators.date import base_date_validation


def device_date(
    string: str,
    date_format: Optional[str] = "%Y-%m-%d",
    short: Optional[bool] = False,
) -> Optional[str]:
    return base_date_validation(string, date_format, max_years_to=100)
