import pytest
from ..validators.base import (
    is_ukrainian_symbols,
    is_cyrillic_symbols,
    remove_special_symbols,
    clean_whitespace,
    is_single_character_or_digit_exist,
    base_validation,
)


@pytest.mark.parametrize(
    "param, expected",
    [
        (None, None),
        ("", None),
        ("Тут есть слово тест", None),
        ("aaaaa", None),
        ("1111", None),
        ("Hello, World!", "Hello World"),
        ("Extra    whitespace", "Extra whitespace"),
        ("Valid string without issues", "Valid string without issues"),
    ],
)
def test_base_validation(param, expected):
    assert base_validation(param) == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("Сергій", True),
        ("Сергій Hello", True),
        ("Сергій Hello 123", True),
        ("Сергей 123", False),
        ("Сергей", False),
        ("Сергей", False),
    ],
)
def test_is_ukrainian_symbols(param, expected):
    assert is_ukrainian_symbols(param) == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("Сергей", True),
        ("Сергей123", True),
        ("Sergio", False),
        ("12345", False),
        ("!@#$%^", False),
        ("Серге й", True),
    ],
)
def test_is_cyrillic_symbols(param, expected):
    assert is_cyrillic_symbols(param) == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("Hello, World!", "Hello World"),
        ("Special#$Symbols!", "SpecialSymbols"),
        ("NoSpecialSymbolsHere", "NoSpecialSymbolsHere"),
        ("@Remove*These&Symbols$", "RemoveTheseSymbols"),
        ("1234%^&5678", "12345678"),
        ("Only-Some-Allowed", "Only-Some-Allowed"),
    ],
)
def test_remove_special_symbols(param, expected):
    assert remove_special_symbols(param) == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("   Leading and trailing spaces   ", "Leading and trailing spaces"),
        ("Multiple     spaces   inside", "Multiple spaces inside"),
        ("\tTabs\tand\nnewlines\r\nmixed", "Tabs and newlines mixed"),
        ("&nbsp;HTML&nbsp;entity&nbsp;", "HTML entity"),
        (" No &nbsp; extra  \t spaces\n here ", "No extra spaces here"),
        ("OnlySingleSpaces", "OnlySingleSpaces"),
    ],
)
def test_clean_whitespace(param, expected):
    assert clean_whitespace(param) == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("aaaa", True),
        ("1111", True),
        ("!!!!", True),
        ("A", True),
        ("bBbB", True),
        ("1234", False),
        ("", False),
        ("abab", False),
    ],
)
def test_is_single_character_or_digit_exist(param, expected):
    assert is_single_character_or_digit_exist(param) == expected
