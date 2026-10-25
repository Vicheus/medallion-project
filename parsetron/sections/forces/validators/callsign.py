import re
from typing import Optional

from parsetron.sections.base.validators.base import clean_whitespace


def validate_callsign(value: Optional[str]) -> Optional[str]:
    if value:
        parsed_value = re.sub(r"[^a-zA-Zа-яёА-ЯЁ0-9\- ]", " ", value)
        if parsed_value:
            parsed_value = clean_whitespace(parsed_value.strip(" -"))
            if len(set(parsed_value.lower())) > 1 and parsed_value.count(" ") < 4:
                return parsed_value
    return None
