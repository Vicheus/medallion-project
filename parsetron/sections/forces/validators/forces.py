from typing import Optional, Dict, Union

from .base import base_validation
from .callsign import validate_callsign
from .category import validate_category
from .mos_code import validate_mos_code
from .tag_number import validate_tag_number
from .unit_code import validate_unit_code
from ...base.validators.date import base_date_validation


# TODO: Add date `date_start < date_end` validation
def force(
    tag_number: Optional[str] = None,
    unit_code: Optional[str] = None,
    unit_name: Optional[str] = None,
    callsign: Optional[str] = None,
    rank: Optional[str] = None,
    position: Optional[str] = None,
    mos_code: Optional[str] = None,
    category: Optional[str] = None,
    date_start: Optional[str] = None,
    date_end: Optional[str] = None,
    comment: Optional[str] = None,
    date_format: str = "%Y-%m-%d",
) -> Optional[Dict[str, Union[Optional[int], Optional[str]]]]:
    parsed_tag_number = validate_tag_number(tag_number)
    parsed_unit_code = validate_unit_code(unit_code)
    parsed_unit_name = base_validation(unit_name)
    parsed_position = base_validation(position)
    parsed_mos_code = validate_mos_code(mos_code)

    if (
        not parsed_tag_number
        and not parsed_unit_code
        and not parsed_unit_name
        and not parsed_position
        and not parsed_mos_code
    ):
        return None

    parsed_callsign = validate_callsign(callsign)
    parsed_rank = base_validation(rank)
    parsed_category = validate_category(category)
    parsed_date_start = base_date_validation(
        date_start, date_format, max_years_from=115, max_years_to=0
    )
    parsed_date_end = base_date_validation(
        date_end, date_format, max_years_from=115, max_years_to=0
    )
    comment = base_validation(comment)

    return {
        "tag_number": parsed_tag_number,
        "unit_code": parsed_unit_code,
        "unit_name": parsed_unit_name,
        "callsign": parsed_callsign,
        "rank": parsed_rank,
        "position": parsed_position,
        "mos_code": parsed_mos_code,
        "category": parsed_category,
        "date_start": parsed_date_start,
        "date_end": parsed_date_end,
        "comment": comment,
    }
