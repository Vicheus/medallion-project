import pytest

from parsetron.sections.document.validators.serial.document_serial_ru import (
    document_serial_passport,
    document_serial_driver_license,
    document_serial_international_passport,
    document_serial_birth_certificate,
    document_serial_resident_card,
    document_serial_diplomatic_passport,
    document_serial_service_passport,
    document_serial_military_identification_card,
)


@pytest.mark.parametrize(
    "param, expected",
    [
        ("1220202301", "1220202301"),
        ("12АА202301", None),
        ("0020202301", None),  # starts with double 0
        ("122020230", None),  # insufficient length
        ("12202023012", None),  # length exceeded
        ("series1220number2023012", None),  # numbers must be together
        ("number1220202301", "1220202301"),
        ("1220202301number", "1220202301"),
        ("invalid-value", None),
    ],
)
def test_document_serial_passport(param, expected):
    result = document_serial_passport(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("1220202301", "1220202301"),
        ("12АА202301", "12АА202301"),
        ("12рт202301", "12РТ202301"),  # to upper
        ("0020202301", None),  # starts with double 0
        ("12А202301", None),  # insufficient length
        ("12АА20230", None),  # insufficient length
        ("122020230", None),  # insufficient length
        ("122АА202301", None),  # insufficient pattern
        ("12202023012", None),  # length exceeded
        ("series1220number2023012", None),  # numbers must be together
        ("number1220202301", "1220202301"),
        ("1220202301number", "1220202301"),
        ("numberletter12АА202301", "12АА202301"),
        ("invalid-value", None),
    ],
)
def test_document_serial_driver_license(param, expected):
    result = document_serial_driver_license(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("122020230", None),  # invalid series
        ("992020230", None),  # invalid series
        ("502020230", "502020230"),
        ("50202023", None),  # insufficient length
        ("5020202301", None),  # length exceeded
        ("series50number2020230", None),  # numbers must be together
        ("number702020230", "702020230"),
        ("802020230number", "802020230"),
        ("invalid-value", None),
    ],
)
def test_document_serial_international_passport(param, expected):
    result = document_serial_international_passport(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("1-АЯ 436812", "1АЯ436812"),
        ("111-АЯ 436812", "111АЯ436812"),
        ("1-АЯ 4368121", None),
        ("8-АЯ 436812", "8АЯ436812"),
        ("81-АЯ 436812", None),
        ("18-АЯ 436812", None),
        ("IV-АЯ 202824", "IVАЯ202824"),
        ("1У-АЯ 202824", None),
        ("IIIIII-АЯ 202824", None),
        ("IVАя291571", "IVАЯ291571"),
        ("invalid-value", None),
    ],
)
def test_document_serial_birth_certificate(param, expected):
    result = document_serial_birth_certificate(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("80 8124698", "808124698"),
        ("80 812469", "800812469"),
        ("80 81246", None),
        ("80 81246987", None),
        ("84 8124698", None),
        ("90 8124698", "908124698"),
        ("number828124698", "828124698"),
        ("invalid-value", None),
    ],
)
def test_document_serial_resident_card(param, expected):
    result = document_serial_resident_card(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("112020230", None),  # invalid series
        ("102020230", "102020230"),
        ("10202023", None),  # insufficient length
        ("1020202301", None),  # length exceeded
        ("series10number2020230", None),  # numbers must be together
        ("number102020230", "102020230"),
        ("102020230number", "102020230"),
        ("invalid-value", None),
    ],
)
def test_document_serial_diplomatic_passport(param, expected):
    result = document_serial_diplomatic_passport(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("212020230", None),  # invalid series
        ("202020230", "202020230"),
        ("20202023", None),  # insufficient length
        ("2020202301", None),  # length exceeded
        ("series20number2020230", None),  # numbers must be together
        ("number202020230", "202020230"),
        ("202020230number", "202020230"),
        ("invalid-value", None),
    ],
)
def test_document_serial_service_passport(param, expected):
    result = document_serial_service_passport(param)
    assert result == expected


@pytest.mark.parametrize(
    "param, expected",
    [
        ("АА2935920", "АА2935920"),
        ("ААА935920", "ААА935920"),
        ("аб2935920", "АБ2935920"),
        ("АА293592", None),  # insufficient length
        ("АА29359201", None),  # length exceeded
        ("seriesААnumber2935920", None),
        ("numberАА2935920", "АА2935920"),
        ("АА2935920number", "АА2935920"),
        ("invalid-value", None),
    ],
)
def test_document_serial_military_identification_card(param, expected):
    result = document_serial_military_identification_card(param)
    assert result == expected
