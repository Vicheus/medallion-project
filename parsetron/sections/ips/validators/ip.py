from typing import Optional, Dict, Union
from .ip_address import ip_address
from .ip_address_date import ip_address_date
from parsetron.sections.base.validators.base import base_validation


def ip(
    ip: str = None,
    date: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    ip = ip_address(ip)
    date = ip_address_date(date, date_format)
    comment = base_validation(comment)

    return {"ip": ip, "date": date, "comment": comment}
