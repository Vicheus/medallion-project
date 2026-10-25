from typing import Optional
from .document_serial_base import (
    document_serial,
    extract_pattern,
    document_serial_digits,
)


def document_serial_passport(string: str) -> Optional[str]:
    """
    Processes the given string to extract a passport serial number for Belarus by removing all non-alphanumeric
    characters, checking if the length is exactly 9 symbols (2 cyrillic letters with 7 digits), and ensuring the serial
    number is not made up of identical digits.

    :param string: The input string containing the passport serial number.
    :return: The cleaned passport serial number consisting of exactly 9 symbols, or None if the length of the cleaned
             string is not 9 or if the serial number consists of identical digits.
    """
    string = document_serial(string)
    if string:
        string = string.upper()
        string = extract_pattern(r"((АВ|ВМ|НВ|КН|МР|МС|КВ|РР)\d{7})(?![0-9])", string)
    return string


def document_serial_diplomatic_passport(string: str) -> Optional[str]:
    """
    Processes the given string to extract a diplomatic passport serial number for Belarus by removing all
    non-alphanumeric characters, checking if the length is exactly 9 symbols (2 letters with 7 digits), and ensuring the
    serial number is not made up of identical digits.

    :param string: The input string containing the diplomatic passport serial number.
    :return: The cleaned diplomatic passport serial number consisting of exactly 9 symbols, or None if the length of the
             cleaned string is not 9 or if the serial number consists of identical digits.
    """
    string = document_serial(string)
    if string:
        string = string.upper()
        string = extract_pattern(r"((DP|SP)\d{7})(?![0-9])", string)
    return string


def document_serial_id_number(string: str):
    """
    Processes the given string to extract a inn serial number for Belarus by removing all non-alphanumeric characters,
    checking if the length is exactly 14 symbols and ensuring the serial number is not made up of identical digits.

    :param string: The input string containing the inn serial number.
    :return: The cleaned inn serial number consisting of exactly 14 symbols, or None if the length of the cleaned string is not 14
    or if the serial number consists of identical digits.
    """
    if not string:
        return
    id_num = document_serial_digits(string)

    if (len(set(id_num)) <= 1) or len(id_num) != 14:
        return

    return id_num


def document_serial_inn(string: str):
    """
    Processes the given string to extract a inn serial number for Belarus by removing all non-alphanumeric characters,
    checking if the length is exactly 9 symbols (for organization and individual), and ensuring the serial number is not made up of identical digits.

    :param string: The input string containing the inn serial number.
    :return: The cleaned inn serial number consisting of exactly 9 symbols, or None if the length of the cleaned string is not 9
    or if the serial number consists of identical digits.
    """
    string = document_serial_digits(string)
    if not string:
        return

    if (len(set(string)) <= 1) or len(string) != 9:
        return

    return string


def document_serial_unp(string: str):
    """
    Processes the given string to extract a unp serial number for Belarus,
    checking if the length is exactly 9 digits, and ensuring the serial number is not made up of identical digits, validate unp checksum.

    :param string: The input string containing the unp serial number.
    :return: The cleaned unp serial number or None if provided string is not valid unp.
    """
    if not string:
        return

    unp = string

    if len(unp) != 9:
        return

    weights = [29, 23, 19, 17, 13, 7, 5, 3]
    sum_ = 0

    try:
        sum_ += int(unp[7]) * weights[7]
        sum_ += int(unp[6]) * weights[6]
        sum_ += int(unp[5]) * weights[5]
        sum_ += int(unp[4]) * weights[4]
        sum_ += int(unp[3]) * weights[3]
        sum_ += int(unp[2]) * weights[2]
    except ValueError:
        return

    second_char_map = {
        "A": 0,
        "B": 1,
        "C": 2,
        "E": 3,
        "H": 4,
        "K": 5,
        "M": 6,
        "O": 7,
        "P": 8,
        "T": 9,
    }
    second_char = unp[1]
    if second_char in second_char_map:
        sum_ += second_char_map[second_char] * weights[1]
    else:
        try:
            sum_ += int(second_char) * weights[1]
        except ValueError:
            return

    first_char_map = {"A": 10, "B": 11, "C": 12, "E": 14, "H": 17, "K": 20, "M": 22}
    first_char = unp[0]
    if first_char in first_char_map:
        sum_ += first_char_map[first_char] * weights[0]
    else:
        try:
            sum_ += int(first_char) * weights[0]
        except ValueError:
            return

    try:
        checksum = int(unp[8])
    except ValueError:
        return

    if checksum == (sum_ % 11):
        return unp
    else:
        return
