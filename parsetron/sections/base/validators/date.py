from datetime import datetime
from typing import Optional

from parsetron.settings import DATE_FORMAT


def _parse(string: str, date_format: str) -> Optional[datetime]:
    if not string:
        return None
    try:
        return datetime.strptime(string, date_format)
    except ValueError:
        return None


def _is_valid(
    date: datetime, max_years_from: Optional[int], max_years_to: Optional[int]
) -> bool:
    current_year = datetime.now().year
    if max_years_from and date.year < (current_year - max_years_from):
        return False
    if max_years_to and date.year > (current_year + max_years_to):
        return False
    return True


def date_validation(
    string: str,
    date_format: str = "yyyy-MM-dd",
    max_years_from: Optional[int] = None,
    max_years_to: Optional[int] = None,
) -> Optional[datetime]:
    date = _parse(string, date_format)
    if date and _is_valid(date, max_years_from, max_years_to):
        return date
    return None


def format_date(
    base_date: Optional[datetime], result_date_format: str = DATE_FORMAT
) -> Optional[str]:
    if not base_date:
        return None
    return base_date.strftime(result_date_format)


def base_date_validation(
    string: str,
    date_format: str = "yyyy-MM-dd",
    max_years_from: Optional[int] = None,
    max_years_to: Optional[int] = None,
    result_date_format: str = DATE_FORMAT,
) -> Optional[str]:
    base_date = date_validation(string, date_format, max_years_from, max_years_to)
    return format_date(base_date, result_date_format)
