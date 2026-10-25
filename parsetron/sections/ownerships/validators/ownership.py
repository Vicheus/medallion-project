from typing import Optional, Dict, Union
from .date import validate_date
from .type import validate_type
from parsetron.sections.base.validators.base import base_validation


def ownership(
    title: str = None,
    type: int = None,
    date: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    date = validate_date(date, date_format)
    type = validate_type(type)
    comment = base_validation(comment)

    return {"title": title, "type": type, "date": date, "comment": comment}
