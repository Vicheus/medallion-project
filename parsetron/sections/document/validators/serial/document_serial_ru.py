from typing import Optional

from .document_serial_base import (
    document_serial,
    extract_pattern,
)


def document_serial_passport(value: str) -> Optional[str]:
    """
    Processes the given string to extract a passport serial number for Russia ensuring the serial number is not made up
    of identical digits, extracting number according to the regular expression, checking if the length is exactly 10
    digits.

    :param value: The input string containing the passport serial number.
    :return: The cleaned passport serial number consisting of exactly 10 digits, or None if the length of the cleaned string is not 10
             or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    value = extract_pattern(r"(?<![0-9])(\d{10})(?![0-9])", value)

    if not value or value.startswith("00"):
        return None
    return value


def _calculate_snils_control_sum(value: str) -> int:
    numbers = [int(value[i]) * (9 - i) for i in range(9)]
    numbers_sum = sum(numbers)
    remainder = numbers_sum % 101
    return 0 if remainder == 100 else remainder


def document_serial_snils(string: str):
    """
    Processes the given string to extract a snils serial number for Russia by removing all non-digit characters,
    checking if the length is exactly 11 digits, and ensuring the serial number is not made up of identical digits also checking control sum of snils by algorythm.

    :param string: The input string containing the snils serial number.
    :return: The cleaned snils serial number consisting of exactly 11 digits, or None if the length of the cleaned string is not 11
             or if the serial number consists of identical digits.
    """
    if not string:
        return None

    string = "".join([s for s in string if s.isdigit()])

    if len(string) == 9:
        string = f"00{string}"

    if len(string) == 10:
        string = f"0{string}"

    if len(string) != 11 or len(set(string)) <= 1:
        return None

    control_sum = _calculate_snils_control_sum(string)
    snils_last_digits = string[9:11]
    if control_sum != int(snils_last_digits):
        return None

    return string


def document_serial_snils_without_control_sum(value: str):
    """
    Processes the given string to extract a snils serial number for Russia by removing all non-digit characters,
    checking if the length is exactly 9 digits, and ensuring the serial number is not made up of identical digits also
    adding control sum of snils by algorythm.

    :param value: The input string containing the snils serial number.
    :return: The cleaned snils serial number consisting of exactly 11 digits including 2 appended, or None if the length
             of the cleaned string is not 9 or if the serial number consists of identical digits.
    """
    if not value:
        return None

    value = "".join([s for s in value if s.isdigit()])

    if len(set(value)) < 2 or len(value) != 9:
        return None

    control_sum = _calculate_snils_control_sum(value)
    if control_sum < 10:
        control_sum = f"0{control_sum}"
    value = f"{value}{control_sum}"

    return value


def document_serial_inn(string: str):
    """
    Processes the given string to extract a inn serial number for Russia by removing all non-digit characters,
    checking if the length is exactly 10 or 12 digits (for organization or individual), and ensuring the serial number is not made up of identical digits,
    also checking checksum of inn by algorythm.

    :param string: The input string containing the inn serial number.
    :return: The cleaned inn serial number consisting of exactly 10 or 12 digits, or None if the length of the cleaned string is not 10/12
             or if the serial number consists of identical digits.
    """
    if not string:
        return None

    inn = "".join([s for s in string if s.isdigit()])

    if len(set(inn)) <= 1:
        return None

    try:
        if not inn.isdigit():
            return None

        # Organization INN
        if len(inn) == 10:
            weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
            checksum = sum(int(inn[i]) * weights[i] for i in range(9)) % 11
            checksum = checksum if checksum < 10 else checksum % 10
            if checksum != int(inn[9]):
                return None

        # Sometimes 11 digit inn occurred when 0 at start missed
        if len(inn) == 11:
            inn = f"""0{inn}"""

        # Individual INN
        if len(inn) == 12:
            weights_11 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
            weights_12 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

            checksum_11 = sum(int(inn[i]) * weights_11[i] for i in range(10)) % 11
            checksum_11 = checksum_11 if checksum_11 < 10 else checksum_11 % 10

            checksum_12 = sum(int(inn[i]) * weights_12[i] for i in range(11)) % 11
            checksum_12 = checksum_12 if checksum_12 < 10 else checksum_12 % 10

            if (checksum_11 != int(inn[10])) or (checksum_12 != int(inn[11])):
                return None

            return inn
        else:
            return None
    except:  # noqa: E722
        return None


def document_serial_driver_license(value: str) -> Optional[str]:
    """
    Processes the given string to extract a driver license serial number for Russia ensuring the serial number is not
    made up of identical digits, extracting number according to the regular expression, checking if the length is
    exactly 10 symbols.

    :param value: The input string containing the driver license serial number.
    :return: The cleaned driver license serial number consisting of exactly 10 digits (or 2 digits, 2 cyrillic letters,
             6 digits), or None if the length of the cleaned string is not 10 or if the serial number consists of
             identical digits.
    """

    value = document_serial(value)
    if value:
        value = value.upper()
        value = extract_pattern(
            r"(?<![0-9])(\d{10}|\d{2}[А-ЯЁ]{2}\d{6})(?![0-9])", value
        )

    if not value or value.startswith("00"):
        return None
    return value


def document_serial_international_passport(value: str) -> Optional[str]:
    """
    Processes the given string to extract an international passport serial number for Russia ensuring the serial number
    is not made up of identical digits, extracting number according to the regular expression, checking if the length is
    exactly 9 symbols.

    :param value: The input string containing the international passport serial number.
    :return: The cleaned international passport serial number consisting of exactly 9 digits, or None if the length of
             the cleaned string is not 9 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    value = extract_pattern(r"(?<![0-9])(([5-8][0-9]|9[0-8])\d{7})(?![0-9])", value)
    return value


