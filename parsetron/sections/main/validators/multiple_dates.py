from typing import Optional

from parsetron.sections.base.validators.date import base_date_validation
from parsetron.settings import DATE_FORMAT


def multiple_date_formats(
    value: str,
    date_formats: list[str],
    max_years_from: int = 50,
    max_years_to: int = 0,
    result_date_format: str = DATE_FORMAT,
) -> Optional[str]:
    for date_format in date_formats:
        parsed_date = base_date_validation(
            value,
            date_format=date_format,
            max_years_from=max_years_from,
            max_years_to=max_years_to,
            result_date_format=result_date_format,
        )
        if parsed_date:
            return parsed_date
    return None
