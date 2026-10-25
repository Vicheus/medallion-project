import re
from typing import Optional
from .document_serial_base import (
    document_serial,
    document_serial_digits,
    extract_pattern,
)
from datetime import date
from datetime import datetime


def document_serial_passport(string: str) -> Optional[str]:
    """
    Processes the given string to extract a passport serial number for Kazakhstan by removing all non-alphanumeric
    characters, checking if the length is exactly 9 symbols, and ensuring the serial number is not made up of identical
    digits. Also check first letter symbol of serial number which should be exactly - N.

    :param string: The input string containing the passport serial number.
    :return: The cleaned passport serial number consisting of exactly 9 symbols, or None if the length of the cleaned
             string is not 9 or if the serial number consists of identical digits or serial number is not correct.
    """
    string = document_serial(string)
    if string:
        string = string.upper()
        string = extract_pattern(r"(N\d{8})(?![0-9])", string)

    return string


def document_serial_inn(string: str):
    """
    Processes the given string to extract a inn serial number\bin serial number for Kazakhstan by removing all non-digit characters,
    checking if the length is exactly 12 digits, and ensuring the serial number is not made up of identical digits,
    also checking checksum of inn by algorythm.

    :param string: The input string containing the inn serial number.
    :return: The cleaned inn serial number consisting of exactly 12 digits, or None if the length of the cleaned string is not 12
             or if the serial number consists of identical digits or if checksum not valid.
    """

    def validate_inn(numbers: list[int]) -> bool:
        year = ""
        month = int(f"{numbers[2]}{numbers[3]}") - 1

        if not in_range(month, 0, 11):
            return False

        day = int(f"{numbers[4]}{numbers[5]}")

        if not in_range(numbers[6], 1, 6):
            return False

        if numbers[6] in [1, 2]:
            year = f"18{numbers[0]}{numbers[1]}"
        elif numbers[6] in [3, 4]:
            year = f"19{numbers[0]}{numbers[1]}"
        elif numbers[6] in [5, 6]:
            year = f"20{numbers[0]}{numbers[1]}"

        is_leap_year = int(year) % 4 == 0
        if not in_range(day, 1, 31) or (
            month == 1 and is_leap_year and not in_range(day, 1, 29)
        ):
            return False

        birthDate = date(int(year), month + 1, day)

        if not birthDate:
            return False

        return True

    def validate_bin(numbers: list[int]) -> bool:
        current_year = datetime.now().year
        year = int(f"{numbers[0]}{numbers[1]}")
        year = 2000 + year if current_year - 2000 >= year else 1900 + year

        month = int(f"{numbers[2]}{numbers[3]}") - 1
        if not in_range(month, 0, 11):
            return False

        registration_date = date(year, month + 1, 1)
        if not registration_date:
            return False

        return True

    def in_range(needle: int, min_val: int, max_val: int) -> bool:
        return min_val <= needle <= max_val

    def is_iin(type_number: int) -> bool:
        if not in_range(type_number, 0, 6):
            raise ValueError("invalid identification number")
        return (type_number <= 6) & (type_number > 0)

    def validate_checksum(numbers: list[int]) -> bool:
        standard_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        alternative_sequence = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]

        if len(numbers) != 12:
            return False

        control_digit = sum(s * n for s, n in zip(standard_sequence, numbers)) % 11

        if control_digit == 10:
            control_digit = (
                sum(s * n for s, n in zip(alternative_sequence, numbers)) % 11
            )

        return control_digit == numbers[11]

    if not string:
        return

    inn_numbers = [int(s) for s in string if s.isdigit()]

    if len(inn_numbers) == 11:
        inn_numbers.insert(0, 0)

    if len(set(inn_numbers)) <= 1:
        return

    try:
        is_checksum_valid = validate_checksum(inn_numbers)
        if not is_checksum_valid:
            return
        if is_iin(inn_numbers[6]):
            if not validate_inn(inn_numbers):
                return
        else:
            if not validate_bin(inn_numbers):
                return

        inn = "".join(str(n) for n in inn_numbers)
        if not inn.isdigit():
            return

        return inn
    except Exception as e:
        print(f"""Error validation INN\BIN {e}""")
        return


def document_serial_id_number(string: str):
    """
    Processes the given string to extract a id serial number for Kazakhstan by removing all non-alphanumeric characters,
    checking if the length is exactly 14 symbols and ensuring the serial number is not made up of identical digits.

    :param string: The input string containing the id serial number.
    :return: The cleaned id serial number consisting of exactly 9 symbols, or None if the length of the cleaned string is not 9
    or if the serial number consists of identical digits.
    """
    if not string:
        return
    id_num = document_serial_digits(string)

    if (len(set(id_num)) <= 1) or len(id_num) != 9:
        return

    return id_num


def document_serial_driver_license(string: str):
    """
    Processes the given string to extract a driver license serial number for Kazakhstan by removing all non-alphanumeric characters,
    checking if the length is exactly 10 symbols and ensuring the serial number is not made up of identical digits.
    Also check that series is correct - 2 letters + 2 numbers of 4 numbers

    :param string: The input string containing the driver license serial number.
    :return: The cleaned driver license serial number consisting of exactly 10 symbols, or None if the length of the cleaned string is not 10
    or if the serial number consists of identical digits.
    """
    if not string:
        return
    driver_license_num = document_serial(string)

    pattern = r"^(?:[A-Za-z]{2}\d{8}|\d{10})$"
    if (
        (not bool(re.match(pattern, driver_license_num)))
        or (len(set(driver_license_num)) <= 1)
        or (len(driver_license_num) != 10)
    ):
        return

    return driver_license_num


def document_serial_seaman_passport(string: str):
    """
    Processes the given string to extract a seaman passport serial number for Kazakhstan by removing all non-alphanumeric characters,
    checking if the length is no more than 10 symbols and ensuring the serial number is not made up of identical digits.

    :param string: The input string containing the seaman passport serial number.
    :return: The cleaned seaman passport serial number consisting of no more than 10 symbols, or None if the length of the cleaned string is more than 10 symbols
    or if the serial number consists of identical digits.
    """
    if not string:
        return
    seaman_passport_num = document_serial(string)

    if (len(set(seaman_passport_num)) <= 1) or (len(seaman_passport_num) > 10):
        return

    return seaman_passport_num
