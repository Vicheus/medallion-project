import phonenumbers
from typing import Optional, List


def phone(string: str, region: str = "RU") -> Optional[str]:
    try:
        string = phonenumbers.parse(string, region=region)
    except phonenumbers.NumberParseException:
        return None

    if not phonenumbers.is_valid_number(
        string
    ) or not phonenumbers.is_valid_number_for_region(string, region):
        return

    string = phonenumbers.format_number(
        string, phonenumbers.PhoneNumberFormat.E164
    ).replace("+", "")

    if len(set(string)) > 3:
        return string


def phones(phones: List[str], region: str = "RU") -> Optional[List[str]]:
    if not phones:
        return None

    formatted_phones = set()
    for phone_value in phones:
        formatted_phone = phone(phone_value, region)
        if not formatted_phone:
            continue

        formatted_phones.add(formatted_phone)

    return list(formatted_phones) if len(formatted_phones) > 0 else None
