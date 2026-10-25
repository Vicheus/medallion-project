from datetime import datetime
from typing import Optional

from parsetron.sections.base.validators.date import date_validation


def actuality_date(string: str, date_format: str = "yyyy-MM-dd") -> Optional[datetime]:
    return date_validation(string, date_format, max_years_from=30, max_years_to=0)


def latest_actuality_date(
    *dates: str, date_format: str = "yyyy-MM-dd"
) -> Optional[datetime]:
    parsed_dates = []
    for date in dates:
        parsed_date = actuality_date(date, date_format)
        if parsed_date:
            parsed_dates.append(parsed_date)
    return max(parsed_dates, default=None)
