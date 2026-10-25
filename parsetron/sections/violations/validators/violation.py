from typing import Optional, Dict, Union
from .date import validate_date
from parsetron.sections.base.validators.base import base_validation


def violation(
    title: str = None,
    date: int = None,
    serial: str = None,
    penalty_fare: str = None,
    insurance: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    date = validate_date(date, date_format)
    comment = base_validation(comment)

    if title and (len(title) > 255):
        title = title[:255]

    return {
        "title": title,
        "date": date,
        "serial": serial,
        "penalty_fare": penalty_fare,
        "insurance": insurance,
        "comment": comment,
    }
