from datetime import datetime
from typing import Optional

from parsetron.sections.base.validators.date import date_validation, format_date


def death_date(
    dd: str, birth_date: Optional[str] = None, dd_format: str = "%d.%m.%Y"
) -> Optional[str]:
    parsed_dd: Optional[datetime] = date_validation(
        dd, dd_format, max_years_from=70, max_years_to=0
    )
    if not parsed_dd:
        return None
    if birth_date:
        parsed_bd: Optional[datetime] = date_validation(
            birth_date, "%d.%m.%Y", max_years_from=115, max_years_to=0
        )
        if parsed_bd and parsed_bd >= parsed_dd:
            return None
    return format_date(parsed_dd)
