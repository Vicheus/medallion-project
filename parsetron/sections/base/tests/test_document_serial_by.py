import pytest

from parsetron.sections.document.validators.serial.document_serial_by import (
    document_serial_passport,
    document_serial_diplomatic_passport,
)


@pytest.mark.parametrize(
    "param, expected",
    [
        ("0202301", None),
        ("ав0202301", "АВ0202301"),
        ("АВ02023012", None),
        ("02023012", None),
        ("020230", None),
        ("invalid-value", None),
    ],
)
def test_document_serial_passport(param, expected):
    result = document_serial_passport(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("0202301", None),
        ("sp0202301", "SP0202301"),
        ("SP02023012", None),
        ("02023012", None),
        ("020230", None),
        ("invalid-value", None),
    ],
)
def test_document_serial_diplomatic_passport(param, expected):
    result = document_serial_diplomatic_passport(param)
    assert result == expected
