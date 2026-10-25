import re
from typing import Optional

from ..settings import (
    UKRAINIAN_SYMBOLS,
    SPECIAL_SYMBOLS,
    STOP_WORDS,
    WHITESPACE_SYMBOLS,
    CYRILLIC_SYMBOLS,
    SPECIAL_ADDRESS_SYMBOLS,
    SPECIAL_RAW_SYMBOLS,
)


def base_validation(string: Optional[str]) -> Optional[str]:
    """
    Validate the input string based on certain conditions:

    - If the string contains Ukrainian symbols, return None.
    - If the string contains stop words, return None.
    - Clean the string by removing special symbols and excess whitespace.

    :param string: Input string to validate.
    :return: Cleaned string or None if validation fails.
    """
    if string is None or not string:
        return

    if is_ukrainian_symbols(string):
        return

    if is_stop_words_exist(string):
        return

    if is_single_character_or_digit_exist(string):
        return

    string = clean_whitespace(remove_special_symbols(string))
    return string


def base_address_validation(string: str) -> Optional[str]:
    if string is None or not string:
        return None

    if is_ukrainian_symbols(string):
        return None

    if is_stop_words_exist(string):
        return None

    if is_single_character_or_digit_exist(string):
        return None

    string = re.sub(SPECIAL_ADDRESS_SYMBOLS, " ", string)
    string = clean_whitespace(string)
    return string


def base_raw_validation(string: Optional[str]) -> Optional[str]:
    if string is None or not string:
        return

    if is_ukrainian_symbols(string):
        return

    string = re.sub(SPECIAL_RAW_SYMBOLS, "", string)
    string.replace("()", " ")
    string = clean_whitespace(string)
    string = re.sub(r"\?+", "?", string)
    string = string.lstrip(" _\\,;/?)*:-")
    string.rstrip(" _\\,;/(*:-")
    if len(string) > 1:
        return string
    return None


def is_ukrainian_symbols(string: str) -> bool:
    """
    Check if the given string contains any Ukrainian symbols.
    """
    pattern = re.compile(UKRAINIAN_SYMBOLS)
    return bool(pattern.search(string))


def is_cyrillic_symbols(string: str) -> bool:
    """
    Check if the given string contains any cyrillic symbols.
    """
    pattern = re.compile(CYRILLIC_SYMBOLS)
    return bool(pattern.search(string))


def remove_special_symbols(string: str) -> str:
    """
    Remove all special symbols from the given string.
    """
    return re.sub(SPECIAL_SYMBOLS, "", string)


def is_stop_words_exist(string: str) -> bool:
    """
    Check if the given string contains any stop words.
    """
    words = string.split()
    stop_words = {w.lower() for w in STOP_WORDS}
    return any(word.lower() in stop_words for word in words)


def clean_whitespace(string: str) -> str:
    """
    Remove all leading and trailing whitespace, including tabs and &nbsp;,
    and replace multiple spaces with a single space.
    """
    for symbol in WHITESPACE_SYMBOLS:
        string = string.replace(symbol, " ")

    string = re.sub(r"\s+", " ", string)

    return string.strip()


def is_single_character_or_digit_exist(string: str) -> bool:
    """
    Check if the given string contains only single characters or digits.
    """
    pattern = re.compile(r"^(.)\1*$")
    return bool(pattern.match(string.lower())) if string else False
