import re
from typing import Optional

from parsetron.sections.base.validators.base import clean_whitespace


def validate_unit_code(value: Optional[str]) -> Optional[str]:
    if value:
        parsed_value = re.sub(r"[^а-яёА-ЯЁ0-9]", " ", value)
        if parsed_value:
            parsed_value = clean_whitespace(parsed_value.upper())
            if parsed_value.startswith("В"):
                parsed_value = (
                    parsed_value.replace("В Ч", "")
                    .replace("ВОЙСКОВАЯ ЧАСТЬ", "")
                    .strip()
                )
            pattern = re.compile(
                r"^(\d{5} ?[А-ЯЁ]{0,2}|\d{5} ?\d{0,3}|\d{4}|\d{5} ?[0-9]{1,2} ?[А-ЯЁ])$"
            )
            if (
                pattern.match(parsed_value)
                and len(set(re.sub(r"\D", "", parsed_value))) > 1
            ):
                return parsed_value
        print(
            f"Unable to parse unit code: `{value}`, partially parsed: `{parsed_value}`"
        )
    return None
