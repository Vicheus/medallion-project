from typing import Optional
from parsetron.sections.base.validators.time import base_time_validation


def movement_time(string: str, time_format: str = "%H:%M:%S") -> Optional[str]:
    return base_time_validation(
        string, input_time_format=time_format, output_time_format="%H:%M:%S"
    )
