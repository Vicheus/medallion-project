import re
from typing import Optional, List

from parsetron.sections.base.validators.base import base_validation, is_cyrillic_symbols
from parsetron.sections.main.settings import ALLOWED_SHORT_NAMES
from parsetron.utils import TextAnalyser
from parsetron.utils import NamesExtractor


def name(string: str) -> Optional[str]:
    value = base_validation(string)
    if not value:
        return None

    lowered = value.lower()
    compact = lowered.replace(" ", "")

    if len(compact) <= 2:
        return None

    if len(set(compact)) <= 3 and lowered not in ALLOWED_SHORT_NAMES:
        return None

    number_pattern = re.compile(r"\d")
    if number_pattern.search(value):
        return None

    value = value.strip(" .-")

    return value.title()


def names(names: List[str]) -> Optional[List[str]]:
    if not names:
        return None

    formatted_names = set()
    for name_value in names:
        formatted_name = name(name_value)
        if not formatted_name:
            continue

        formatted_names.add(formatted_name)

    return list(formatted_names) if len(formatted_names) > 0 else None


def name_parts(first_name: str, last_name: str, middle_name: str) -> Optional[str]:
    return name_parts_ordered(last_name, first_name, middle_name)


def name_parts_ordered(*args: str) -> Optional[str]:
    full_name = " ".join(x.strip() for x in args if x and x.strip())
    return name(full_name)


def validate_name_is_person_or_organisation(names: List[str]) -> Optional[List[str]]:
    if not names:
        return None

    validated_names = set()
    for name_value in names:
        if (is_cyrillic_symbols(name_value)) & (
            not TextAnalyser.is_person_or_organisation(name_value)
        ):
            continue

        validated_names.add(name_value)

    return list(validated_names) if len(validated_names) > 0 else None


def extract_name(name_str: str) -> Optional[str]:
    if not name_str:
        return None

    return NamesExtractor.NamesExtractor.extract_name(name_str)
