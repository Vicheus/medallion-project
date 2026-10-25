import pytest

from ..validators.time import base_time_validation


@pytest.mark.parametrize(
    "param, input_format, output_format, expected",
    [
        ("14:30:00", "%H:%M:%S", "%H:%M", "14:30"),
        ("14:30", "%H:%M", "%H:%M", "14:30"),
        ("2:30 PM", "%I:%M %p", "%H:%M", "14:30"),
        ("invalid-time", "%H:%M:%S", "%H:%M", None),
        ("14:30:00", "%H:%M:%S", "%I:%M %p", "02:30 PM"),
        ("", "%H:%M:%S", "%H:%M", None),
        ("  14:30:00  ", "%H:%M:%S", "%H:%M", "14:30"),
        ("09:00:00", "%H:%M:%S", "%H:%M", "09:00"),
    ],
)
def test_base_time_validation(param, input_format, output_format, expected):
    result = base_time_validation(param, input_format, output_format)
    assert result == expected
