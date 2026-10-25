from typing import Optional, Dict, Union
from .education_level import education_level
from .education_date import education_date

from parsetron.sections.base.validators.base import base_validation


def education(
    title: str = None,
    level: str = None,
    country: str = None,
    date_start: str = None,
    date_end: str = None,
    comment: str = None,
    date_format: str = "%Y-%m-%d",
) -> Optional[Dict[str, Union[int, str]]]:
    title = base_validation(title)
    level = education_level(level)

    if (not title) & (not level):
        return

    date_start = education_date(date_start, date_format)
    date_end = education_date(date_end, date_format)

    return {
        "title": title,
        "level": level,
        "country": country,
        "date_start": date_start,
        "date_end": date_end,
        "comment": comment,
    }
