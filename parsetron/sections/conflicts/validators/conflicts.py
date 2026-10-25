from typing import Optional, Dict, Union
from .date_start import validate_date_start
from .date_end import validate_date_end
from .type import validate_type
from parsetron.sections.base.validators.base import base_validation


def conflict(
    title: str = None,
    country: str = None,
    region: str = None,
    type: int = None,
    date_start: str = None,
    date_end: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    date_start = validate_date_start(date_start, date_format)
    date_end = validate_date_end(date_end, date_format)

    type = validate_type(type)
    comment = base_validation(comment)

    return {
        "title": title,
        "country": country,
        "region": region,
        "type": type,
        "date_start": date_start,
        "date_end": date_end,
        "comment": comment,
    }
