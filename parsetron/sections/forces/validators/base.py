import re
from typing import Optional

from parsetron.sections.base.validators.base import (
    clean_whitespace,
    is_ukrainian_symbols,
)


def strip_noise(value: str) -> str:
    value = value.lstrip(" /,.-")
    value = value.rstrip(" /-")
    value = re.sub(r"[ /,-][ /,.-]+$", "", value)
    return value


def base_validation(value: Optional[str]) -> Optional[str]:
    if value and len(value) > 1 and not is_ukrainian_symbols(value):
        parsed_value = re.sub(r"[^a-zA-Zа-яёА-ЯЁ0-9/\-., '\s]", " ", value)
        if parsed_value:
            parsed_value = clean_whitespace(strip_noise(parsed_value))
            if len(parsed_value) > 1 and len(set(parsed_value.lower())) > 1:
                return parsed_value
    return None
