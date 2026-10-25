import pytest

from ..validators.date import base_date_validation


@pytest.mark.parametrize(
    "param, date_format, max_years_from, max_years_to, expected",
    [
        ("2023-01-21", "%Y-%m-%d", None, None, "21.01.2023"),
        ("2023-01-21", "%Y-%m-%d", 10, None, "21.01.2023"),
        ("2023-01-21", "%Y-%m-%d", 0, 0, "21.01.2023"),
        ("2025-01-21", "%Y-%m-%d", None, 5, "21.01.2025"),
        ("20230121", "%Y%m%d", None, None, "21.01.2023"),
        ("2010-01-21", "%Y-%m-%d", 10, None, None),
        ("2075-01-21", "%Y-%m-%d", None, 10, None),
        ("invalid-date", "%Y-%m-%d", None, None, None),
    ],
)
def test_base_date_validation(
    param, date_format, max_years_from, max_years_to, expected
):
    result = base_date_validation(param, date_format, max_years_from, max_years_to)
    assert result == expected
