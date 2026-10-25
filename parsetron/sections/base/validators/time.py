from datetime import datetime
from typing import Optional
from parsetron.settings import TIME_FORMAT


def base_time_validation(
    string: str,
    input_time_format: Optional[str] = "%H:%M:%S",
    output_time_format: Optional[str] = TIME_FORMAT,
) -> Optional[str]:
    if not string:
        return
    string = string.strip()

    if not string:
        return

    try:
        time_object = datetime.strptime(string, input_time_format)
    except ValueError:
        return

    string = time_object.strftime(output_time_format)

    return string