def document_serial_birth_certificate(value: str) -> Optional[str]:
    """
    Processes the given string to extract a birth certificate serial number for Russia ensuring the serial number
    is not made up of identical digits, extracting number according to the regular expression, checking if the length is
    between 9 and 13.

    :param value: The input string containing the birth certificate serial number.
    :return: The cleaned birth certificate serial number consisting of 9-13 symbols (last 6 is always digits), or None
             if the length of the cleaned string is not 9-13 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    if value:
        value = value.upper()
        # Pattern can be extended with prefixed Cyrillic УХЛС letters that corresponds to VXLC if required
        value = extract_pattern(
            r"(((?<![0-9])([2-9]|1+)|[IVXLCDM]+)[А-ЯЁ]{2}\d{6})(?![0-9])",
            value,
        )
        if not value or len(value) > 13:
            return None
    return value


def document_serial_resident_card(value: str) -> Optional[str]:
    """
    Processes the given string to extract a resident card serial number for Russia ensuring the serial number
    is not made up of identical digits, extracting number according to the regular expression, checking if the length is
    exactly 9 symbols.

    :param value: The input string containing the resident card serial number.
    :return: The cleaned resident card serial number consisting of exactly 9 digits, or None if the length of
             the cleaned string is not 9 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    value = extract_pattern(r"(?<![0-9])((8[0-3]|90)\d{6,7})(?![0-9])", value)

    if value and len(value) == 8:
        value = value[:2] + "0" + value[2:]

    return value


def document_serial_diplomatic_passport(value: str) -> Optional[str]:
    """
    Processes the given string to extract a diplomatic passport serial number for Russia ensuring the serial number is
    not made up of identical digits, extracting number according to the regular expression, checking if the length is
    exactly 9 digits.

    :param value: The input string containing the diplomatic passport serial number.
    :return: The cleaned diplomatic passport serial number consisting of exactly 9 digits, or None if the length of the
             cleaned string is not 9 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    value = extract_pattern(r"(?<![0-9])(10\d{7})(?![0-9])", value)
    return value


def document_serial_service_passport(value: str) -> Optional[str]:
    """
    Processes the given string to extract a service passport serial number for Russia ensuring the serial number is
    not made up of identical digits, extracting number according to the regular expression, checking if the length is
    exactly 9 digits.

    :param value: The input string containing the service passport serial number.
    :return: The cleaned service passport serial number consisting of exactly 9 digits, or None if the length of the
             cleaned string is not 9 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    value = extract_pattern(r"(?<![0-9])(2[02]\d{7})(?![0-9])", value)
    return value


def document_serial_military_identification_card(value: str) -> Optional[str]:
    """
    Processes the given string to extract a military identification card of a citizen serial number for Russia ensuring
    the serial number is not made up of identical digits, extracting number according to the regular expression,
    checking if the length is exactly 9 symbols.

    :param value: The input string containing the military identification card of a citizen serial number.
    :return: The cleaned military identification card of a citizen serial number consisting of exactly 9 symbols, or
             None if the length of the cleaned string is not 9 or if the serial number consists of identical digits.
    """

    value = document_serial(value)
    if value:
        value = value.upper()
        value = extract_pattern(
            r"(?<![А-ЯЁ])(([А-ЯЁ]{2}\d{7})|([А-ЯЁ]{3}\d{6}))(?![0-9])", value
        )
    return value


def document_serial_kpp(string: str):
    """
    Processes the given string to extract a kpp serial number for Russia by removing all non-digit characters,
    checking if the length is exactly 9 digits, and ensuring the serial number is not made up of identical digits.

    :param string: The input string containing the kpp serial number.
    :return: The cleaned kpp serial number consisting of exactly 9 digits, or None if the length of the cleaned string is not 9
             or if the serial number consists of identical digits.
    """
    if not string:
        return None

    kpp = "".join([s for s in string if s.isdigit()])

    if len(set(kpp)) <= 1:
        return None
    try:
        if not kpp.isdigit():
            return None

        if len(kpp) != 9:
            return None

        return kpp

    except:  # noqa: E722
        return None


def document_serial_ogrn(string: str):
    if not string:
        return None

    ogrn = "".join([s for s in string if s.isdigit()])

    if len(set(ogrn)) <= 1:
        return None

    if not ogrn.isdigit():
        return None
    if len(ogrn) != 13:
        return None
    try:
        n = int(ogrn[:-1])
        control_digit = int(ogrn[-1])
        calculated = int(str(n % 11)[-1])
        if calculated == control_digit:
            return ogrn
        else:
            return None
    except ValueError:
        return None
