import re
from typing import Optional


def validate_mos_code(value: Optional[str]) -> Optional[str]:
    if value and len(value) > 5:
        parsed_value = re.sub(r"[^а-яёА-ЯЁ0-9/]", "", value)
        if parsed_value:
            parsed_value = parsed_value.strip("/").upper()
            pattern = re.compile(r"^(\d{6}[А-ЯЁ]?(/\d{3}[А-ЯЁ]?)?|\d{6}[23])$")
            if (
                pattern.match(parsed_value)
                and len(set(re.sub(r"\D", "", parsed_value))) > 1
            ):
                return parsed_value
        print(
            f"Unable to parse mos code: `{value}`, partially parsed: `{parsed_value}`"
        )
    return None
