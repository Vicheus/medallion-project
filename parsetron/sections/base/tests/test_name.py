import pytest

from parsetron.sections.main.validators.name import name, names


@pytest.mark.parametrize(
    "param, expected",
    [
        ("иванов", "Иванов"),
        ("ИВАНОВ", "Иванов"),
        ("иван Иванов", "Иван Иванов"),
        (" Иванов . . ", "Иванов"),
        (" Иванов И. И. ", "Иванов И. И"),
        ("-Горин", "Горин"),
        (". Лавренко", "Лавренко"),
        ("  - . Петров . ", "Петров"),
        ("  иВаНоВ  ", "Иванов"),
        ("Ив", None),
        (" А ", None),
        ("ааа", None),
        ("бббб", None),
        ("Иванов123", None),
        ("123", None),
        ("", None),
        (None, None),
    ],
)
def test_name(param, expected):
    result = name(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        (["иванов", "петров"], ["Иванов", "Петров"]),
        (["иванов", "ИВАНОВ", " Иванов "], ["Иванов"]),
        (["иванов", "ааа", "123", None], ["Иванов"]),
        (["ааа", "111", "", None], None),
        ([], None),
        (None, None),
        (["  - иванов . ", ". петров"], ["Иванов", "Петров"]),
    ],
)
def test_names(param, expected):
    result = names(param)

    if expected is None:
        assert result is None
    else:
        assert sorted(result) == sorted(expected)
