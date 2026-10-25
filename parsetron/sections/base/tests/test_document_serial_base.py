import pytest

from parsetron.sections.document.validators.serial.document_serial_base import (
    clean_doc_serial,
    is_doc_length_valid,
)


def test_clean_doc_serial():
    expected = "FSabАЫъюфиЁ"
    param = " !FS]. ab-АЫъю фиЁ;ії@ "
    result = clean_doc_serial(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("", False),
        (None, False),
        ("1111", False),  # insufficient length and symbols
        ("1234", True),
        ("112", True),
        ("1234567890", True),
    ],
)
def test_is_doc_length_valid(param, expected):
    result = is_doc_length_valid(param)
    assert result == expected
