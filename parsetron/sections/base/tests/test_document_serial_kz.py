import pytest

from parsetron.sections.document.validators.serial.document_serial_kz import (
    document_serial_passport,
)


@pytest.mark.parametrize(
    "param, expected",
    [
        ("2023012", None),
        ("n20230125", "N20230125"),
        ("N202301253", None),
        ("N2023012", None),
        ("2023012", None),
        ("invalid-value", None),
    ],
)
def test_document_serial_passport(param, expected):
    result = document_serial_passport(param)
    assert result == expected
