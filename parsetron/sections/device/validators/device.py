from typing import Optional, Dict, Union
from .device_date import device_date


def device(
    title: str = None,
    user_agent: str = None,
    date: str = None,
    action: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    date = device_date(date, date_format)

    return {
        "title": title,
        "user_agent": user_agent,
        "date": date,
        "action": action,
        "comment": comment,
    }
