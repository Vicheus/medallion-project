import re
from typing import Optional


def validate_tag_number(value: Optional[str]) -> Optional[str]:
    if value and len(value) > 5:
        parsed_value = re.sub(r"[^а-яёА-ЯЁ0-9]", "", value)
        if parsed_value:
            parsed_value = parsed_value.upper()
            pattern = re.compile(r"^[А-ЯЁ]{1,2}\d{4,7}$")
            if pattern.match(parsed_value):
                digits = re.sub(r"\D", "", parsed_value)
                digits_count = len(digits)
                if digits_count != 6:
                    print(
                        f"Potentially wrong digits length ({digits_count}) in tag number: `{value}`"
                    )
                if set(digits) != {"0"}:
                    return parsed_value
        print(
            f"Unable to parse tag number: `{value}`, partially parsed: `{parsed_value}`"
        )
    return None
